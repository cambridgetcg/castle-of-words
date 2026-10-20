"""Check this bounded visit's artifacts without contacting the network."""
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
expected_line = (
    '- 2026-10-20 16:23 · visit: filed 0, researched 1, planted 0 — '
    'Bounded public searches supplied no new evidence about the mirror’s '
    'update schedule or delays, so the question stayed open.\n'
)

unchanged = []
for name, entry in before.items():
    if not isinstance(entry, dict) or name == 'chronicle.md':
        continue
    raw = (ROOT / name).read_bytes()
    assert sha256(raw).hexdigest() == entry['sha256'], name
    unchanged.append(name)

chronicle = (ROOT / 'chronicle.md').read_bytes()
old = before['chronicle.md']
assert sha256(chronicle[:old['bytes']]).hexdigest() == old['sha256']
assert chronicle[old['bytes']:] == expected_line.encode('utf-8')

courtyard = (ROOT / 'courtyard.md').read_text()
assert courtyard.startswith('# Courtyard\n')
assert not any(line.startswith('- ') for line in courtyard.splitlines())
questions = (ROOT / 'questions.md').read_text()
open_count = sum(line.startswith('- [ ]') for line in questions.splitlines())
assert open_count == 16

room_names = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(
    r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$',
    map_text, re.M,
)
counts = Counter(entries)
assert set(counts) == room_names
assert all(n == 1 for n in counts.values())
assert len(room_names) == 697

retrievals = []
for receipt_file in sorted(HERE.glob('*-receipt.json')):
    receipt = json.loads(receipt_file.read_text())
    label = receipt_file.name.removesuffix('-receipt.json')
    body = HERE / (label + '.html')
    raw = body.read_bytes() if body.exists() else b''
    assert len(raw) == receipt['bytes']
    assert sha256(raw).hexdigest() == receipt['sha256']
    if not body.exists():
        assert receipt['exit_code'] != 0
        assert receipt['curl']['http_code'] == 0
    assert 'info/refs' not in receipt['url']
    retrievals.append({
        'label': label,
        'exit_code': receipt['exit_code'],
        'http_code': receipt['curl']['http_code'],
        'response_body_present': body.exists(),
        'saved_bytes': len(raw),
        'hash_matches_receipt': True,
    })
assert len(retrievals) == 4
assert Counter(r['http_code'] for r in retrievals) == Counter([200, 404, 429, 0])

garden_status = subprocess.run(
    ['git', 'status', '--porcelain', '--', 'garden'], cwd=ROOT,
    check=True, capture_output=True, text=True,
).stdout
assert garden_status == ''

result = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'passed': True,
    'filed': 0,
    'researched': 1,
    'answered': 0,
    'planted': 0,
    'open_questions': open_count,
    'rooms': len(room_names),
    'map_entries': len(entries),
    'map_missing': [],
    'map_extra': [],
    'map_duplicates': [],
    'unchanged_files': unchanged,
    'chronicle_prefix_unchanged': True,
    'chronicle_lines_appended': 1,
    'garden_git_status_empty': True,
    'retrievals': retrievals,
}
(HERE / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
