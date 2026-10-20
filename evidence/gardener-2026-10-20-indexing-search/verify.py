"""Check the completed visit using retained bytes, without network requests."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
before = json.loads((HERE / 'before.json').read_text())
preflight = json.loads((HERE / 'preflight.json').read_text())
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
assert {str(p.relative_to(ROOT)) for p in paths} == set(before)
unchanged = []
chronicle_line = None
for name, record in before.items():
    p = ROOT / name
    assert p.resolve().is_relative_to(ROOT)
    raw = p.read_bytes()
    if name == 'chronicle.md':
        prefix = raw[:record['bytes']]
        assert sha256(prefix).hexdigest() == record['sha256'], 'Chronicle history changed'
        suffix = raw[record['bytes']:].decode()
        assert len(suffix.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-20 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', suffix)
        chronicle_line = suffix.rstrip('\n')
    else:
        assert len(raw) == record['bytes'] and sha256(raw).hexdigest() == record['sha256'], name
        unchanged.append(name)

assert chronicle_line is not None
map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and len(entries) == len(rooms) == 697
open_questions = [line for line in (ROOT / 'questions.md').read_text().splitlines() if line.startswith('- [ ]')]
assert len(open_questions) == 16
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())
assert sum(line.startswith('- [ ]') for line in (ROOT / 'quests.md').read_text().splitlines()) == 8

garden_status = subprocess.run(['git', 'status', '--porcelain', '--', 'garden'], cwd=ROOT, check=True, capture_output=True, text=True).stdout
assert garden_status == preflight['garden_git_status'] == ''
receipts = sorted(HERE.glob('*-receipt.json'))
assert len(receipts) == 3
sources = []
for p in receipts:
    record = json.loads(p.read_text())
    label = p.name.removesuffix('-receipt.json')
    body = (HERE / (label + '.html')).read_bytes()
    assert len(body) == record['bytes'] and sha256(body).hexdigest() == record['sha256']
    assert record['exit_code'] == 0
    assert record['curl']['http_code'] == (404 if label == 'archive-gc' else 200)
    assert urlparse(record['url']).netloc in {'public-inbox.org', 'search.brave.com'}
    assert 'info/refs' not in record['url']
    sources.append({'label': label, 'status': record['curl']['http_code'], 'bytes': len(body), 'sha256': record['sha256']})

result = {
    'verified_utc': datetime.now(timezone.utc).isoformat(),
    'passed': True,
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'unchanged_castle_markdown_files': len(unchanged),
    'room_count': len(rooms), 'map_entries': len(entries),
    'map_missing': [], 'map_extra': [], 'map_duplicates': [],
    'open_questions': len(open_questions), 'open_quests': 8,
    'garden_git_status_unchanged': True,
    'chronicle_prefix_unchanged': True, 'chronicle_lines_appended': 1,
    'chronicle_line': chronicle_line,
    'source_receipts': sources,
}
(HERE / 'verification.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(result, indent=2, ensure_ascii=False))
