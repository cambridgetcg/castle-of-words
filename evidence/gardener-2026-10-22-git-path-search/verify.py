"""Check this visit against its own saved baseline, without changing the castle."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
preclose = '--preclose' in sys.argv
before = json.loads((HERE / 'before.json').read_text())
preflight = json.loads((HERE / 'preflight.json').read_text())
changed = []
for relative, record in before.items():
    path = ROOT / relative
    assert path.resolve().is_relative_to(ROOT), relative
    assert path.is_file(), relative
    if sha256(path.read_bytes()).hexdigest() != record['sha256']:
        changed.append(relative)
expected = {'rooms/what-the-gaps-can-say.md', 'words/deployment-claim.md', 'gate.md'}
if not preclose:
    expected.add('chronicle.md')
assert set(changed) == expected, changed
current_garden = {str(p.relative_to(ROOT)) for p in (ROOT / 'garden').rglob('*') if p.is_file()}
original_garden = {s for s in before if s.startswith('garden/')}
assert current_garden == original_garden
assert all(not s.startswith('garden/') for s in changed)
current_prose = {str(p.relative_to(ROOT)) for p in ROOT.glob('*.md')}
current_prose |= {str(p.relative_to(ROOT)) for directory in ('rooms', 'words') for p in (ROOT / directory).glob('*.md')}
assert current_prose == {s for s in before if not s.startswith('garden/')}
questions = (ROOT / 'questions.md').read_text()
assert sum(s.startswith('- [ ]') for s in questions.splitlines()) == 16
assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())
gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms
assert all(n == 1 for n in Counter(entries).values())
assert len(entries) == 697
room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
paragraphs = room.split('\n\n')
assert paragraphs[0] == '# what-the-gaps-can-say'
assert paragraphs[1].startswith('*') and paragraphs[1].endswith('*')
assert room.count('## A quoted deployment keeps its own host — 2026-10-22') == 1
section = room.split('## A quoted deployment keeps its own host — 2026-10-22\n', 1)[1].split('\n## Sources', 1)[0]
word = (ROOT / 'words/deployment-claim.md').read_text()
assert word.startswith('# deployment-claim\n\nA deployment claim says')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
for link in re.findall(r'\[\[([^\]|#]+)', section + word):
    assert any((ROOT / folder / (link + '.md')).is_file() for folder in ('words', 'rooms', '')), link
assert (HERE / 'README.md').is_file()
source_receipts = sorted(HERE.glob('*-receipt.json'))
assert len(source_receipts) == 5
source_results = []
for path in source_receipts:
    receipt = json.loads(path.read_text())
    label = path.name.removesuffix('-receipt.json')
    raw = (HERE / (label + '.html')).read_bytes()
    assert receipt['sha256'] == sha256(raw).hexdigest(), label
    assert receipt['bytes'] == len(raw), label
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200, label
    assert 'info/refs' not in receipt['url'], label
    for suffix in ('-text.txt', '-links.json'):
        assert (HERE / (label + suffix)).is_file(), label
    source_results.append({'label': label, 'status': 200, 'bytes': len(raw), 'hash_verified': True})
reply = (HERE / 'operator-proxy-text.txt').read_text()
original = (HERE / 'proxy-patch-text.txt').read_text()
assert 'Eric Wong writes:' in reply and '> This PSGI reverse proxy' in reply
assert 'https://public-inbox.org' in original and 'https://yhbt.net/lore/' in original
assert 'From: Eric Wong' in original and 'Date: Sun, 13 Jul 2025' in original
assert 'yhetil.org' not in original
chronicle = (ROOT / 'chronicle.md').read_bytes()
original_length = before['chronicle.md']['bytes']
assert sha256(chronicle[:original_length]).hexdigest() == before['chronicle.md']['sha256']
added = chronicle[original_length:].decode()
if preclose:
    assert not added
else:
    assert len(chronicle.splitlines()) == preflight['chronicle_lines'] + 1
    assert re.fullmatch(r'- 2026-10-22 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — A quoted deployment report kept its original speaker and named hosts instead of becoming evidence about another site\.\n', added), repr(added)
result = {
    'mode': 'preclose' if preclose else 'final',
    'changed_castle_prose': sorted(changed),
    'courtyard_items': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'open_questions': 16, 'open_quests': 8,
    'rooms': len(rooms), 'map_entries': len(entries), 'map_exact_once': True,
    'garden_files_unchanged': len(original_garden),
    'question_quest_courtyard_bytes_unchanged': True,
    'new_or_deleted_root_room_word_files': 0,
    'source_retrievals': source_results,
    'chronicle_original_prefix_preserved': True,
    'chronicle_added_lines': len(added.splitlines()),
    'checks': 'passed',
}
output = HERE / ('preclose-verification.json' if preclose else 'verification.json')
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
