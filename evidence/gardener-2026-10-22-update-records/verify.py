"""Verify a bounded documentation visit against its pre-research state."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')
BEFORE = json.loads((HERE / 'before.json').read_text())
preclose = '--preclose' in sys.argv
expected = {'gate.md', 'rooms/what-the-gaps-can-say.md'}
if not preclose:
    expected.add('chronicle.md')
changed = set()
for rel, saved in BEFORE.items():
    path = ROOT / rel
    assert path.resolve().is_relative_to(ROOT)
    assert path.is_file(), f'Missing: {rel}'
    if sha256(path.read_bytes()).hexdigest() != saved['sha256']:
        changed.add(rel)
assert changed == expected, (changed, expected)

for folder in ('rooms', 'words', 'garden'):
    current = {str(p.relative_to(ROOT)) for p in (ROOT / folder).rglob('*') if p.is_file()}
    previous = {p for p in BEFORE if p.startswith(folder + '/')}
    additions = {'words/git-trace2.md'} if folder == 'words' else set()
    assert current == previous | additions, (folder, current ^ (previous | additions))

chronicle = (ROOT / 'chronicle.md').read_bytes()
saved = BEFORE['chronicle.md']
assert sha256(chronicle[:saved['bytes']]).hexdigest() == saved['sha256']
addition = chronicle[saved['bytes']:].decode()
if preclose:
    assert addition == ''
else:
    assert re.fullmatch(r'- 2026-10-22 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — Git’s optional work diary and reference-update hooks describe different events, not the mirror’s missing update history\.\n', addition)
    assert len(addition.splitlines()) == 1

questions = (ROOT / 'questions.md').read_text()
open_count = sum(line.startswith('- [ ]') for line in questions.splitlines())
assert open_count == 16
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())

gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and all(n == 1 for n in Counter(entries).values())
old_glance = '> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-22 (all 697 rooms listed once in the Map; a [quoted deployment report](evidence/gardener-2026-10-22-git-path-search/README.md) kept its original speaker and named hosts rather than becoming evidence about yhetil.org; one question researched and still open, none planted, no watched Git requests or new timing samples)'
old_map_line = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — saved replies leave unseen gaps; historical reports keep their named hosts and do not explain later Git delays (updated 2026-10-22)'
restored_lines = []
for line in gate.splitlines(keepends=True):
    if line.startswith('> rooms: **697**'):
        line = old_glance + '\n'
    elif line.startswith('- [what-the-gaps-can-say]'):
        line = old_map_line + '\n'
    restored_lines.append(line)
assert sha256(''.join(restored_lines).encode()).hexdigest() == BEFORE['gate.md']['sha256']

room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
header = '## A work diary and a changed bookmark are different records — 2026-10-22\n'
assert room.count(header) == 1
start = room.index(header)
end = room.index('## Sources\n\n1. Prometheus, **Alerting rules**', start)
section = room[start:end]
assert sha256((room[:start] + room[end:]).encode()).hexdigest() == BEFORE['rooms/what-the-gaps-can-say.md']['sha256']
assert '**740 remains open.** uncertain:' in section
assert 'HTTP 429' in section and 'v2.39.5' in section
assert room.startswith('# what-the-gaps-can-say\n\n*')
word = (ROOT / 'words/git-trace2.md').read_text()
assert word.startswith('# git-trace2\n\nGit Trace2 is a diary')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
assert 'fetched and read **2026-10-22**' in word
all_names = {p.stem for p in (ROOT / 'rooms').glob('*.md')} | {p.stem for p in (ROOT / 'words').glob('*.md')}
for link in re.findall(r'\[\[([^]|#]+)', word + section):
    assert link in all_names, link
assert (HERE / 'README.md').is_file()

statuses = {'schedule-search': 200, 'update-record-search': 200, 'trace-search': 429, 'trace2-doc': 200, 'hooks-doc': 200}
for label, status in statuses.items():
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    data = (HERE / (label + '.html')).read_bytes()
    assert len(data) == receipt['bytes']
    assert sha256(data).hexdigest() == receipt['sha256']
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == status
    assert 'info/refs' not in receipt['url']

# Check the specific documented exceptions used in the new prose.
hooks = (HERE / 'hooks-doc.html').read_text()
trace = (HERE / 'trace2-doc.html').read_text()
assert 'githooks - Hooks used by Git' in hooks
assert 'does not cover symbolic references' in hooks
assert 'The hook will not be called with\n"aborted" state in that case.' in hooks
assert 'where `<old-value>` is the old object name passed into the reference' in hooks
assert 'only present on the "start" and "atexit" events.' in trace
assert 'The child is assumed to be a long-running daemon process and may\noutlive the parent process.' in trace

result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'mode': 'preclose' if preclose else 'closed',
    'all_checks_passed': True,
    'changed_baseline_files': sorted(changed),
    'new_word_files': ['words/git-trace2.md'],
    'room_count': len(rooms), 'map_entries': len(entries), 'map_exact_once': True,
    'open_questions': open_count, 'courtyard_items': 0,
    'chronicle_added_lines': len(addition.splitlines()),
    'garden_unchanged': True, 'questions_and_quests_unchanged': True,
    'earlier_room_content_unchanged': True, 'gate_changes_limited_to_glance_and_one_map_line': True,
    'retrievals_verified': statuses,
}
(HERE / ('preclose-verification.json' if preclose else 'verification.json')).write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
