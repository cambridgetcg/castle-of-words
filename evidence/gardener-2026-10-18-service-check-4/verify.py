"""Offline self-check; never sends a request or edits the castle's prose."""
from collections import Counter
from datetime import datetime
from pathlib import Path
import hashlib
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.loads((HERE / name).read_text())


def dt(value):
    return datetime.fromisoformat(value)


def check_links(text, base):
    for match in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
        name = match.group(1)
        assert any((ROOT / d / (name + '.md')).is_file() for d in ('rooms', 'words', '')), name
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^()]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            path = (base / target.split('#', 1)[0]).resolve()
            assert path.is_relative_to(ROOT) and path.is_file(), target


before = load('before.json')
manifest = load('manifest.json')
comparison = load('comparison.json')
source_record = load('collector-source.json')
for path_key, hash_key, record in (
    ('path', 'sha256', source_record),
    ('parser_path', 'parser_sha256', before),
):
    assert sha((ROOT / record[path_key]).read_bytes()) == record[hash_key]
parse = runpy.run_path(str(ROOT / before['parser_path']))['parse']
previous_dir = ROOT / source_record['baseline']
previous_records = json.loads((previous_dir / 'manifest.json').read_text())['records']
records = manifest['records']
assert len(records) == manifest['planned_maximum_requests'] == 6
assert manifest['stop_reason'] is None
readme = (HERE / 'README.md').read_text()
previous_finish = None
assert len(records) == len(comparison['comparisons'])
for rec, comp in zip(records, comparison['comparisons']):
    rid = rec['id']
    metrics = rec['curl_metrics']
    body = (HERE / (rid + '.body')).read_bytes()
    assert sha(body) == rec['body_sha256'] and len(body) == rec['body_bytes']
    assert rec['curl_exit'] == 0 and rec['stderr'] == ''
    assert metrics['num_redirects'] == '0' and metrics['ssl_verify_result'] == '0'
    assert 0 < float(metrics['time_total']) < 1
    assert dt(rec['start_utc']) <= dt(rec['finish_utc'])
    assert rec['process_elapsed_monotonic_seconds'] >= float(metrics['time_total'])
    if previous_finish is not None:
        assert previous_finish <= dt(rec['start_utc'])
    previous_finish = dt(rec['finish_utc'])
    assert rec['command'][0:2] == ['curl', '--disable']
    for flag, value in (('--retry', '0'), ('--connect-timeout', '10'),
                        ('--max-time', '45'), ('--max-filesize', '1048576')):
        assert rec['command'][rec['command'].index(flag) + 1] == value
    assert not {'--location', '--insecure', '--user', '--cookie'} & set(rec['command'])
    assert rid == comp['id']
    prior_capture = ROOT / comp['previous_complete_capture']
    prior_rec = json.loads(prior_capture.read_text())
    prior_body = prior_capture.with_suffix('.body').read_bytes()
    assert sha(prior_body) == prior_rec['body_sha256']
    assert comp['body_equal_to_previous'] == (body == prior_body)
    if rid.endswith('orgmode'):
        assert metrics['http_code'] == '200' and len(body) == 370
        assert parse(body) == comp['parsed'] and comp['parse_problem'] is None
    else:
        assert metrics['http_code'] == '500' and body == b'Internal Server Error'
    row = '| ' + ' | '.join((rid, dt(rec['start_utc']).strftime('%H:%M:%S.%f'),
        dt(rec['finish_utc']).strftime('%H:%M:%S.%f'), metrics['http_code'],
        str(len(body)), metrics['time_total'])) + ' |'
    assert row in readme, row

old = (previous_dir / 'r2-orgmode.body').read_bytes()
new = (HERE / 'r1-orgmode.body').read_bytes()
old_view, new_view = parse(old), parse(new)
old_id, new_id = old_view['references']['HEAD'], new_view['references']['HEAD']
assert old_id != new_id
assert old_view['references'].keys() == new_view['references'].keys()
assert old_view['capabilities'] == new_view['capabilities']
assert old.count(old_id.encode()) == 2
assert old.replace(old_id.encode(), new_id.encode()) == new
assert new == (HERE / 'r2-orgmode.body').read_bytes()
assert old_id in readme and new_id in readme and sha(new) in readme
expected_spans = {
    'observation_window_seconds': (dt(records[-1]['finish_utc']) - dt(records[0]['start_utc'])).total_seconds(),
    'previous_attempt_finish_to_start_seconds': (dt(records[0]['start_utc']) - dt(previous_records[-1]['finish_utc'])).total_seconds(),
    'previous_complete_orgmode_finish_to_start_seconds': (dt(records[0]['start_utc']) - dt(previous_records[3]['finish_utc'])).total_seconds(),
}
for key, value in expected_spans.items():
    assert comparison[key] == value
    assert f'{value:,.6f}' in readme

sources = load('sources.json')
assert sha((ROOT / sources['helper_path']).read_bytes()) == sources['helper_sha256']
for source in sources['sources']:
    data = (HERE / source['file']).read_bytes()
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert len(data) == source['bytes'] and sha(data) == source['sha256']
    assert source['url'] in readme

added_sections = {
    'rooms/what-the-gaps-can-say.md': ('## A changed address across an unwatched gap — 2026-10-18, 07:58 UTC\n', '## Sources\n'),
    'rooms/measuring-the-window.md': ("## The view changed; the fault's boundaries did not appear — 2026-10-18, 07:58 UTC\n", 'Links:\n'),
    'words/reference-advertisement.md': ('## Another measured comparison — 2026-10-18\n', 'Links: '),
}
for rel, (start, end) in added_sections.items():
    path = ROOT / rel
    text = path.read_text()
    assert text.startswith('# ' + path.stem + '\n')
    a, rest = text.split(start)
    added, b = rest.split(end, 1)
    assert sha((a + end + b).encode()) == before['content_hashes'][rel], rel
    check_links(start + added, path.parent)
    if rel.startswith('rooms/'):
        assert text.splitlines()[2].startswith('*') and text.splitlines()[2].endswith('*')
    else:
        assert text.rstrip().splitlines()[-1].startswith('Links: ')
    assert '2026-10-18' in added and 'uncertain:' in added

allowed = set(added_sections) | {'gate.md', 'chronicle.md'}
for rel, expected in before['content_hashes'].items():
    if rel not in allowed:
        assert sha((ROOT / rel).read_bytes()) == expected, rel
current_prose = {str(p.relative_to(ROOT)) for d in ('rooms', 'words') for p in (ROOT / d).glob('*.md')}
initial_prose = {p for p in before['content_hashes'] if p.startswith(('rooms/', 'words/'))}
assert current_prose == initial_prose

gate = (ROOT / 'gate.md').read_text()
new_map_line = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — changed or matching Git lists show the views received, not the hidden update history; quick replies do not fill the gaps between checks (updated 2026-10-18)'
old_map_line = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — matching or changed replies show the views received, not the hidden update history; separate waits do not establish a shared cause (updated 2026-10-18)'
assert gate.count(new_map_line) == 1
assert sha(gate.replace(new_map_line, old_map_line).encode()) == before['content_hashes']['gate.md']
map_section = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^()]+\.md)\)', map_section, re.M)
rooms = {p.name for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and all(v == 1 for v in Counter(entries).values())

garden = {str(p.relative_to(ROOT)): sha(p.read_bytes())
          for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()}
assert garden == before['garden_hashes']
questions = (ROOT / 'questions.md').read_text().splitlines()
open_lines = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
assert len(open_lines) == 16
assert all(questions[n-1].startswith('- [ ]') for n in (740, 744, 766))
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())
check_links(readme, HERE)

chronicle = (ROOT / 'chronicle.md').read_bytes()
prefix = chronicle[:before['chronicle_bytes']]
assert sha(prefix) == before['content_hashes']['chronicle.md']
suffix = chronicle[len(prefix):].decode()
if '--pre-close' in sys.argv:
    assert suffix == ''
else:
    assert re.fullmatch(r'- 2026-10-18 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', suffix)
    assert len(suffix.splitlines()) == 1

print(json.dumps({
    'result': 'PASS', 'phase': 'pre-close' if '--pre-close' in sys.argv else 'closed',
    'service_requests': len(records), 'source_reads': len(sources['sources']),
    'orgmode_view_changed': old_id != new_id, 'new_orgmode_captures_equal': True,
    'object_id_replacement_explains_all_changed_bytes': True,
    'all_six_operations_sub_second': True, 'error_responses': 4,
    'spans_seconds': expected_spans, 'map_rooms': len(rooms), 'map_entries': len(entries),
    'open_questions': len(open_lines), 'researched_questions_still_open': [740, 744, 766],
    'courtyard_questions_quests_unchanged': True, 'garden_unchanged': True,
    'changed_prose_files': sorted(allowed),
    'added_chronicle_lines': len(suffix.splitlines()),
    'limits': 'Offline local self-check, not independent review or evidence of a service cause.'
}, indent=2))
