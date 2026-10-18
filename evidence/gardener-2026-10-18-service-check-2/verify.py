"""Offline self-check of this bounded gardener visit; no network or machinery edits."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
import hashlib
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FINAL = '--final' in sys.argv


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    assert path.resolve().is_relative_to(ROOT)
    return json.loads(path.read_text())


before = load(HERE / 'before.json')
manifest = load(HERE / 'manifest.json')
comparison = load(HERE / 'comparison.json')
rows = manifest['records']
parse = runpy.run_path(str(ROOT / before['parser_path']))['parse']
assert sha((ROOT / before['parser_path']).read_bytes()) == before['parser_sha256']
collector = load(HERE / 'collector-source.json')
assert sha((ROOT / collector['path']).read_bytes()) == collector['sha256']
assert len(rows) == manifest['planned_maximum_requests'] == 6
assert manifest['stop_reason'] is None
assert [r['id'] for r in rows] == [f'r{i}-{n}' for i in (1, 2) for n in ('orgmode', 'emacs', 'guix')]
receipt = (HERE / 'README.md').read_text()
initial_plan = receipt.split('\n## What arrived\n', 1)[0].rstrip() + '\n'
assert sha(initial_plan.encode()) == before['plan_sha256']
waits = {}
previous_finish = None
for rec, comp in zip(rows, comparison['comparisons']):
    rid = rec['id']
    assert rec == load(HERE / (rid + '.json')) and comp['id'] == rid
    body = (HERE / (rid + '.body')).read_bytes()
    headers = (HERE / (rid + '.headers')).read_bytes()
    met = rec['curl_metrics']
    assert rec['curl_exit'] == 0 and rec['body_present']
    assert sha(body) == rec['body_sha256'] and len(body) == rec['body_bytes']
    assert int(met['size_download']) == len(body)
    assert met['ssl_verify_result'] == '0' and met['num_redirects'] == '0'
    assert met['url_effective'] == rec['url']
    assert rec['command'][1] == '--disable'
    for flag, value in [('--retry', '0'), ('--max-time', '45'), ('--connect-timeout', '10'), ('--max-filesize', '1048576')]:
        assert rec['command'][rec['command'].index(flag) + 1] == value
    assert not {'--location', '-L', '--insecure', '-k', '--data', '--request', '--cookie'} & set(rec['command'])
    start, finish = (datetime.fromisoformat(rec[k]) for k in ('start_utc', 'finish_utc'))
    assert start < finish and (previous_finish is None or previous_finish <= start)
    assert abs((finish-start).total_seconds() - rec['process_elapsed_monotonic_seconds']) < 0.1
    previous_finish = finish
    old = load(ROOT / comp['previous_complete_capture'])
    old_body = (ROOT / comp['previous_complete_capture']).with_suffix('.body').read_bytes()
    assert old['url'] == rec['url'] and old['curl_exit'] == 0
    assert sha(old_body) == old['body_sha256']
    assert comp['body_equal_to_previous'] is True and body == old_body
    assert comp['parse_problem'] is None
    if rid.endswith('orgmode'):
        assert met['http_code'] == '200' and b'200 OK' in headers
        assert comp['parsed'] == parse(body) == parse(old_body)
        assert set(comp['parsed']['references'].values()) == {'fffa58637c7f24f10d33437a6ef7acd1dd2498df'}
    else:
        assert met['http_code'] == '500' and b'500 Internal Server Error' in headers
        assert body == b'Internal Server Error'
    table_row = f"| {rid} | {start.strftime('%H:%M:%S.%f')} | {finish.strftime('%H:%M:%S.%f')} | {met['http_code']} | {len(body)} | {met['time_total']} |"
    assert table_row in receipt
    waits[rid] = str(Decimal(met['time_starttransfer']) - Decimal(met['time_pretransfer']))
window = (datetime.fromisoformat(rows[-1]['finish_utc']) - datetime.fromisoformat(rows[0]['start_utc'])).total_seconds()
assert window == comparison['observation_window_seconds'] == 54.074505
assert waits['r2-orgmode'] == '18.668885'
old_rows = load(ROOT / 'evidence/gardener-2026-10-18-service-check/manifest.json')['records']
first = datetime.fromisoformat(rows[0]['start_utc'])
assert (first-datetime.fromisoformat(old_rows[-1]['finish_utc'])).total_seconds() == comparison['previous_attempt_finish_to_start_seconds'] == 11403.859139
assert (first-datetime.fromisoformat(old_rows[3]['finish_utc'])).total_seconds() == comparison['previous_complete_orgmode_finish_to_start_seconds'] == 11448.173587
sources = load(HERE / 'sources.json')
assert len(sources) == 3
for src in sources:
    data = (HERE / src['file']).read_bytes()
    assert src['curl_exit'] == 0 and src['http_status'] == '200'
    assert len(data) == src['bytes'] and sha(data) == src['sha256']
    assert src['url'] in receipt
    assert datetime.fromisoformat(src['start_utc']) > datetime.fromisoformat(rows[-1]['finish_utc'])
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text)
assert set(entries) == rooms and all(v == 1 for v in Counter(entries).values())
for line in map_text.splitlines():
    if '](rooms/' in line:
        assert line.startswith('- ') and len(re.findall(r'\]\(rooms/', line)) == 1
for name in ('rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'):
    text = (ROOT / name).read_text()
    parts = text.splitlines()
    assert parts[0] == '# ' + Path(name).stem and parts[2].startswith('*') and parts[2].endswith('*')
    assert parts[4] and not parts[4].startswith(('#', '*'))
    assert '2026-10-18, 01:36–01:37 UTC' in text and 'uncertain:' in text
word = (ROOT / 'words/response-time.md').read_text()
assert word.startswith('# response-time\n\nResponse time is') and word.rstrip().splitlines()[-1].startswith('Links: ')
for rel in ('courtyard.md', 'questions.md', 'quests.md'):
    assert sha((ROOT / rel).read_bytes()) == before['content_hashes'][rel]
questions = (ROOT / 'questions.md').read_text().splitlines()
opened = [(i, line) for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
eligible = [i for i, line in opened if not re.search(r'commission|waits for: yu|yu decides|needs yu|being grown', line, re.I)]
assert len(opened) == 16 and eligible == [740, 744, 766]
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())
garden = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()}
assert garden == before['garden_hashes']
changed = {name for name, digest in before['content_hashes'].items() if sha((ROOT/name).read_bytes()) != digest}
expected = {'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md', 'words/response-time.md', 'gate.md'}
chronicle = (ROOT / 'chronicle.md').read_bytes()
assert sha(chronicle[:before['chronicle_bytes']]) == before['content_hashes']['chronicle.md']
addition = chronicle[before['chronicle_bytes']:].decode()
if FINAL:
    expected.add('chronicle.md')
    assert len(addition.splitlines()) == 1
    assert re.fullmatch(r'- 2026-10-18 \d\d:\d\d · visit: filed 0, researched 3, planted 0 — [^\n]+\n', addition)
else:
    assert not addition
assert changed == expected, sorted(changed)
for directory in ('rooms', 'words'):
    assert {str(p.relative_to(ROOT)) for p in (ROOT/directory).glob('*.md')} == {n for n in before['content_hashes'] if n.startswith(directory+'/')}
result = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'mode': 'final' if FINAL else 'pre-close',
          'self_check_only': True, 'requests': len(rows), 'source_fetches': len(sources),
          'all_bodies_equal_to_previous_complete_same_path': True, 'observation_window_seconds': window,
          'ready_to_first_byte_seconds': waits, 'map_rooms': len(rooms), 'map_entries': len(entries),
          'open_questions': len(opened), 'eligible_researched': eligible, 'answered': 0, 'planted': 0,
          'garden_unchanged': True, 'changed_prose_files': sorted(changed), 'chronicle_append': addition,
          'checks_passed': True}
name = 'verification.json' if FINAL else 'pre-close-verification.json'
with (HERE / name).open('x') as f:
    json.dump(result, f, indent=2)
    f.write('\n')
print(json.dumps(result, indent=2))
