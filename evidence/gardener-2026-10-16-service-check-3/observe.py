"""Finite public GETs for three uncommissioned questions. No retries or scheduler."""
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
OLD = [ROOT / 'evidence/gardener-2026-10-16-service-check',
       ROOT / 'evidence/gardener-2026-10-16-service-check-2']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(name, value):
    with (HERE / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')


def parse(data):
    packets, pos = [], 0
    while pos < len(data):
        prefix = data[pos:pos+4]
        assert re.fullmatch(b'[0-9a-fA-F]{4}', prefix), 'invalid packet length'
        size = int(prefix, 16)
        if size == 0:
            packets.append(None)
            pos += 4
        else:
            assert 4 <= size <= 65520 and pos + size <= len(data)
            packets.append(data[pos+4:pos+size])
            pos += size
    assert len(packets) >= 4
    assert packets[0] == b'# service=git-upload-pack\n'
    assert packets[1] is None and packets[-1] is None
    refs, caps = {}, []
    for i, packet in enumerate(packets[2:-1]):
        assert packet is not None
        payload = packet.removesuffix(b'\n')
        if i == 0:
            payload, capabilities = payload.split(b'\x00')
            caps = capabilities.decode('ascii').split()
        match = re.fullmatch(rb'([0-9a-f]{40}) (\S+)', payload)
        assert match, 'unexpected reference line'
        oid, name = (part.decode('ascii') for part in match.groups())
        assert name not in refs
        refs[name] = oid
    return {'references': refs, 'capabilities': caps, 'packet_count': len(packets),
            'bytes_consumed': pos}


assert not (HERE / 'manifest.json').exists(), 'already collected'
questions = (ROOT / 'questions.md').read_text().splitlines()
chronicle = (ROOT / 'chronicle.md').read_bytes()
tracked = ['courtyard.md', 'questions.md', 'quests.md', 'gate.md',
           'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md']
save('before.json', {
    'recorded_utc': stamp(),
    'chronicle_bytes': len(chronicle), 'chronicle_sha256': sha(chronicle),
    'chronicle_lines': len(chronicle.splitlines()),
    'open_question_line_hashes': {str(i): sha(line.encode())
                                for i, line in enumerate(questions, 1)
                                if line.startswith('- [ ]')},
    'tracked_sha256': {name: sha((ROOT / name).read_bytes()) for name in tracked},
    'garden_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes())
                      for p in sorted((ROOT / 'garden').rglob('*'))
                      if p.is_file() and not p.is_symlink()},
})
version = subprocess.run(['curl', '--disable', '--version'], capture_output=True,
                         text=True, check=True).stdout.splitlines()[0]
fields = ['http_code', 'url_effective', 'content_type', 'http_version',
          'num_redirects', 'time_namelookup', 'time_connect', 'time_appconnect',
          'time_pretransfer', 'time_starttransfer', 'time_total', 'size_download',
          'remote_ip', 'proxy_used', 'ssl_verify_result']
write_out = '\n'.join(f'{key}=%{{{key}}}' for key in fields)
manifest = {'purpose': 'third bounded read for questions 740, 744, 766 only',
            'curl_version': version, 'retries': 0, 'redirects_followed': False,
            'new_watch_started': False, 'records': [], 'stopped_reason': None}
for round_number in (1, 2):
    for name in ('orgmode', 'emacs', 'guix'):
        rid = f'r{round_number}-{name}'
        url = f'https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack'
        body_path, header_path = HERE / f'{rid}.body', HERE / f'{rid}.headers'
        assert not body_path.exists() and not header_path.exists()
        command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https',
                   '--connect-timeout', '10', '--max-time', '45', '--max-filesize', '1048576',
                   '--retry', '0', '--user-agent', 'castle-gardener/1.0',
                   '--header', 'Accept-Encoding: identity', '--header', 'Git-Protocol: version=0',
                   '--dump-header', str(header_path.relative_to(ROOT)),
                   '--output', str(body_path.relative_to(ROOT)), '--write-out', write_out, url]
        start, tick = stamp(), time.monotonic_ns()
        try:
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=55)
            code, out, error = result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired as exc:
            code, out, error = 124, '', str(exc)
        elapsed, finish = (time.monotonic_ns() - tick) / 1e9, stamp()
        metrics = dict(line.split('=', 1) for line in out.splitlines() if '=' in line)
        body = body_path.read_bytes() if body_path.exists() else None
        record = {'id': rid, 'url': url, 'method': 'GET', 'round': round_number,
                  'request_headers': {'User-Agent': 'castle-gardener/1.0',
                                      'Accept-Encoding': 'identity', 'Git-Protocol': 'version=0'},
                  'start_utc': start, 'finish_utc': finish,
                  'process_elapsed_monotonic_seconds': elapsed,
                  'curl_exit': code, 'curl_metrics': metrics, 'stderr': error, 'stdout': out,
                  'body_present': body is not None, 'body_bytes': len(body) if body is not None else None,
                  'body_sha256': sha(body) if body is not None else None, 'command': command}
        save(f'{rid}.json', record)
        manifest['records'].append(record)
        print(rid, metrics.get('http_code'), metrics.get('time_total'), record['body_bytes'], flush=True)
        status = int(metrics.get('http_code', '0'))
        challenge = body is not None and any(marker in body[:32768].lower() for marker in
                    (b'anubis', b'captcha', b'verify you are human', b'access denied'))
        if code or status in (401, 403, 407, 429, 451) or 300 <= status < 400 or challenge:
            manifest['stopped_reason'] = f'boundary at {rid}: curl={code}, status={status}, challenge={challenge}'
            break
    if manifest['stopped_reason']:
        break
save('manifest.json', manifest)

comparison = {'captures': {}, 'pairs': [], 'limits': 'captured views only, not continuity or origin update times'}
for directory in [*OLD, HERE]:
    records = json.loads((directory / 'manifest.json').read_text())['records']
    for record in records:
        key = f'{directory.name}/{record["id"]}'
        body = (directory / f'{record["id"]}.body').read_bytes() if record['body_present'] else None
        parsed, problem = None, None
        if record['curl_exit'] == 0 and record['curl_metrics']['http_code'] == '200':
            try:
                assert record['curl_metrics']['content_type'].split(';')[0] == 'application/x-git-upload-pack-advertisement'
                parsed = parse(body)
            except (AssertionError, ValueError, UnicodeError) as exc:
                problem = str(exc) or type(exc).__name__
        comparison['captures'][key] = {'body_sha256': sha(body) if body is not None else None,
                                      'record': record, 'parsed': parsed, 'parse_problem': problem}
keys = [key for key, value in comparison['captures'].items() if value['parsed'] is not None]
for left, right in zip(keys, keys[1:]):
    a, b = comparison['captures'][left], comparison['captures'][right]
    left_dir, left_id = left.split('/')
    right_dir, right_id = right.split('/')
    abody = (ROOT / 'evidence' / left_dir / f'{left_id}.body').read_bytes()
    bbody = (ROOT / 'evidence' / right_dir / f'{right_id}.body').read_bytes()
    comparison['pairs'].append({
        'left': left, 'right': right,
        'same_method_url_headers': all(a['record'][k] == b['record'][k] for k in ('method', 'url', 'request_headers')),
        'body_byte_equal': abody == bbody,
        'references_equal': a['parsed']['references'] == b['parsed']['references'],
        'capabilities_equal': a['parsed']['capabilities'] == b['parsed']['capabilities'],
        'request_start_spacing_seconds': (datetime.fromisoformat(b['record']['start_utc']) - datetime.fromisoformat(a['record']['start_utc'])).total_seconds(),
        'between_processes_seconds': (datetime.fromisoformat(b['record']['start_utc']) - datetime.fromisoformat(a['record']['finish_utc'])).total_seconds(),
    })
records = manifest['records']
comparison['observation_window_seconds'] = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
save('comparison.json', comparison)
print(json.dumps({k: v for k, v in comparison.items() if k != 'captures'}, indent=2))
