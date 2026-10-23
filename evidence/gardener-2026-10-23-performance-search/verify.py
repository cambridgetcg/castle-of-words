"""Check the gardener's local changes, not the watched service's behavior."""
from collections import Counter
from datetime import datetime
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')
assert sys.argv[1:] in ([], ['--preclose'])
preclose = sys.argv[1:] == ['--preclose']
before = json.loads((HERE / 'before.json').read_text())
preflight = json.loads((HERE / 'preflight.json').read_text())
paths = list(ROOT.glob('*.md'))
for folder in ('rooms', 'words', 'garden'):
    paths.extend(p for p in (ROOT / folder).rglob('*') if p.is_file())
after = {}
for path in paths:
    assert path.resolve().is_relative_to(ROOT)
    raw = path.read_bytes()
    after[str(path.relative_to(ROOT))] = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
assert set(before) - set(after) == set()
assert set(after) - set(before) == {'words/benchmark.md'}
changed = sorted(k for k in before if before[k] != after[k])
expected = ['gate.md', 'questions.md', 'rooms/what-the-gaps-can-say.md']
if not preclose:
    expected.append('chronicle.md')
assert changed == sorted(expected), changed

def same_as_before(name, text):
    assert sha256(text.encode()).hexdigest() == before[name]['sha256'], name

questions = (ROOT / 'questions.md').read_text()
notes = re.findall(r'\(researched 2026-10-23; still open — \[\[what-the-gaps-can-say\]\], “A test using the archive is not a test of its service,”[^\n)]*\) ', questions)
assert len(notes) == 1
same_as_before('questions.md', questions.replace(notes[0], '', 1))
assert sum(s.startswith('- [ ]') for s in questions.splitlines()) == 16
assert questions.splitlines()[739].startswith('- [ ]')
assert preflight['eligible_oldest_first'] == [740, 744, 766]
assert preflight['courtyard_items'] == 0 and preflight['open_questions'] == 16

room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
heading = '## A test using the archive is not a test of its service — 2026-10-23\n'
assert room.count(heading) == 1
start = room.index(heading)
end = room.index('## Sources\n', start)
section = room[start:end]
same_as_before('rooms/what-the-gaps-can-say.md', room[:start] + room[end:])
assert room.startswith('# what-the-gaps-can-say\n\n*')
assert 'uncertain:' in section and '**740 remains open.**' in section

old_glance = '> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-22 (all 697 rooms listed once in the Map; [job traces and reference-update records](evidence/gardener-2026-10-22-update-records/README.md) gained separate meanings without becoming observations of the mirror; one question researched and still open, none planted, no watched Git requests or new timing samples)'
old_map = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — saved replies leave unseen gaps; job traces, reference updates and client waits record different events, not a proved shared cause (updated 2026-10-22)'
gate = (ROOT / 'gate.md').read_text()
gate_lines = gate.splitlines(keepends=True)
assert gate_lines[34].startswith('> rooms: **697**') and 'checked 2026-10-23' in gate_lines[34]
gate_lines[34] = old_glance + '\n'
map_indices = [i for i,s in enumerate(gate_lines) if s.startswith('- [what-the-gaps-can-say](rooms/')]
assert len(map_indices) == 1
gate_lines[map_indices[0]] = old_map + '\n'
same_as_before('gate.md', ''.join(gate_lines))
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert Counter(entries) == Counter({name: 1 for name in rooms})
assert len(rooms) == 697

word = (ROOT / 'words/benchmark.md').read_text()
assert word.startswith('# benchmark\n\nA benchmark is a test')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
assert 'uncertain:' in word
wiki_targets = sorted(set(re.findall(r'\[\[([^]|#]+)', word + section)))
for target in wiki_targets:
    assert any((ROOT / folder / (target + '.md')).is_file() for folder in ('words', 'rooms', '')), target
assert (HERE / 'README.md').is_file()

labels = ['performance-search', 'slow-update-search', 'archive-performance-search',
          'archive-link-report', 'archive-link-reply', 'archive-link-revision']
retrievals = []
for label in labels:
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    raw = (HERE / (label + '.html')).read_bytes()
    assert receipt['bytes'] == len(raw)
    assert receipt['sha256'] == sha256(raw).hexdigest()
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    assert datetime.fromisoformat(receipt['started_utc']).astimezone().date().isoformat() == '2026-10-23'
    retrievals.append({'label': label, 'http_status': 200, 'curl_exit': 0})
assert 'Showing results for yeti performance' in (HERE / 'performance-search-text.txt').read_text()
report_text = (HERE / 'archive-link-report-text.txt').read_text()
assert 'unscientific timings' in report_text and 'multipart_text_as_html' in report_text
revision_text = (HERE / 'archive-link-revision-text.txt').read_text()
assert 'busy server' in revision_text and '6078 messages on a local mirror' in revision_text

chronicle = (ROOT / 'chronicle.md').read_bytes()
old_size = before['chronicle.md']['bytes']
assert sha256(chronicle[:old_size]).hexdigest() == before['chronicle.md']['sha256']
added = chronicle[old_size:].decode()
if preclose:
    assert not added
else:
    assert re.fullmatch(
        r'- 2026-10-23 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — '
        r'A historical rendering test used the archive as data without measuring its live Git service or explaining later delays\.\n', added), repr(added)

result = {
    'passed': True, 'phase': 'preclose' if preclose else 'closed',
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'new_words': ['benchmark'], 'new_rooms': 0,
    'changed_existing_grounds_files': changed,
    'chronicle_lines_appended': len(added.splitlines()),
    'map_rooms_exactly_once': len(rooms), 'open_questions': 16,
    'reserved_questions_unchanged': True, 'garden_unchanged': True,
    'new_wiki_targets_exist': wiki_targets, 'retrievals': retrievals,
    'scope': 'Local consistency; historical tests were read, not rerun, and no service measurements were made.'
}
output = 'preclose-verification.json' if preclose else 'verification.json'
(HERE / output).write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
