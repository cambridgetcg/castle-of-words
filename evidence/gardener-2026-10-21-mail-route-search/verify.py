"""Check this visit's local changes without contacting any service."""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
preclose = '--preclose' in sys.argv
before = json.loads((HERE / 'before.json').read_text())
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
current = {str(p.relative_to(ROOT)): p.read_bytes() for p in paths}
assert set(current) - set(before) == {'words/reproducer.md'}
assert set(before) - set(current) == set()
allowed = {'gate.md', 'rooms/what-the-gaps-can-say.md', 'chronicle.md'}
for name, record in before.items():
    if name not in allowed:
        assert sha256(current[name]).hexdigest() == record['sha256'], name

room = current['rooms/what-the-gaps-can-say.md'].decode()
heading = '## A reproduced bug keeps its own address — 2026-10-21\n'
assert room.count(heading) == 1
prefix, rest = room.split(heading, 1)
addition, suffix = rest.split('## Sources\n', 1)
restored_room = prefix + '## Sources\n' + suffix
assert sha256(restored_room.encode()).hexdigest() == before['rooms/what-the-gaps-can-say.md']['sha256']
assert room.splitlines()[0] == '# what-the-gaps-can-say'
assert room.splitlines()[2].startswith('*') and room.splitlines()[2].endswith('*')
assert '**740 remains open.** uncertain:' in addition

word = current['words/reproducer.md'].decode()
assert word.startswith('# reproducer\n\nA reproducer is ')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
for name in set(re.findall(r'\[\[([^\]|#]+)', word + addition)):
    assert any((ROOT / group / (name + '.md')).is_file() for group in ('words', 'rooms')), name

old_glance = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [bounded upkeep search](evidence/gardener-2026-10-21-upkeep-search/README.md) found no new evidence about the mirror's update schedule or delays; one question researched and still open, none planted, no new service probes or watch)"
old_map = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — saved replies and historical hosting accounts do not by themselves reveal current update jobs, server arrangements, or a cause connecting changes with slow replies (updated 2026-10-21)'
gate = current['gate.md'].decode()
assert gate.count('> rooms: ') == 1
assert gate.count('- [what-the-gaps-can-say]') == 1
restored_gate = re.sub(r'^> rooms: .*$', lambda _: old_glance, gate, flags=re.M)
restored_gate = re.sub(r'^- \[what-the-gaps-can-say\].*$', lambda _: old_map, restored_gate, flags=re.M)
assert sha256(restored_gate.encode()).hexdigest() == before['gate.md']['sha256']
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and len(entries) == len(rooms) == 697
questions = current['questions.md'].decode()
assert sum(s.startswith('- [ ]') for s in questions.splitlines()) == 16
assert sum(s.startswith('- [ ]') for s in current['quests.md'].decode().splitlines()) == 8
assert sum(s.startswith('- ') for s in current['courtyard.md'].decode().splitlines()) == 0

helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
labels = ['web-mbsync', 'operator-org', 'operator-reproducer', 'patch-reply', 'operator-confirmation']
for label in labels:
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    raw = (HERE / (label + '.html')).read_bytes()
    assert sha256(raw).hexdigest() == receipt['sha256']
    assert len(raw) == receipt['bytes']
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    text = helper['Text']()
    text.feed(raw.decode('utf-8', errors='replace'))
    cleaned = '\n'.join(s.strip() for s in ''.join(text.parts).splitlines() if s.strip()) + '\n'
    assert cleaned == (HERE / (label + '-text.txt')).read_text()
    assert list(dict.fromkeys(text.links)) == json.loads((HERE / (label + '-links.json')).read_text())
assert parsedate_to_datetime('Mon, 20 Oct 2025 23:39:50 -0400').astimezone(timezone.utc).isoformat() == '2025-10-21T03:39:50+00:00'

chronicle = current['chronicle.md']
prior = before['chronicle.md']
assert sha256(chronicle[:prior['bytes']]).hexdigest() == prior['sha256']
extra = chronicle[prior['bytes']:].decode()
if preclose:
    assert extra == ''
else:
    assert len(extra.splitlines()) == 1
    assert re.fullmatch(r'- 2026-10-21 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — A reported message-search bug and its fix gained a place without becoming an explanation of later Git delays\.\n', extra)
result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'passed': True,
    'preclose': preclose,
    'retrievals_verified': len(labels),
    'rooms': len(rooms),
    'map_entries': len(entries),
    'open_questions': 16,
    'open_quests': 8,
    'courtyard_items': 0,
    'new_words': ['reproducer'],
    'other_checked_markdown_unchanged': True,
    'room_previous_bytes_preserved': True,
    'gate_only_two_lines_replaced': True,
    'chronicle_lines_added': len(extra.splitlines()),
}
out = HERE / ('preclose-verification.json' if preclose else 'verification.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
