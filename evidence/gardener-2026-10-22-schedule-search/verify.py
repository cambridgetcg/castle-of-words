"""Local checks for this finite visit, not verification of the remote host."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import subprocess
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
PRE = '--preclose' in sys.argv
before = json.loads((HERE / 'before.json').read_text())

def digest(data):
    return sha256(data).hexdigest()

changed = []
for name, info in before.items():
    path = ROOT / name
    assert path.resolve().is_relative_to(ROOT)
    if digest(path.read_bytes()) != info['sha256']:
        changed.append(name)
expected = {'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/freshness-target.md'}
if not PRE:
    expected.add('chronicle.md')
assert set(changed) == expected, changed
assert {p.name for p in (ROOT / 'rooms').glob('*.md')} == {Path(p).name for p in before if p.startswith('rooms/')}
assert {p.name for p in (ROOT / 'words').glob('*.md')} == {Path(p).name for p in before if p.startswith('words/')}

room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
start = '## A search reader can keep an old view — 2026-10-22\n\n'
assert room.count(start) == 1
prefix, rest = room.split(start, 1)
addition, suffix = rest.split('## Sources\n', 1)
assert digest((prefix + '## Sources\n' + suffix).encode()) == before['rooms/what-the-gaps-can-say.md']['sha256']
opening = [s for s in room.splitlines() if s.strip()][:3]
assert opening[0].startswith('# ')
assert opening[1].startswith('*') and opening[1].endswith('*')
assert not opening[2].startswith('#')

word = (ROOT / 'words/freshness-target.md').read_text()
heading = '## The reader has a freshness boundary too — 2026-10-22\n\n'
assert word.count(heading) == 1
word_prefix, rest = word.split(heading, 1)
word_addition, word_suffix = rest.split('Links:', 1)
old_uncertain = "uncertain: whether the historical expectation still applies, how this host brings in mail, and whether its updates share a cause with slow replies. The announcement alone answers none of those questions.\n\n"
assert digest((word_prefix + old_uncertain + 'Links:' + word_suffix).encode()) == before['words/freshness-target.md']['sha256']
assert word.startswith('# freshness-target\n\nA freshness target says how soon new information is meant to appear.\n')
assert word.strip().splitlines()[-1].startswith('Links:')

gate = (ROOT / 'gate.md').read_text()
old_glance = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [historical date-reading](evidence/gardener-2026-10-21-input-search/README.md) separated a thread's sorting date from its displayed date, not a mirror's update time; one question researched and still open, none planted, no watched Git requests or new timing samples)"
old_map = "- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — saved replies and historical hosting reports leave update times and causes unproved; a thread's displayed date can differ from its sorting date (updated 2026-10-21)"
lines = gate.splitlines(keepends=True)
assert sum(s.startswith('> rooms:') for s in lines) == 1
assert sum(s.startswith('- [what-the-gaps-can-say]') for s in lines) == 1
restored_gate = ''.join(old_glance + '\n' if s.startswith('> rooms:') else old_map + '\n' if s.startswith('- [what-the-gaps-can-say]') else s for s in lines)
assert digest(restored_gate.encode()) == before['gate.md']['sha256']
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and len(entries) == len(rooms) == 697
assert sum(s.startswith('- [ ]') for s in (ROOT / 'questions.md').read_text().splitlines()) == 16
assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())

sources = []
for receipt_path in sorted(HERE.glob('*-receipt.json')):
    label = receipt_path.name.removesuffix('-receipt.json')
    receipt = json.loads(receipt_path.read_text())
    raw = (HERE / (label + '.html')).read_bytes()
    assert digest(raw) == receipt['sha256'] and len(raw) == receipt['bytes']
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    assert receipt['started_utc'].startswith('2026-10-22')
    sources.append({'label': label, 'status': receipt['curl']['http_code'], 'hash_matches': True})
assert len(sources) == 4

link_count = 0
readme = (HERE / 'README.md').read_text()
for text, base in [(addition, ROOT / 'rooms'), (word_addition, ROOT / 'words'), (readme, HERE)]:
    for name in re.findall(r'\[\[([^]|]+)(?:\|[^]]+)?\]\]', text):
        candidates = [ROOT / (name + '.md'), ROOT / 'words' / (name + '.md'), ROOT / 'rooms' / (name + '.md')]
        assert any(p.is_file() and p.resolve().is_relative_to(ROOT) for p in candidates), name
        link_count += 1
    for href in re.findall(r'\]\(([^)]+)\)', text):
        if not urlparse(href).scheme and not href.startswith('#'):
            path = (base / href.split('#', 1)[0]).resolve()
            assert path.is_relative_to(ROOT) and path.exists(), href
            link_count += 1

chronicle = (ROOT / 'chronicle.md').read_bytes()
length = before['chronicle.md']['bytes']
assert digest(chronicle[:length]) == before['chronicle.md']['sha256']
new = chronicle[length:].decode()
if PRE:
    assert not new
else:
    assert re.fullmatch(r'- 2026-10-22 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', new), new

subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True, capture_output=True)
garden_changes = subprocess.check_output(['git', 'diff', 'HEAD', '--name-only', '--', 'garden/'], cwd=ROOT, text=True).strip()
assert not garden_changes
result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'phase': 'preclose' if PRE else 'complete',
    'passed': True,
    'changed_markdown': sorted(changed),
    'prior_text_preserved': True,
    'questions_quests_and_courtyard_unchanged': True,
    'open_questions': 16, 'open_quests': 8,
    'rooms': len(rooms), 'map_entries': len(entries), 'map_exact_once': True,
    'new_room_files': 0, 'new_word_files': 0,
    'sources': sources, 'added_local_links_checked': link_count,
    'chronicle_lines_added': len(new.splitlines()),
    'garden_tracked_changes': garden_changes,
    'git_diff_check': 'passed',
}
(HERE / ('preclose-verification.json' if PRE else 'verification.json')).write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
