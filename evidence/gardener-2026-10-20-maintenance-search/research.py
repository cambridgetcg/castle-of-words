"""One finite public search; no watched Git endpoints and no service changes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import quote
import json
import re
import runpy
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
assert not (HERE / 'before.json').exists(), 'Do not replay the snapshot'
paths = [ROOT / n for n in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md')]
paths += sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
before = {}
for path in paths:
    assert path.resolve().is_relative_to(ROOT)
    raw = path.read_bytes()
    before[str(path.relative_to(ROOT))] = {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}
(HERE / 'before.json').write_text(json.dumps(before, indent=2) + '\n')
open_questions = []
for number, line in enumerate((ROOT / 'questions.md').read_text().splitlines(), 1):
    if not line.startswith('- [ ]'):
        continue
    reserved = bool(re.search(r'commissioned|waits for: commission|waits for: yu|yu decides|being grown by another builder|needs yu', line, re.I))
    planted = re.findall(r'planted by [^\n)]{0,180}', line)
    open_questions.append({'line': number, 'reserved': reserved, 'planting': planted})
gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
room_names = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == room_names and len(entries) == len(room_names)
preflight = {
    'captured_utc': datetime.now(timezone.utc).isoformat(),
    'open_questions': open_questions,
    'eligible_in_file_order': [q['line'] for q in open_questions if not q['reserved']],
    'courtyard_items': sum(l.startswith('- ') for l in (ROOT / 'courtyard.md').read_text().splitlines()),
    'rooms': len(room_names), 'map_entries': len(entries),
    'garden_git_status': subprocess.run(['git', 'status', '--porcelain', '--', 'garden'], cwd=ROOT, check=True, capture_output=True, text=True).stdout,
}
(HERE / 'preflight.json').write_text(json.dumps(preflight, indent=2) + '\n')
print(json.dumps(preflight, indent=2), flush=True)
assert preflight['eligible_in_file_order'] == [740, 744, 766]
assert preflight['courtyard_items'] == 0

# Reuse the reviewed in-castle helper, without altering it or creating bytecode.
ns = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
fetch = ns['fetch']
fetch.__globals__['ROOT'] = HERE
pairs = [
    ('web-maintenance', 'https://search.brave.com/search?q=' + quote('"yhetil.org" "maintenance"')),
    ('operator-performance', 'https://public-inbox.org/meta/?q=' + quote('f:kyle@kyleam.com performance') + '&x=t'),
]
with ThreadPoolExecutor(max_workers=2) as pool:
    for outcome in pool.map(fetch, pairs):
        print(json.dumps(outcome), flush=True)
