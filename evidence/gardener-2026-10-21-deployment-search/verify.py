"""Offline consistency checks for this finite reading; does not change castle pages."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import runpy
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
closed = sys.argv[1:] == ['--closed']
assert not sys.argv[1:] or closed
before = json.loads((HERE / 'before.json').read_text())
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
assert {str(p.relative_to(ROOT)) for p in paths} == set(before)
allowed = {'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/via-header.md', 'chronicle.md'}
changed = []
suffix = ''
for path in paths:
    assert path.resolve().is_relative_to(ROOT)
    name = str(path.relative_to(ROOT))
    raw = path.read_bytes()
    record = before[name]
    if sha256(raw).hexdigest() != record['sha256']:
        changed.append(name)
    if name == 'chronicle.md':
        assert sha256(raw[:record['bytes']]).hexdigest() == record['sha256']
        suffix = raw[record['bytes']:].decode()
        if closed:
            assert len(suffix.splitlines()) == 1
            assert re.fullmatch(r'- 2026-10-21 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', suffix)
        else:
            assert not suffix
    elif name not in allowed:
        assert len(raw) == record['bytes'] and sha256(raw).hexdigest() == record['sha256'], name
assert set(changed) == (allowed if closed else allowed - {'chronicle.md'})

for name, start, end in [
    ('rooms/what-the-gaps-can-say.md', '## A host named its helpers — 2026-10-21\n', '## Sources\n'),
    ('words/via-header.md', '## The same name in an older account — 2026-10-21\n', 'Links: '),
]:
    text = (ROOT / name).read_text()
    assert text.count(start) == 1
    a = text.index(start)
    b = text.index(end, a)
    original = (text[:a] + text[b:]).encode()
    assert sha256(original).hexdigest() == before[name]['sha256'], name
    assert 'https://public-inbox.org/meta/87v9bmswkh.fsf@kyleam.com/' in text[a:b]
    assert 'uncertain:' in text[a:b]
word = (ROOT / 'words/via-header.md').read_text().splitlines()
room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text().splitlines()
assert word[0] == '# via-header' and word[-1].startswith('Links: ')
assert room[0] == '# what-the-gaps-can-say' and room[2].startswith('*') and room[2].endswith('*')

map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(entries) == len(rooms) == 697 and set(entries) == rooms
assert sum(s.startswith('- [ ]') for s in (ROOT / 'questions.md').read_text().splitlines()) == 16
assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())
assert subprocess.run(['git', 'status', '--porcelain', '--', 'garden'], cwd=ROOT, check=True, capture_output=True, text=True).stdout == ''
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)

helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
receipts = sorted(HERE.glob('*-receipt.json'))
assert len(receipts) == 3
sources = []
for path in receipts:
    record = json.loads(path.read_text())
    label = path.name.removesuffix('-receipt.json')
    raw = (HERE / (label + '.html')).read_bytes()
    assert len(raw) == record['bytes'] and sha256(raw).hexdigest() == record['sha256']
    assert record['exit_code'] == 0 and record['curl']['http_code'] == 200
    assert urlparse(record['url']).netloc in {'public-inbox.org', 'search.brave.com'}
    assert 'info/refs' not in record['url']
    text = helper['Text']()
    text.feed(raw.decode('utf-8', errors='replace'))
    cleaned = '\n'.join(s.strip() for s in ''.join(text.parts).splitlines() if s.strip()) + '\n'
    assert cleaned == (HERE / (label + '-text.txt')).read_text()
    assert list(dict.fromkeys(text.links)) == json.loads((HERE / (label + '-links.json')).read_text())
    sources.append({'label': label, 'status': 200, 'bytes': len(raw), 'sha256': record['sha256']})
primary = (HERE / 'operator-stack-text.txt').read_text()
assert 'yhetil.org uses nginx and varnish' in primary
assert 'Date: Sun, 24 Jan 2021' in primary
assert '400 Bad Request' in primary
for slug in ('what-the-gaps-can-say', 'via-header', 'proxy-status', 'measuring-the-window'):
    assert (ROOT / 'rooms' / (slug + '.md')).exists() or (ROOT / 'words' / (slug + '.md')).exists()
assert (HERE / 'README.md').is_file()

result = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'passed': True, 'closed': closed,
          'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
          'changed_castle_markdown': changed, 'original_room_and_word_text_preserved': True,
          'rooms': len(rooms), 'map_entries': len(entries), 'map_missing': [], 'map_extra': [], 'map_duplicates': [],
          'open_questions': 16, 'open_quests': 8, 'garden_git_status_clean': True,
          'chronicle_prefix_unchanged': True, 'chronicle_lines_appended': len(suffix.splitlines()),
          'chronicle_line': suffix.rstrip('\n'), 'source_receipts': sources}
(HERE / ('verification.json' if closed else 'preclose-verification.json')).write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(result, indent=2, ensure_ascii=False))
