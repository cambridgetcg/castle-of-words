"""One bounded collection, six GETs at most. Refuse to overwrite receipts."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
OLD = [ROOT / 'evidence' / ('gardener-2026-10-16-service-check' + suffix)
       for suffix in ('', '-2', '-3')]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(name, value):
    with (HERE / name).open('x') as f:
        json.dump(value, f, indent=2)
        f.write('\n')


def parse(body):
    """Strict narrow decoder for the observed SHA-1 protocol-v0 advertisement."""
    packets, pos = [], 0
    while pos < len(body):
        prefix = body[pos:pos+4]
        assert re.fullmatch(rb'[0-9a-fA-F]{4}', prefix)
        n = int(prefix, 16)
        if n == 0:
            packets.append(None)
            pos += 4
        else:
            assert 4 <= n <= 65520 and pos+n <= len(body)
            packets.append(body[pos+4:pos+n])
            pos += n
    assert len(packets) >= 4 and packets[0] == b'# service=git-upload-pack\n'
    assert packets[1] is None and packets[-1] is None
    refs, caps = {}, []
    for i, packet in enumerate(packets[2:-1]):
        assert packet is not None
        line = packet.removesuffix(b'\n')
        if i == 0:
            line, capability = line.split(b'\x00')
            caps = capability.decode('ascii').split()
        m = re.fullmatch(rb'([0-9a-f]{40}) (\S+)', line)
        assert m
        oid, name = (part.decode('ascii') for part in m.groups())
        assert name not in refs
        refs[name] = oid
    return {'references': refs, 'capabilities': caps, 'packet_count': len(packets), 'bytes_consumed': pos}


assert not (HERE / 'before.json').exists(), 'collection already started'
tracked = ['courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md',
           'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md',
           'words/response-time.md', 'words/name-lookup-time.md']
q = (ROOT / 'questions.md').read_text().splitlines()
c = (ROOT / 'chronicle.md').read_bytes()
save('before.json', {
    'recorded_utc': stamp(),
    'tracked_sha256': {name: sha((ROOT / name).read_bytes()) for name in tracked},
    'chronicle_bytes': len(c), 'chronicle_sha256': sha(c),
    'chronicle_lines': len(c.splitlines()),
    'question_lines_sha256': {str(i): sha(line.encode()) for i, line in enumerate(q, 1)},
    'open_question_lines': [i for i, line in enumerate(q, 1) if line.startswith('- [ ]')],
    'garden_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes())
                      for p in sorted((ROOT / 'garden').rglob('*'))
                      if p.is_file() and not p.is_symlink()},
})
version = subprocess.run(['curl', '--disable', '--version'], capture_output=True,
                         text=True, check=True).stdout.splitlines()[0]
fields = ['http_code', 'url_effective', 'content_type', 'http_version', 'num_redirects',
          'time_namelookup', 'time_connect', 'time_appconnect', 'time_pretransfer',
          'time_starttransfer', 'time_total', 'size_download', 'remote_ip',
          'proxy_used', 'ssl_verify_result']
writeout = '\n'.join(f'{field}=%{{{field}}}' for field in fields)
manifest = {'purpose': 'fourth bounded check of questions 740, 744, 766',
            'curl_version': version, 'records': [], 'stopped_reason': None,
            'retries': 0, 'redirects_followed': False, 'new_watch_started': False}
for round_number in (1, 2):
    for name in ('orgmode', 'emacs', 'guix'):
        rid = f'r{round_number}-{name}'
        url = f'https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack'
        bp, hp = HERE / f'{rid}.body', HERE / f'{rid}.headers'
        assert not bp.exists() and not hp.exists()
        command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https',
                   '--connect-timeout', '10', '--max-time', '45', '--max-filesize', '1048576',
                   '--retry', '0', '--user-agent', 'castle-gardener/1.0',
                   '--header', 'Accept-Encoding: identity', '--header', 'Git-Protocol: version=0',
                   '--dump-header', str(hp.relative_to(ROOT)), '--output', str(bp.relative_to(ROOT)),
                   '--write-out', writeout, url]
        start, tick = stamp(), time.monotonic_ns()
        try:
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=55)
            code, out, error = result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired as exc:
            code, out, error = 124, '', str(exc)
        elapsed, finish = (time.monotonic_ns()-tick)/1e9, stamp()
        metrics = dict(line.split('=', 1) for line in out.splitlines() if '=' in line)
        body = bp.read_bytes() if bp.exists() else None
        record = {'id': rid, 'url': url, 'method': 'GET', 'round': round_number,
                  'request_headers': {'User-Agent': 'castle-gardener/1.0',
                                      'Accept-Encoding': 'identity', 'Git-Protocol': 'version=0'},
                  'start_utc': start, 'finish_utc': finish, 'process_elapsed_monotonic_seconds': elapsed,
                  'curl_exit': code, 'curl_metrics': metrics, 'stdout': out, 'stderr': error,
                  'body_present': body is not None, 'body_bytes': len(body) if body is not None else None,
                  'body_sha256': sha(body) if body is not None else None, 'command': command}
        save(f'{rid}.json', record)
        manifest['records'].append(record)
        print(rid, metrics.get('http_code'), metrics.get('time_total'), record['body_bytes'], flush=True)
        status = int(metrics.get('http_code', '0'))
        challenge = body is not None and any(x in body[:32768].lower() for x in
                    (b'anubis', b'captcha', b'verify you are human', b'access denied'))
        if code or status in (401, 403, 407, 429, 451) or 300 <= status < 400 or challenge:
            manifest['stopped_reason'] = f'{rid}: curl={code}, HTTP={status}, challenge={challenge}'
            break
    if manifest['stopped_reason']:
        break
save('manifest.json', manifest)
comparison = {'captures': {}, 'pairs': [], 'limits': 'saved views only, not continuous service history'}
for directory in [*OLD, HERE]:
    for r in json.loads((directory / 'manifest.json').read_text())['records']:
        key = f'{directory.name}/{r["id"]}'
        body = (directory / f'{r["id"]}.body').read_bytes() if r['body_present'] else None
        parsed, problem = None, None
        if r['curl_exit'] == 0 and r['curl_metrics']['http_code'] == '200':
            try:
                assert r['curl_metrics']['content_type'].split(';')[0] == 'application/x-git-upload-pack-advertisement'
                parsed = parse(body)
            except (AssertionError, ValueError, UnicodeError) as exc:
                problem = str(exc) or type(exc).__name__
        comparison['captures'][key] = {'record': r, 'parsed': parsed, 'parse_problem': problem}
keys = [k for k, v in comparison['captures'].items() if v['parsed'] is not None]
for left, right in zip(keys, keys[1:]):
    a, b = comparison['captures'][left], comparison['captures'][right]
    ad, ai = left.split('/')
    bd, bi = right.split('/')
    comparison['pairs'].append({
        'left': left, 'right': right,
        'same_method_url_headers': all(a['record'][k] == b['record'][k] for k in ('method', 'url', 'request_headers')),
        'body_byte_equal': (ROOT/'evidence'/ad/f'{ai}.body').read_bytes() == (ROOT/'evidence'/bd/f'{bi}.body').read_bytes(),
        'references_equal': a['parsed']['references'] == b['parsed']['references'],
        'capabilities_equal': a['parsed']['capabilities'] == b['parsed']['capabilities'],
        'request_start_spacing_seconds': (datetime.fromisoformat(b['record']['start_utc'])-datetime.fromisoformat(a['record']['start_utc'])).total_seconds(),
        'between_processes_seconds': (datetime.fromisoformat(b['record']['start_utc'])-datetime.fromisoformat(a['record']['finish_utc'])).total_seconds(),
    })
r = manifest['records']
comparison['observation_window_seconds'] = (datetime.fromisoformat(r[-1]['finish_utc'])-datetime.fromisoformat(r[0]['start_utc'])).total_seconds()
save('comparison.json', comparison)
print(json.dumps({k: v for k, v in comparison.items() if k != 'captures'}, indent=2))
