"""Finite public reads; refuse overwrite. All artifacts stay inside the castle."""
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


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(name, value):
    with (HERE / name).open('x') as f:
        json.dump(value, f, indent=2)
        f.write('\n')


def parse(body):
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
    return {'references': refs, 'capabilities': caps, 'packet_count': len(packets)}


def main():
    assert not (HERE/'before.json').exists(), 'collection already started'
    tracked = ['courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md',
               'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md',
               'words/response-time.md', 'words/timeout.md']
    questions = (ROOT/'questions.md').read_text().splitlines()
    chronicle = (ROOT/'chronicle.md').read_bytes()
    save('before.json', {
        'recorded_utc': stamp(),
        'tracked_sha256': {p: sha((ROOT/p).read_bytes()) for p in tracked},
        'chronicle_bytes': len(chronicle), 'chronicle_lines': len(chronicle.splitlines()),
        'question_lines_sha256': {str(i): sha(line.encode()) for i, line in enumerate(questions, 1)},
        'open_question_lines': [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')],
        'garden_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes())
                          for p in sorted((ROOT/'garden').rglob('*'))
                          if p.is_file() and not p.is_symlink()},
    })
    version = subprocess.run(['curl', '--disable', '--version'], capture_output=True,
                             text=True, check=True).stdout.splitlines()[0]
    fields = ['http_code', 'url_effective', 'content_type', 'http_version', 'num_redirects',
              'time_namelookup', 'time_connect', 'time_appconnect', 'time_pretransfer',
              'time_starttransfer', 'time_total', 'size_download', 'remote_ip',
              'proxy_used', 'ssl_verify_result']
    writeout = '\n'.join(f'{field}=%{{{field}}}' for field in fields)
    manifest = {'purpose': 'fifth bounded check of questions 740, 744, 766',
                'curl_version': version, 'records': [], 'stopped_reason': None,
                'retries': 0, 'redirects_followed': False, 'new_watch_started': False}
    for round_number in (1, 2):
        for name in ('orgmode', 'emacs', 'guix'):
            rid = f'r{round_number}-{name}'
            url = f'https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack'
            bp, hp = HERE/f'{rid}.body', HERE/f'{rid}.headers'
            assert not bp.exists() and not hp.exists()
            command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https',
                       '--connect-timeout', '10', '--max-time', '45', '--max-filesize', '1048576',
                       '--retry', '0', '--user-agent', 'castle-gardener/1.0',
                       '--header', 'Accept-Encoding: identity', '--header', 'Git-Protocol: version=0',
                       '--dump-header', str(hp.relative_to(ROOT)), '--output', str(bp.relative_to(ROOT)),
                       '--write-out', writeout, url]
            start, tick = stamp(), time.monotonic_ns()
            try:
                r = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=55)
                code, out, err = r.returncode, r.stdout, r.stderr
            except subprocess.TimeoutExpired as exc:
                code, out, err = 124, '', str(exc)
            elapsed, finish = (time.monotonic_ns()-tick)/1e9, stamp()
            metrics = dict(line.split('=', 1) for line in out.splitlines() if '=' in line)
            body = bp.read_bytes() if bp.exists() else None
            rec = {'id': rid, 'url': url, 'method': 'GET', 'round': round_number,
                   'request_headers': {'User-Agent': 'castle-gardener/1.0',
                                      'Accept-Encoding': 'identity', 'Git-Protocol': 'version=0'},
                   'start_utc': start, 'finish_utc': finish,
                   'process_elapsed_monotonic_seconds': elapsed, 'curl_exit': code,
                   'curl_metrics': metrics, 'stdout': out, 'stderr': err,
                   'body_present': body is not None,
                   'body_bytes': len(body) if body is not None else None,
                   'body_sha256': sha(body) if body is not None else None, 'command': command}
            save(f'{rid}.json', rec)
            manifest['records'].append(rec)
            print(rid, metrics.get('http_code'), metrics.get('time_total'), rec['body_bytes'], flush=True)
            status = int(metrics.get('http_code', '0'))
            challenge = body is not None and any(x in body[:32768].lower() for x in
                        (b'anubis', b'captcha', b'verify you are human', b'access denied'))
            if code or status in (401, 403, 407, 429, 451) or 300 <= status < 400 or challenge:
                manifest['stopped_reason'] = f'{rid}: curl={code}, HTTP={status}, challenge={challenge}'
                break
        if manifest['stopped_reason']:
            break
    save('manifest.json', manifest)
    dirs = [ROOT/'evidence'/('gardener-2026-10-16-service-check'+suffix)
            for suffix in ('', '-2', '-3', '-4', '-5')]
    comparisons = []
    for directory in dirs:
        for rec in json.loads((directory/'manifest.json').read_text())['records']:
            if not rec['body_present']:
                continue
            body = (directory/f'{rec["id"]}.body').read_bytes()
            assert sha(body) == rec['body_sha256']
            parsed, parse_problem = None, None
            if rec['curl_exit'] == 0 and rec['curl_metrics']['http_code'] == '200':
                content_type = rec['curl_metrics']['content_type'].split(';')[0]
                if content_type != 'application/x-git-upload-pack-advertisement':
                    parse_problem = f'unexpected content type: {content_type}'
                else:
                    try:
                        parsed = parse(body)
                    except (AssertionError, ValueError, UnicodeError) as exc:
                        parse_problem = f'unparseable Git advertisement: {type(exc).__name__}'
            comparisons.append({'capture': f'{directory.name}/{rec["id"]}',
                                'sha256': sha(body), 'parsed': parsed, 'parse_problem': parse_problem})
    records = manifest['records']
    old = json.loads((dirs[-2]/'manifest.json').read_text())['records']
    result = {'captures': comparisons,
              'orgmode_hashes': sorted({c['sha256'] for c in comparisons if c['parsed']}),
              'orgmode_parsed_views_equal': all(c['parsed'] == comparisons[0]['parsed']
                                               for c in comparisons if c['parsed']),
              'window_seconds': (datetime.fromisoformat(records[-1]['finish_utc'])-
                                 datetime.fromisoformat(records[0]['start_utc'])).total_seconds(),
              'previous_check_finish_to_this_start_seconds':
                  (datetime.fromisoformat(records[0]['start_utc'])-
                   datetime.fromisoformat(old[-1]['finish_utc'])).total_seconds()}
    save('comparison.json', result)
    print(json.dumps({k: v for k, v in result.items() if k != 'captures'}, indent=2))


if __name__ == '__main__':
    main()
