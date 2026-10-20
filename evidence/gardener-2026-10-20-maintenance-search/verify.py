"""Verify this visit's kept evidence and edit boundary, without network access."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
before = json.loads((HERE / 'before.json').read_text())
preflight = json.loads((HERE / 'preflight.json').read_text())
expected_line = (
    '- 2026-10-20 19:33 · visit: filed 0, researched 1, planted 0 — '
    'A bounded maintenance search added no new evidence about the mirror’s changes or delays, so the question stayed open.\n'
)
unchanged = []
for name, entry in before.items():
    if name == 'chronicle.md':
        continue
    path = ROOT / name
    assert path.resolve().is_relative_to(ROOT)
    raw = path.read_bytes()
    assert sha256(raw).hexdigest() == entry['sha256'], name
    assert len(raw) == entry['bytes'], name
    unchanged.append(name)

chronicle = (ROOT / 'chronicle.md').read_bytes()
old = before['chronicle.md']
assert sha256(chronicle[:old['bytes']]).hexdigest() == old['sha256']
assert chronicle[old['bytes']:] == expected_line.encode()
assert chronicle.count(expected_line.encode()) == 1
courtyard = (ROOT / 'courtyard.md').read_text()
assert courtyard.startswith('# Courtyard\n')
assert not any(line.startswith('- ') for line in courtyard.splitlines())
open_count = sum(line.startswith('- [ ]') for line in (ROOT / 'questions.md').read_text().splitlines())
assert open_count == 16 == len(preflight['open_questions'])

room_names = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
counts = Counter(entries)
assert set(counts) == room_names
assert all(n == 1 for n in counts.values())
assert len(room_names) == 697
current_pages = {str(p.relative_to(ROOT)) for d in ('rooms', 'words') for p in (ROOT / d).glob('*.md')}
old_pages = {name for name in before if name.startswith(('rooms/', 'words/'))}
assert current_pages == old_pages

retrievals = []
for receipt_file in sorted(HERE.glob('*-receipt.json')):
    receipt = json.loads(receipt_file.read_text())
    label = receipt_file.name.removesuffix('-receipt.json')
    body = HERE / (label + '.html')
    raw = body.read_bytes() if body.exists() else b''
    assert len(raw) == receipt['bytes']
    assert sha256(raw).hexdigest() == receipt['sha256']
    if not body.exists():
        assert receipt['exit_code'] != 0 and receipt['curl']['http_code'] == 0
    assert 'info/refs' not in receipt['url']
    retrievals.append({'label': label, 'exit_code': receipt['exit_code'],
                       'http_code': receipt['curl']['http_code'],
                       'response_body_present': body.exists(),
                       'saved_bytes': len(raw), 'hash_matches_receipt': True})
assert len(retrievals) == 3
assert Counter(r['http_code'] for r in retrievals) == Counter([200, 429, 0])
garden_status = subprocess.run(['git', 'status', '--porcelain', '--', 'garden'], cwd=ROOT,
                               check=True, capture_output=True, text=True).stdout
assert garden_status == preflight['garden_git_status'] == ''
result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(), 'passed': True,
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'open_questions': open_count, 'rooms': len(room_names), 'map_entries': len(entries),
    'map_missing': [], 'map_extra': [], 'map_duplicates': [],
    'unchanged_page_count': len(unchanged), 'new_rooms_or_words': 0,
    'chronicle_prefix_unchanged': True, 'chronicle_lines_appended': 1,
    'garden_git_status_unchanged_and_empty': True, 'retrievals': retrievals,
}
(HERE / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
