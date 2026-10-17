"""One finite read-only public check; all artifacts remain inside the castle."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import runpy
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
OLD = ROOT / 'evidence/gardener-2026-10-16-service-check-5'
PARSER = OLD / 'observe.py'
parse = runpy.run_path(str(PARSER))['parse']

def digest(data):
    return hashlib.sha256(data).hexdigest()

def stamp():
    return datetime.now(timezone.utc).isoformat()

def save(name, value):
    with (HERE / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def garden_hashes():
    paths = [p for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()]
    assert all(p.resolve().is_relative_to(ROOT) for p in paths)
    return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in sorted(paths)}

def main():
    assert not (HERE / 'before.json').exists(), 'refuse a second collection'
    tracked = ['courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md',
               'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md',
               'words/reference-advertisement.md']
    questions = (ROOT / 'questions.md').read_text().splitlines()
    chronicle = (ROOT / 'chronicle.md').read_bytes()
    save('before.json', {'recorded_utc': stamp(),
         'tracked_sha256': {p: digest((ROOT / p).read_bytes()) for p in tracked},
         'chronicle_bytes': len(chronicle), 'chronicle_lines': len(chronicle.splitlines()),
         'question_lines_sha256': {str(i): digest(s.encode()) for i, s in enumerate(questions, 1)},
         'open_question_lines': [i for i, s in enumerate(questions, 1) if s.startswith('- [ ]')],
         'room_paths': sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'rooms').glob('*.md')),
         'garden_sha256': garden_hashes()})
    version = subprocess.run(['curl', '--disable', '--version'], capture_output=True,
                             text=True, check=True).stdout.splitlines()[0]
    fields = ['http_code', 'url_effective', 'content_type', 'http_version', 'num_redirects',
              'time_namelookup', 'time_connect', 'time_appconnect', 'time_pretransfer',
              'time_starttransfer', 'time_total', 'size_download', 'remote_ip',
              'proxy_used', 'ssl_verify_result']
    writeout = '\n'.join(f'{field}=%{{{field}}}' for field in fields)
    result = {'purpose': 'bounded 2026-10-17 check of questions 740, 744, 766',
              'curl_version': version, 'parser_path': str(PARSER.relative_to(ROOT)),
              'parser_sha256': digest(PARSER.read_bytes()), 'records': [],
              'stopped_reason': None, 'retries': 0, 'redirects_followed': False}
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
                proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=55)
                code, out, err = proc.returncode, proc.stdout, proc.stderr
            except subprocess.TimeoutExpired as exc:
                code, out, err = 124, '', str(exc)
            elapsed, finish = (time.monotonic_ns() - tick) / 1e9, stamp()
            metrics = dict(s.split('=', 1) for s in out.splitlines() if '=' in s)
            body = bp.read_bytes() if bp.exists() else None
            record = {'id': rid, 'url': url, 'method': 'GET', 'round': round_number,
                      'start_utc': start, 'finish_utc': finish,
                      'process_elapsed_monotonic_seconds': elapsed, 'curl_exit': code,
                      'curl_metrics': metrics, 'stdout': out, 'stderr': err,
                      'body_present': body is not None,
                      'body_bytes': len(body) if body is not None else None,
                      'body_sha256': digest(body) if body is not None else None, 'command': command}
            save(f'{rid}.json', record)
            result['records'].append(record)
            print(rid, metrics.get('http_code'), metrics.get('time_total'), record['body_bytes'], flush=True)
            status = int(metrics.get('http_code', '0'))
            challenge = body is not None and any(term in body[:32768].lower() for term in
                         (b'anubis', b'captcha', b'verify you are human', b'access denied'))
            if code or status in (401, 403, 407, 429, 451) or 300 <= status < 400 or challenge:
                result['stopped_reason'] = f'{rid}: curl={code}, HTTP={status}, challenge={challenge}'
                break
        if result['stopped_reason']:
            break
    save('manifest.json', result)
    comparisons = []
    for rec in result['records']:
        name = rec['id'].split('-', 1)[1]
        oldrec = json.loads((OLD / f'r2-{name}.json').read_text())
        oldbody = (OLD / f'r2-{name}.body').read_bytes()
        assert digest(oldbody) == oldrec['body_sha256']
        body = (HERE / f'{rec["id"]}.body').read_bytes() if rec['body_present'] else None
        parsed, problem = None, None
        if rec['curl_exit'] == 0 and rec['curl_metrics'].get('http_code') == '200':
            if rec['curl_metrics'].get('content_type', '').split(';')[0] != 'application/x-git-upload-pack-advertisement':
                problem = 'unexpected content type'
            else:
                try:
                    parsed = parse(body)
                except (AssertionError, ValueError, UnicodeError, TypeError) as exc:
                    problem = type(exc).__name__
        comparisons.append({'id': rec['id'], 'previous_capture': str((OLD / f'r2-{name}.json').relative_to(ROOT)),
                            'body_equal_to_previous': body == oldbody, 'parsed': parsed, 'parse_problem': problem})
    rows = result['records']
    previous = json.loads((OLD / 'manifest.json').read_text())['records']
    calc = {'comparisons': comparisons,
            'window_seconds': (datetime.fromisoformat(rows[-1]['finish_utc']) - datetime.fromisoformat(rows[0]['start_utc'])).total_seconds(),
            'previous_finish_to_start_seconds': (datetime.fromisoformat(rows[0]['start_utc']) - datetime.fromisoformat(previous[-1]['finish_utc'])).total_seconds(),
            'total_time_min': min(float(r['curl_metrics']['time_total']) for r in rows if 'time_total' in r['curl_metrics']),
            'total_time_max': max(float(r['curl_metrics']['time_total']) for r in rows if 'time_total' in r['curl_metrics'])}
    save('comparison.json', calc)
    print(json.dumps(calc, indent=2))

if __name__ == '__main__':
    main()
