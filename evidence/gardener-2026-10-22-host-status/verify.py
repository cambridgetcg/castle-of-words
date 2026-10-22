"""Check this visit against its own saved starting state."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from collections import Counter
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')
before = json.loads((HERE / 'before.json').read_text())
preclose = '--preclose' in sys.argv
changed = []
for rel, saved in before.items():
    path = ROOT / rel
    assert path.resolve().is_relative_to(ROOT)
    assert path.is_file(), f'Missing: {rel}'
    data = path.read_bytes()
    if sha256(data).hexdigest() != saved['sha256']:
        changed.append(rel)
assert changed == ([] if preclose else ['chronicle.md']), changed
for folder in ('rooms', 'words', 'garden'):
    current = {str(p.relative_to(ROOT)) for p in (ROOT / folder).rglob('*') if p.is_file()}
    old = {p for p in before if p.startswith(folder + '/')}
    assert current == old, (folder, current ^ old)
chronicle = (ROOT / 'chronicle.md').read_bytes()
old = before['chronicle.md']
assert sha256(chronicle[:old['bytes']]).hexdigest() == old['sha256']
addition = chronicle[old['bytes']:].decode()
if preclose:
    assert addition == ''
else:
    assert len(addition.splitlines()) == 1
    assert re.fullmatch(r'- 2026-10-22 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — A bounded search found no new evidence about the archive’s update times or delays, so its oldest eligible question stayed open\.\n', addition)
questions = (ROOT / 'questions.md').read_text()
assert sum(l.startswith('- [ ]') for l in questions.splitlines()) == 16
assert not any(l.startswith('- ') for l in (ROOT / 'courtyard.md').read_text().splitlines())
map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and all(n == 1 for n in Counter(entries).values())
labels = ('web-status', 'archive-delays', 'operator-update-query')
for label in labels:
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    data = (HERE / (label + '.html')).read_bytes()
    assert receipt['sha256'] == sha256(data).hexdigest()
    assert receipt['bytes'] == len(data)
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'mode': 'preclose' if preclose else 'closed',
    'all_checks_passed': True,
    'changed_baseline_files': changed,
    'saved_source_hashes_verified': len(labels),
    'room_count': len(rooms), 'map_entries': len(entries), 'map_exact_once': True,
    'open_questions': 16, 'courtyard_items': 0,
    'chronicle_added_lines': len(addition.splitlines()),
    'garden_unchanged': True, 'existing_room_and_word_files_unchanged': True,
}
output = HERE / ('preclose-verification.json' if preclose else 'verification.json')
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
