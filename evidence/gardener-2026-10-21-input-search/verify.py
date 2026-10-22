"""Local consistency checks for this finite reading visit, not host verification."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
before = json.loads((HERE / 'before.json').read_text())
preclose = '--preclose' in sys.argv
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
assert {str(p.relative_to(ROOT)) for p in paths} == set(before)
changed = []
for path in paths:
    assert path.resolve().is_relative_to(ROOT)
    key = str(path.relative_to(ROOT))
    if sha256(path.read_bytes()).hexdigest() != before[key]['sha256']:
        changed.append(key)
expected = {'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/timestamp-provenance.md'}
if not preclose:
    expected.add('chronicle.md')
assert set(changed) == expected, changed

def original_matches(name, text):
    assert sha256(text.encode()).hexdigest() == before[name]['sha256'], name

room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
marker = '## The sorting date need not be the shown date — 2026-10-21\n'
assert room.count(marker) == 1
start = room.index(marker)
end = room.index('## Sources\n', start)
room_addition = room[start:end]
original_matches('rooms/what-the-gaps-can-say.md', room[:start] + room[end:])
assert room.startswith('# what-the-gaps-can-say\n\n*')
assert '**740 remains open.** uncertain:' in room_addition
assert 'not evidence that it was adopted' in room_addition
word = (ROOT / 'words/timestamp-provenance.md').read_text()
marker = 'The time used to order a list can differ from the time printed beside an item.'
assert word.count(marker) == 1
start = word.index(marker)
end = word.index('Links:', start)
word_addition = word[start:end]
original_matches('words/timestamp-provenance.md', word[:start] + word[end:])
assert word.startswith('# timestamp-provenance\n\nA time mark needs')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
readme = (HERE / 'README.md').read_text()
for target in set(re.findall(r'\[\[([^\]|#]+)', room_addition + word_addition + readme)):
    assert any((ROOT / part / (target + '.md')).is_file() for part in ('', 'rooms', 'words')), target
assert (ROOT / 'evidence/gardener-2026-10-21-input-search/README.md').is_file()

gate = (ROOT / 'gate.md').read_text()
old_summary = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [public configuration reading](evidence/gardener-2026-10-21-public-config-search/README.md) found a template for readers making another mirror, not the host's own update schedule; one question researched and still open, none planted, no watched Git requests or new timing samples)"
summaries = [line for line in gate.splitlines() if line.startswith('> rooms: ')]
assert len(summaries) == 1
assert '[historical date-reading](evidence/gardener-2026-10-21-input-search/README.md)' in summaries[0]
old_map = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — saved replies, hosting accounts, mirror templates and a historical bug fix do not by themselves reveal current update jobs or the cause of later slow Git replies (updated 2026-10-21)'
new_map = "- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — saved replies and historical hosting reports leave update times and causes unproved; a thread's displayed date can differ from its sorting date (updated 2026-10-21)"
assert gate.count(new_map) == 1
original_matches('gate.md', gate.replace(summaries[0], old_summary, 1).replace(new_map, old_map, 1))
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(rooms) == 697 and set(entries) == rooms
assert all(n == 1 for n in Counter(entries).values())
assert len(entries) == len(rooms)
assert sum(line.startswith('- [ ]') for line in (ROOT / 'questions.md').read_text().splitlines()) == 16
assert sum(line.startswith('- [ ]') for line in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())

helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
labels = ('web-poll', 'web-maildir', 'archive-poll', 'archive-input', 'future-date-report', 'received-patch', 'received-reply')
source_results = []
for label in labels:
    receipt = json.loads((HERE / f'{label}-receipt.json').read_text())
    raw = (HERE / f'{label}.html').read_bytes()
    assert len(raw) == receipt['bytes'] and sha256(raw).hexdigest() == receipt['sha256']
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    assert receipt['command'][receipt['command'].index('--retry') + 1] == '0'
    parser = helper['Text']()
    parser.feed(raw.decode('utf-8', errors='replace'))
    cleaned = '\n'.join(s.strip() for s in ''.join(parser.parts).splitlines() if s.strip()) + '\n'
    assert cleaned == (HERE / f'{label}-text.txt').read_text()
    assert list(dict.fromkeys(parser.links)) == json.loads((HERE / f'{label}-links.json').read_text())
    source_results.append({'label': label, 'status': 200, 'verified_bytes': len(raw), 'url': receipt['url']})
assert len(list(HERE.glob('*-receipt.json'))) == len(labels)
assert "I'm slightly against it." in (HERE / 'received-reply-text.txt').read_text()
assert 'base-commit: 0f19ca7e3ca6fc568a8713c5ececdb4d9fa577e6' in (HERE / 'received-patch-text.txt').read_text()
assert 'https://yhetil.org/orgmode/' in (HERE / 'future-date-report-text.txt').read_text()

chronicle = (ROOT / 'chronicle.md').read_bytes()
size = before['chronicle.md']['bytes']
assert sha256(chronicle[:size]).hexdigest() == before['chronicle.md']['sha256']
addition = chronicle[size:].decode()
if preclose:
    assert addition == ''
else:
    assert re.fullmatch(r"- 2026-10-21 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — A historical Org archive discussion separated the date used to order threads from the date shown beside them, without revealing the mirror's update schedule\.\n", addition), addition
report = {
    'verified_utc': datetime.now(timezone.utc).isoformat(),
    'mode': 'preclose' if preclose else 'final', 'checks_passed': True,
    'changed_existing_markdown': changed,
    'rooms': len(rooms), 'map_entries': len(entries), 'map_missing': [], 'map_extra': [], 'map_duplicates': [],
    'open_questions': 16, 'open_quests': 8,
    'new_rooms': 0, 'new_words': 0, 'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'source_count': len(source_results), 'source_results': source_results,
    'chronicle_addition': addition,
    'scope': 'Local consistency and source-byte integrity, not host deployment verification or search completeness.',
}
output = HERE / ('preclose-verification.json' if preclose else 'verification.json')
output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(report, indent=2, ensure_ascii=False))
