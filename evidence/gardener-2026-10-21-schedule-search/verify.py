"""Verify this finite visit offline; do not change the castle pages."""
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
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
assert {str(p.relative_to(ROOT)) for p in paths} == set(before)
assert 'chronicle.md' in before
suffix = ''
for name, record in before.items():
    path = ROOT / name
    assert path.resolve().is_relative_to(ROOT)
    raw = path.read_bytes()
    if name == 'chronicle.md':
        assert sha256(raw[:record['bytes']]).hexdigest() == record['sha256']
        suffix = raw[record['bytes']:].decode()
        assert len(suffix.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-21 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', suffix)
    else:
        assert len(raw) == record['bytes'] and sha256(raw).hexdigest() == record['sha256'], name

map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and len(entries) == len(rooms) == 697
assert sum(line.startswith('- [ ]') for line in (ROOT / 'questions.md').read_text().splitlines()) == 16
assert sum(line.startswith('- [ ]') for line in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())
assert subprocess.run(['git', 'status', '--porcelain', '--', 'garden'], cwd=ROOT, check=True, capture_output=True, text=True).stdout == ''
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)

receipts = sorted(HERE.glob('*-receipt.json'))
assert len(receipts) == 2
sources = []
for path in receipts:
    record = json.loads(path.read_text())
    label = path.name.removesuffix('-receipt.json')
    raw = (HERE / (label + '.html')).read_bytes()
    assert len(raw) == record['bytes'] and sha256(raw).hexdigest() == record['sha256']
    assert record['exit_code'] == 0 and record['curl']['http_code'] == 200
    assert urlparse(record['url']).netloc in {'public-inbox.org', 'search.brave.com'}
    assert 'info/refs' not in record['url']
    sources.append({'label': label, 'status': 200, 'bytes': len(raw), 'sha256': record['sha256']})
for slug in ('what-the-gaps-can-say', 'mail-ingestion', 'freshness-target'):
    assert (ROOT / 'rooms' / (slug + '.md')).exists() or (ROOT / 'words' / (slug + '.md')).exists()

result = {
    'verified_utc': datetime.now(timezone.utc).isoformat(), 'passed': True,
    'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'unchanged_castle_markdown_files': len(before) - 1,
    'rooms': len(rooms), 'map_entries': len(entries), 'map_missing': [], 'map_extra': [], 'map_duplicates': [],
    'open_questions': 16, 'open_quests': 8, 'garden_git_status_clean': True,
    'chronicle_prefix_unchanged': True, 'chronicle_lines_appended': 1,
    'chronicle_line': suffix.rstrip('\n'), 'source_receipts': sources,
}
(HERE / 'verification.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(result, indent=2, ensure_ascii=False))
