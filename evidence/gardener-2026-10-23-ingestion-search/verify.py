"""Verify this quiet reading visit without altering castle content."""
from collections import Counter
from datetime import datetime
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
    raw = path.read_bytes()
    after[str(path.relative_to(ROOT))] = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
assert set(before) == set(after), 'Unexpected new or missing grounds file'
changed = sorted(k for k in before if before[k] != after[k])
assert changed == ([] if preclose else ['chronicle.md']), changed

questions = (ROOT / 'questions.md').read_text()
assert sum(s.startswith('- [ ]') for s in questions.splitlines()) == 16
assert preflight['eligible_oldest_first'] == [740, 744, 766]
assert questions.splitlines()[739].startswith('- [ ] Door 736')
assert preflight['courtyard_items'] == 0
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())
assert preflight['open_questions'] == 16
reserved = sum(q['reserved'] for q in preflight['questions'])

gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert Counter(entries) == Counter({name: 1 for name in rooms})
assert len(rooms) == preflight['room_count'] == 697
room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
assert '# what-the-gaps-can-say\n\n*' in room
assert '## Old mail can enter by more than one route — 2026-10-20' in room
assert '## A reproduced bug keeps its own address — 2026-10-21' in room
assert 'https://public-inbox.org/meta/87y2k67ogi.fsf@kyleam.com/' in room
assert 'https://public-inbox.org/meta/871pn6vzvd.fsf@kyleam.com/' in room

labels = ['watch-search', 'archive-watch-search', 'archive-update-search',
          'duplicate-report', 'httpd-report']
retrievals = []
for label in labels:
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    raw = (HERE / (label + '.html')).read_bytes()
    assert receipt['bytes'] == len(raw)
    assert receipt['sha256'] == sha256(raw).hexdigest()
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    assert datetime.fromisoformat(receipt['started_utc']).astimezone().date().isoformat() == '2026-10-23'
    retrievals.append({'label': label, 'http_status': 200, 'curl_exit': 0})
search = (HERE / 'watch-search-text.txt').read_text()
assert 'search operators  were not applied' in search
assert 'Too few matches were found' in search
assert 'Results 1-1 of 1' in (HERE / 'archive-watch-search-text.txt').read_text()
assert 'Results 1-4 of 4' in (HERE / 'archive-update-search-text.txt').read_text()
assert 'restarted\n-watch' in (HERE / 'duplicate-report-text.txt').read_text()
assert "_message ID that's not found_" in (HERE / 'httpd-report-text.txt').read_text()
assert (HERE / 'README.md').is_file()

chronicle = (ROOT / 'chronicle.md').read_bytes()
old_size = before['chronicle.md']['bytes']
assert sha256(chronicle[:old_size]).hexdigest() == before['chronicle.md']['sha256']
added = chronicle[old_size:].decode()
if preclose:
    assert not added
else:
    assert re.fullmatch(
        r'- 2026-10-23 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — '
        r'A bounded ingestion search returned already-recorded reports without supplying the archive’s update times or explaining later delays\.\n', added), repr(added)
result = {
    'passed': True, 'phase': 'preclose' if preclose else 'closed',
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'new_words': 0, 'new_rooms': 0, 'open_questions': 16,
    'reserved_questions_unchanged': reserved,
    'all_questions_unchanged': True, 'garden_unchanged': True,
    'map_rooms_exactly_once': len(rooms), 'map_unchanged': True,
    'changed_existing_grounds_files': changed,
    'chronicle_lines_appended': len(added.splitlines()),
    'retrievals': retrievals,
    'scope': 'Local consistency only; no new service observations or conclusions.'
}
output = 'preclose-verification.json' if preclose else 'verification.json'
(HERE / output).write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
