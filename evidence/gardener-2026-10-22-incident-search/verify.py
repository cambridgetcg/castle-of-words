"""Verify this reading-only visit against its saved starting inventory."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')
before = json.loads((HERE / 'before.json').read_text())
preflight = json.loads((HERE / 'preflight.json').read_text())
paths = list(ROOT.glob('*.md'))
for folder in ('rooms', 'words', 'garden'):
    paths.extend(p for p in (ROOT / folder).rglob('*') if p.is_file())
after = {}
for path in paths:
    assert path.resolve().is_relative_to(ROOT), str(path)
    data = path.read_bytes()
    after[str(path.relative_to(ROOT))] = {
        'bytes': len(data), 'sha256': sha256(data).hexdigest()
    }
assert set(after) == set(before), 'Unexpected new or removed grounds file'
changed = sorted(k for k in before if before[k] != after[k])
assert changed == ['chronicle.md'], changed
chronicle = (ROOT / 'chronicle.md').read_bytes()
old_size = before['chronicle.md']['bytes']
assert sha256(chronicle[:old_size]).hexdigest() == before['chronicle.md']['sha256']
added = chronicle[old_size:].decode()
assert re.fullmatch(
    r'- 2026-10-22 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — '
    r'A bounded incident search added no evidence about the archive’s update times or delays, so its oldest eligible question stayed open\.\n',
    added,
), repr(added)
map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert Counter(entries) == Counter({name: 1 for name in rooms})
assert preflight['courtyard_items'] == 0
assert preflight['open_questions'] == 16
assert preflight['eligible_oldest_first'] == [740, 744, 766]
results = []
for label, status, exit_code in (
    ('update-delay-search', 200, 0),
    ('incident-search', 200, 0),
    ('archive-incident-search', 0, 7),
):
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    body = HERE / (label + '.html')
    raw = body.read_bytes() if body.exists() else b''
    assert len(raw) == receipt['bytes']
    assert sha256(raw).hexdigest() == receipt['sha256']
    assert receipt['exit_code'] == exit_code
    assert receipt['curl']['http_code'] == status
    assert 'info/refs' not in receipt['url']
    results.append({'label': label, 'http_status': status, 'curl_exit': exit_code, 'bytes': len(raw)})
report = {
    'passed': True,
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'changed_grounds_files': changed,
    'chronicle_lines_appended': 1,
    'map_rooms_exactly_once': len(rooms),
    'open_questions_unchanged': 16,
    'garden_unchanged': True,
    'retrievals': results,
    'scope': 'Local consistency only; no new service measurement or answer.'
}
(HERE / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
