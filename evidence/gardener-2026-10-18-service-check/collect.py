"""A finite read-only collection; no background process, no overwrites."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import runpy
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / 'evidence/gardener-2026-10-17-service-check-6'
PARSER = ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, data):
    with (HERE / name).open('x') as f:
        json.dump(data, f, indent=2)
        f.write('\n')


def stamp():
    return datetime.now(timezone.utc).isoformat()


def main():
    assert ROOT == Path('/Users/yu/castle')
    assert not (HERE / 'before.json').exists(), 'refuse repeated collection'
    tracked = list((ROOT / 'rooms').glob('*.md')) + list((ROOT / 'words').glob('*.md'))
    tracked += [ROOT / p for p in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md')]
    garden = [p for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()]
    assert all(p.resolve().is_relative_to(ROOT) for p in tracked + garden)
    chronicle = (ROOT / 'chronicle.md').read_bytes()
    save('before.json', {
        'utc': stamp(),
        'content_hashes': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in tracked},
        'garden_hashes': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in garden},
        'chronicle_bytes': len(chronicle),
        'plan_sha256': sha((HERE / 'README.md').read_bytes()),
        'parser_path': str(PARSER.relative_to(ROOT)), 'parser_sha256': sha(PARSER.read_bytes())})
    parse = runpy.run_path(str(PARSER))['parse']
    old_records = json.loads((OLD / 'manifest.json').read_text())['records']
    latest = {}
    for rec in old_records:
        if rec['curl_exit'] == 0 and rec['body_present']:
            latest[rec['id'].split('-', 1)[1]] = rec
    fields = ['http_code', 'url_effective', 'content_type', 'http_version', 'num_redirects',
              'time_namelookup', 'time_connect', 'time_appconnect', 'time_pretransfer',
              'time_starttransfer', 'time_total', 'size_download', 'remote_ip',
              'proxy_used', 'ssl_verify_result']
    writeout = '\n'.join(f'{key}=%{{{key}}}' for key in fields)
    manifest = {'curl_version': subprocess.run(['curl', '--disable', '--version'],
                capture_output=True, text=True, check=True).stdout.splitlines()[0],
                'records': [], 'stop_reason': None, 'planned_maximum_requests': 6}
    comparisons = []
    for round_number in (1, 2):
        for name in ('orgmode', 'emacs', 'guix'):
            rid = f'r{round_number}-{name}'
            url = f'https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack'
            bp, hp = HERE / (rid + '.body'), HERE / (rid + '.headers')
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
            rec = {'id': rid, 'url': url, 'round': round_number, 'command': command,
                   'start_utc': start, 'finish_utc': finish, 'process_elapsed_monotonic_seconds': elapsed,
                   'curl_exit': code, 'curl_metrics': metrics, 'stdout': out, 'stderr': err,
                   'body_present': body is not None, 'body_bytes': None if body is None else len(body),
                   'body_sha256': None if body is None else sha(body)}
            save(rid + '.json', rec)
            manifest['records'].append(rec)
            old_rec = latest.get(name)
            old_body = None if old_rec is None else (OLD / (old_rec['id'] + '.body')).read_bytes()
            if old_body is not None:
                assert old_rec is not None
                assert sha(old_body) == old_rec['body_sha256']
            complete = code == 0 and body is not None
            parsed, problem = None, None
            if complete and metrics.get('http_code') == '200':
                try:
                    assert metrics.get('content_type', '').split(';')[0] == 'application/x-git-upload-pack-advertisement'
                    parsed = parse(body)
                except (AssertionError, ValueError, UnicodeError, TypeError) as exc:
                    problem = type(exc).__name__
            comparisons.append({'id': rid,
                'previous_complete_capture': None if old_rec is None else str((OLD / (old_rec['id'] + '.json')).relative_to(ROOT)),
                'body_equal_to_previous': None if not complete or old_body is None else body == old_body,
                'parsed': parsed, 'parse_problem': problem})
            print(rid, metrics.get('http_code'), metrics.get('time_total'), code, rec['body_bytes'], flush=True)
            status = int(metrics.get('http_code', '0'))
            challenge = body is not None and any(t in body[:32768].lower() for t in
                         (b'anubis', b'captcha', b'verify you are human', b'access denied'))
            if code or status in (401, 403, 407, 429, 451) or 300 <= status < 400 or challenge:
                manifest['stop_reason'] = f'{rid}: curl={code}, HTTP={status}, challenge={challenge}'
                break
        if manifest['stop_reason']:
            break
    save('manifest.json', manifest)
    rows = manifest['records']
    save('comparison.json', {
        'comparisons': comparisons,
        'observation_window_seconds': (datetime.fromisoformat(rows[-1]['finish_utc']) - datetime.fromisoformat(rows[0]['start_utc'])).total_seconds(),
        'previous_attempt_finish_to_start_seconds': (datetime.fromisoformat(rows[0]['start_utc']) - datetime.fromisoformat(old_records[-1]['finish_utc'])).total_seconds(),
        'previous_complete_orgmode_finish_to_start_seconds': (datetime.fromisoformat(rows[0]['start_utc']) - datetime.fromisoformat(latest['orgmode']['finish_utc'])).total_seconds()})
    print(json.dumps(comparisons, indent=2))


if __name__ == '__main__':
    main()
