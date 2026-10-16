"""Offline verification; no network calls and no imports from the collector."""
from collections import Counter
from datetime import datetime
from decimal import Decimal
from pathlib import Path
import hashlib
import io
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
OLD = [ROOT / 'evidence/gardener-2026-10-16-service-check',
       ROOT / 'evidence/gardener-2026-10-16-service-check-2']
sha = lambda data: hashlib.sha256(data).hexdigest()
before = json.loads((HERE / 'before.json').read_text())
comparison = json.loads((HERE / 'comparison.json').read_text())
current = json.loads((HERE / 'manifest.json').read_text())
assert len(current['records']) == 6 and current['stopped_reason'] is None
assert current['new_watch_started'] is False and current['retries'] == 0
assert current['redirects_followed'] is False


def normalized_command(command):
    result = list(command)
    for option in ('--output', '--dump-header'):
        result[result.index(option) + 1] = '<capture-path>'
    return result


profiles, body_count, advertisements, errors = {}, 0, [], []
for directory in [*OLD, HERE]:
    manifest = json.loads((directory / 'manifest.json').read_text())
    assert manifest['curl_version'] == current['curl_version']
    for record in manifest['records']:
        rid = record['id']
        body = (directory / f'{rid}.body').read_bytes()
        assert len(body) == record['body_bytes'] == int(record['curl_metrics']['size_download'])
        assert sha(body) == record['body_sha256']
        assert record['curl_exit'] == 0 and record['stderr'] == ''
        metrics = record['curl_metrics']
        assert metrics['http_version'] == '1.1' and metrics['num_redirects'] == '0'
        assert metrics['proxy_used'] == '0' and metrics['ssl_verify_result'] == '0'
        headers = (directory / f'{rid}.headers').read_bytes()
        assert headers.startswith(b'HTTP/1.1 ' + metrics['http_code'].encode())
        assert datetime.fromisoformat(record['finish_utc']) > datetime.fromisoformat(record['start_utc'])
        assert record['process_elapsed_monotonic_seconds'] > 0
        profile = (record['method'], record['url'], record['request_headers'], normalized_command(record['command']))
        if rid in profiles:
            assert profiles[rid] == profile
        else:
            profiles[rid] = profile
        body_count += 1
        if rid.endswith('orgmode'):
            assert metrics['http_code'] == '200'
            assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
            advertisements.append(body)
        else:
            assert metrics['http_code'] == '500'
            errors.append(body)
assert body_count == 18 and len(advertisements) == 6 and len(errors) == 12
assert all(body == advertisements[0] for body in advertisements)
assert all(body == b'Internal Server Error' for body in errors)

# Decode the retained packet stream independently with a file-like reader.
for body in advertisements:
    stream = io.BytesIO(body)
    packets = []
    while stream.tell() < len(body):
        prefix = stream.read(4)
        assert re.fullmatch(b'[0-9a-f]{4}', prefix)
        length = int(prefix, 16)
        if length == 0:
            packets.append(None)
        else:
            assert 4 <= length <= 65520
            payload = stream.read(length - 4)
            assert len(payload) == length - 4
            packets.append(payload)
    assert len(packets) == 5
    assert packets[0] == b'# service=git-upload-pack\n'
    assert packets[1] is None and packets[-1] is None
    first, caps = packets[2].rstrip(b'\n').split(b'\x00')
    oid = b'ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb'
    assert first == oid + b' HEAD'
    assert packets[3].rstrip(b'\n') == oid + b' refs/heads/master'
    assert b'symref=HEAD:refs/heads/master' in caps.split()
    assert b'object-format=sha1' in caps.split()
assert all(pair['body_byte_equal'] and pair['references_equal'] and pair['capabilities_equal']
           and pair['same_method_url_headers'] for pair in comparison['pairs'])

records = current['records']
assert [r['id'] for r in records] == [f'r{n}-{name}' for n in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
times = [Decimal(r['curl_metrics']['time_total']) for r in records]
assert min(times) == Decimal('0.322129') and max(times) == Decimal('0.437191')
assert records[0]['curl_metrics']['time_namelookup'] == '0.020607'
assert Decimal(records[0]['curl_metrics']['time_total']) - Decimal(records[0]['curl_metrics']['time_namelookup']) == Decimal('0.384235')
window = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
assert window == comparison['observation_window_seconds'] == 2.510732
old_record = json.loads((OLD[-1] / 'r2-orgmode.json').read_text())
gap = (datetime.fromisoformat(records[0]['start_utc']) - datetime.fromisoformat(old_record['finish_utc'])).total_seconds()
assert gap == 11841.503232
assert (datetime.fromisoformat(records[0]['start_utc']) - datetime.fromisoformat(old_record['start_utc'])).total_seconds() == 11841.900121

questions_text = (ROOT / 'questions.md').read_text()
questions = questions_text.splitlines()
open_lines = {str(i): line for i, line in enumerate(questions, 1) if line.startswith('- [ ]')}
assert len(open_lines) == 16 and set(open_lines) == set(before['open_question_line_hashes'])
changed = [int(i) for i, line in open_lines.items() if sha(line.encode()) != before['open_question_line_hashes'][i]]
assert changed == [740, 744, 766]
reconstructed = questions[:]
for i in changed:
    line = questions[i-1]
    left = line.index('(observed 2026-10-16 13:50 UTC; still open —')
    right = line.index('(observed 2026-10-16 10:32 UTC; still open —')
    original = line[:left] + line[right:]
    assert sha(original.encode()) == before['open_question_line_hashes'][str(i)]
    reconstructed[i-1] = original
assert sha(('\n'.join(reconstructed) + '\n').encode()) == before['tracked_sha256']['questions.md']
for name in ('courtyard.md', 'quests.md'):
    assert sha((ROOT / name).read_bytes()) == before['tracked_sha256'][name]
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())

rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
map_section = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[([^]]+)\]\(rooms/([^/)]+)\.md\) — (.+)$', map_section, re.M)
assert len(entries) == len(rooms) == 697
assert {entry[1] for entry in entries} == rooms
assert all(n == 1 for n in Counter(entry[1] for entry in entries).values())
assert all(label == target for label, target, _ in entries)

for name in ('dns-cache', 'name-lookup-time'):
    text = (ROOT / 'words' / f'{name}.md').read_text()
    lines = text.strip().splitlines()
    assert lines[0] == f'# {name}' and lines[2] and not lines[2].startswith('#')
    assert lines[-1].startswith('Links: ')
for name in ('what-the-gaps-can-say', 'measuring-the-window'):
    lines = (ROOT / 'rooms' / f'{name}.md').read_text().splitlines()
    assert lines[0] == f'# {name}'
    assert lines[2].startswith('*') and lines[2].endswith('*') and lines[4]

# Check new word and receipt links, including precise local Markdown paths.
for path in (ROOT / 'words/dns-cache.md', ROOT / 'words/name-lookup-time.md', HERE / 'README.md'):
    text = path.read_text()
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            resolved = (path.parent / target.split('#')[0]).resolve()
            assert resolved.is_relative_to(ROOT)
            assert resolved.exists() or resolved == HERE / 'verification.json', (path, target)
    for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]+)?\]\]', text):
        assert any((ROOT / folder / f'{target}.md').exists() for folder in ('rooms', 'words')), target
for line in (HERE / 'README.md').read_text().splitlines():
    if line.startswith('|'):
        assert len(line.strip('|').split('|')) == 7, line

# Retain actual source-file hashes; 404 bodies are not accepted documents.
source_hashes = {}
for name in ('dns-cache-timeout-8.7.1.md', 'curl-share-8.7.1.md',
             'libcurl-tutorial-8.7.1.md', 'rfc1034.txt', 'search-brave.html'):
    data = (HERE / name).read_bytes()
    assert len(data) > 1000 and data != b'404: Not Found'
    source_hashes[name] = sha(data)
for name in ('dns-cache-timeout-8.7.1.3', 'curl-share-8.7.1.3'):
    assert (HERE / name).read_bytes() == b'404: Not Found'

garden = {str(p.relative_to(ROOT)): sha(p.read_bytes())
          for p in sorted((ROOT / 'garden').rglob('*')) if p.is_file() and not p.is_symlink()}
assert garden == before['garden_sha256'], 'garden changed since collection began'
chronicle = (ROOT / 'chronicle.md').read_bytes()
assert sha(chronicle[:before['chronicle_bytes']]) == before['chronicle_sha256']
addition = chronicle[before['chronicle_bytes']:].decode()
closed = '--closed' in sys.argv
if closed:
    assert re.fullmatch(r'- 2026-10-16 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', addition)
else:
    assert addition == '', 'chronicle changed before the final line'
report = {'status': 'PASS', 'closed': closed, 'new_service_requests': 6,
          'saved_bodies_checked': body_count, 'identical_orgmode_captures': len(advertisements),
          'same_explicit_request_profiles': True, 'observation_window_seconds': window,
          'gap_between_orgmode_processes_seconds': gap, 'questions_updated': changed,
          'open_questions': 16, 'filed': 0, 'researched': 3, 'answered': 0, 'planted': 0,
          'word_files_created': ['words/dns-cache.md'],
          'rooms': len(rooms), 'map_entries': len(entries), 'garden_unchanged': True,
          'courtyard_unchanged': True, 'quests_unchanged': True,
          'prior_chronicle_preserved': True, 'chronicle_lines_appended': len(addition.splitlines()),
          'source_file_sha256': source_hashes}
(HERE / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
