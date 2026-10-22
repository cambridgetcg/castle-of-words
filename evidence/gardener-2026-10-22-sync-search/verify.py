"""Verify this visit's bounded reading; no claim about the watched service."""
from collections import Counter
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
    data = path.read_bytes()
    after[str(path.relative_to(ROOT))] = {
        'bytes': len(data), 'sha256': sha256(data).hexdigest()
    }
assert set(after) == set(before), 'Unexpected new or removed grounds file'
changed = sorted(k for k in before if before[k] != after[k])
assert changed == ([] if preclose else ['chronicle.md']), changed
chronicle = (ROOT / 'chronicle.md').read_bytes()
old_size = before['chronicle.md']['bytes']
assert sha256(chronicle[:old_size]).hexdigest() == before['chronicle.md']['sha256']
added = chronicle[old_size:].decode()
if preclose:
    assert not added
else:
    assert re.fullmatch(
        r'- 2026-10-22 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — '
        r'A bounded synchronization search found no new evidence about the archive’s update times or delays, so the oldest eligible question stayed open\.\n',
        added,
    ), repr(added)
map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert Counter(entries) == Counter({name: 1 for name in rooms})
assert preflight['courtyard_items'] == 0
assert preflight['open_questions'] == 16
assert preflight['eligible_oldest_first'] == [740, 744, 766]
assert sum(s.startswith('- [ ]') for s in (ROOT / 'questions.md').read_text().splitlines()) == 16
retrievals = []
for label, status in [('sync-search', 200), ('operator-search', 200), ('archive-sync-search', 404)]:
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    body = (HERE / (label + '.html')).read_bytes()
    assert receipt['bytes'] == len(body)
    assert receipt['sha256'] == sha256(body).hexdigest()
    assert receipt['exit_code'] == 0
    assert receipt['curl']['http_code'] == status
    assert 'info/refs' not in receipt['url']
    assert receipt['started_utc'].startswith('2026-10-22')
    retrievals.append({'label': label, 'http_status': status, 'curl_exit': 0})
assert '[No results found]' in (HERE / 'archive-sync-search-text.txt').read_text()
report = {
    'passed': True, 'phase': 'preclose' if preclose else 'closed',
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'changed_grounds_files': changed,
    'chronicle_lines_appended': len(added.splitlines()),
    'map_rooms_exactly_once': len(rooms),
    'open_questions_unchanged': 16, 'garden_unchanged': True,
    'retrievals': retrievals,
    'scope': 'Local consistency only; no new service measurement or answer.'
}
output = 'preclose-verification.json' if preclose else 'verification.json'
(HERE / output).write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
