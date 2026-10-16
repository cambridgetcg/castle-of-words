"""Offline verification only: never repeat a service request."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from io import BytesIO
from pathlib import Path
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
PRE = '--pre-close' in sys.argv


def load(name):
    return json.loads((HERE/name).read_text())


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dt(value):
    return datetime.fromisoformat(value)


def decode(data):
    """A separate narrow decoder using stream reads, not the collector's parser."""
    stream = BytesIO(data)
    payloads = []
    while True:
        header = stream.read(4)
        if not header:
            break
        assert len(header) == 4 and re.fullmatch(rb'[0-9a-f]{4}', header)
        length = int(header, 16)
        if length == 0:
            payloads.append(None)
            continue
        assert 4 <= length <= 65520
        payload = stream.read(length-4)
        assert len(payload) == length-4
        payloads.append(payload)
    assert payloads[:2] == [b'# service=git-upload-pack\n', None]
    assert payloads[-1] is None and len(payloads) == 5
    references, capabilities = {}, []
    for position, payload in enumerate(payloads[2:-1]):
        assert payload is not None and payload.endswith(b'\n')
        line = payload[:-1]
        if position == 0:
            line, sep, cap = line.partition(b'\x00')
            assert sep
            capabilities = cap.decode('ascii').split(' ')
        oid, sep, name = line.partition(b' ')
        assert sep and re.fullmatch(rb'[0-9a-f]{40}', oid)
        assert name and name.decode('ascii') not in references
        references[name.decode('ascii')] = oid.decode('ascii')
    return {'references': references, 'capabilities': capabilities, 'packet_count': len(payloads)}


before, manifest = load('before.json'), load('manifest.json')
records = manifest['records']
assert len(records) == 6 and manifest['stopped_reason'] is None
assert [r['id'] for r in records] == [f'r{i}-{name}' for i in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
assert not manifest['retries'] and not manifest['redirects_followed'] and not manifest['new_watch_started']
assert manifest['curl_version'].startswith('curl 8.7.1 ')
parsed = []
for i, r in enumerate(records):
    assert load(r['id']+'.json') == r
    metrics, command = r['curl_metrics'], r['command']
    assert r['curl_exit'] == 0 and r['stderr'] == '' and r['body_present']
    assert r['method'] == 'GET' and r['url'].startswith('https://yhetil.org/')
    assert command[:2] == ['curl', '--disable']
    for flag, expected in [('--retry', '0'), ('--max-time', '45'), ('--connect-timeout', '10'),
                           ('--proto', '=https'), ('--max-filesize', '1048576')]:
        assert command[command.index(flag)+1] == expected
    assert not any(flag in command for flag in ('--fail', '--fail-with-body', '-L', '--location', '-k', '--insecure'))
    assert r['request_headers'] == {'User-Agent': 'castle-gardener/1.0',
                                   'Accept-Encoding': 'identity', 'Git-Protocol': 'version=0'}
    assert all(metrics[key] == '0' for key in ('num_redirects', 'proxy_used', 'ssl_verify_result'))
    assert dt(r['start_utc']) < dt(r['finish_utc'])
    if i:
        assert dt(records[i-1]['finish_utc']) <= dt(r['start_utc'])
    assert 0 < Decimal(metrics['time_total']) < 1
    assert r['process_elapsed_monotonic_seconds'] >= float(metrics['time_total'])
    raw = (HERE/(r['id']+'.body')).read_bytes()
    headers = (HERE/(r['id']+'.headers')).read_bytes()
    assert len(raw) == r['body_bytes'] == int(metrics['size_download'])
    assert sha(raw) == r['body_sha256']
    assert headers.startswith(('HTTP/1.1 '+metrics['http_code']).encode())
    if r['id'].endswith('orgmode'):
        assert metrics['http_code'] == '200'
        assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
        assert len(raw) == 370
        parsed.append(decode(raw))
    else:
        assert metrics['http_code'] == '500' and raw == b'Internal Server Error'
assert parsed[0] == parsed[1]
assert parsed[0]['references'] == {'HEAD': 'ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb',
                                  'refs/heads/master': 'ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb'}
assert 'symref=HEAD:refs/heads/master' in parsed[0]['capabilities']
comparison = load('comparison.json')
for capture in comparison['captures']:
    folder, rid = capture['capture'].split('/')
    directory = ROOT/'evidence'/folder
    raw = (directory/(rid+'.body')).read_bytes()
    record = json.loads((directory/'manifest.json').read_text())['records']
    old = next(r for r in record if r['id'] == rid)
    assert sha(raw) == capture['sha256'] == old['body_sha256']
    current = next(r for r in records if r['id'].split('-', 1)[1] == rid.split('-', 1)[1])
    assert all(old[k] == current[k] for k in ('method', 'url', 'request_headers'))
    assert raw == (HERE/(current['id']+'.body')).read_bytes()
    if capture['parsed']:
        assert decode(raw) == capture['parsed'] == parsed[0]
old_guix = json.loads((HERE.parent/'gardener-2026-10-16-service-check-4/r1-guix.json').read_text())
assert old_guix['curl_exit'] == 28 and old_guix['curl_metrics']['http_code'] == '000'
assert not old_guix['body_present'] and not (HERE.parent/'gardener-2026-10-16-service-check-4/r1-guix.body').exists()
window = (dt(records[-1]['finish_utc'])-dt(records[0]['start_utc'])).total_seconds()
gap = (dt(records[2]['start_utc'])-dt(old_guix['finish_utc'])).total_seconds()
assert window == comparison['window_seconds'] == 2.564883
assert gap == load('calculations.json')['last_guix_timeout_finish_to_current_guix_start_seconds'] == 11812.414061
for source in load('sources.json')['requests']:
    assert source['http_code'] == '200' and source['curl_exit'] == 0
    assert dt(source['start_utc']) > dt(records[-1]['finish_utc'])
    assert sha((HERE/source['file']).read_bytes()) == source['sha256']
assert load('search-links.json')['results']
questions = (ROOT/'questions.md').read_text().splitlines()
assert len(questions) == len(before['question_lines_sha256'])
changed = [i for i, line in enumerate(questions, 1)
           if sha(line.encode()) != before['question_lines_sha256'][str(i)]]
assert changed == [740, 744, 766]
assert all('fifth bounded check' in questions[i-1] and questions[i-1].startswith('- [ ]') for i in changed)
open_lines = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
assert open_lines == before['open_question_lines'] and len(open_lines) == 16
for name in ('courtyard.md', 'quests.md', 'words/response-time.md', 'words/timeout.md'):
    assert sha((ROOT/name).read_bytes()) == before['tracked_sha256'][name]
assert not any(line.startswith('- ') for line in (ROOT/'courtyard.md').read_text().splitlines())
assert sum(line.startswith('- [ ]') for line in (ROOT/'quests.md').read_text().splitlines()) == 8
garden = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sorted((ROOT/'garden').rglob('*'))
          if p.is_file() and not p.is_symlink()}
assert garden == before['garden_sha256']
map_section = (ROOT/'gate.md').read_text().split('## Map', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/)]+)\.md\).+$', map_section, re.M)
rooms = {p.stem for p in (ROOT/'rooms').glob('*.md')}
assert set(entries) == rooms and all(n == 1 for n in Counter(entries).values())
assert len(rooms) == load('pre-edit-map-audit.json')['rooms'] == 697
word = (ROOT/'words/http-status.md').read_text()
assert word.startswith('# http-status\n\nAn HTTP status') and word.rstrip().splitlines()[-1].startswith('Links: ')
for name in ('what-the-gaps-can-say', 'measuring-the-window'):
    lines = (ROOT/'rooms'/f'{name}.md').read_text().splitlines()
    assert lines[0] == '# '+name and lines[2].startswith('*') and lines[2].endswith('*')
    assert lines[4].startswith('This room gathers')
# Check every newly introduced Markdown path and wiki-link; old sections are not rewritten.
parts = [(ROOT/'words/http-status.md', word), (HERE/'README.md', (HERE/'README.md').read_text())]
for name, heading, end in [('what-the-gaps-can-say', '## A reply returned, not a repaired service', '\n## Sources'),
                           ('measuring-the-window', '## A quick error does not close a fault', '\nLinks:')]:
    path = ROOT/'rooms'/f'{name}.md'
    parts.append((path, path.read_text().split(heading, 1)[1].split(end, 1)[0]))
for path, text in parts:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            dest = (path.parent/target.split('#')[0]).resolve()
            assert dest.is_relative_to(ROOT)
            if dest != HERE/'verification.json':
                assert dest.is_file(), dest
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
        assert any((ROOT/place/(target+'.md')).is_file() for place in ('words', 'rooms', '')), target
chronicle = (ROOT/'chronicle.md').read_bytes()
assert sha(chronicle[:before['chronicle_bytes']]) == before['tracked_sha256']['chronicle.md']
added = chronicle[before['chronicle_bytes']:].decode()
if PRE:
    assert added == ''
else:
    assert len(added.splitlines()) == 1
    assert re.fullmatch(r'- 2026-10-16 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', added)
result = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'passed': True,
          'mode': 'pre-close' if PRE else 'final', 'independent_reviewer': False,
          'service_requests': len(records), 'curl_exit_zero': sum(r['curl_exit'] == 0 for r in records),
          'http_status_counts': dict(Counter(r['curl_metrics']['http_code'] for r in records)),
          'parsed_advertisements_agree': True, 'earlier_saved_bodies_byte_equal': True,
          'observation_window_seconds': window, 'guix_unobserved_gap_seconds': gap,
          'question_lines_changed': changed, 'questions_open': len(open_lines),
          'filed': 0, 'researched': 3, 'settled': 0, 'planted': 0,
          'rooms': len(rooms), 'map_lines': len(entries), 'garden_unchanged': True,
          'new_markdown_links_resolve': True, 'chronicle_lines_added': len(added.splitlines())}
filename = 'pre-close-verification.json' if PRE else 'verification.json'
(HERE/filename).write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
