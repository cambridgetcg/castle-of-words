"""One bounded reading of the oldest eligible question; no service probes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import quote
import json
import re
import runpy

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')
assert not (HERE / 'before.json').exists()
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
before = {}
for path in paths:
    assert path.resolve().is_relative_to(ROOT)
    data = path.read_bytes()
    before[str(path.relative_to(ROOT))] = {'bytes': len(data), 'sha256': sha256(data).hexdigest()}
(HERE / 'before.json').write_text(json.dumps(before, indent=2) + '\n')
questions = []
for n, line in enumerate((ROOT / 'questions.md').read_text().splitlines(), 1):
    if line.startswith('- [ ]'):
        reserved = bool(re.search(r'commissioned|waits for: commission|waits for: yu|yu decides|being grown by another builder|needs yu', line, re.I))
        questions.append({'line': n, 'reserved': reserved, 'planting': re.findall(r'planted[^)]*?\d{4}-\d{2}-\d{2}', line)})
map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
preflight = {
    'captured_utc': datetime.now(timezone.utc).isoformat(),
    'questions': questions,
    'eligible_in_file_order': [q['line'] for q in questions if not q['reserved']],
    'open_questions': len(questions),
    'open_quests': sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()),
    'courtyard_items': sum(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines()),
    'rooms': len(rooms), 'map_entries': len(entries),
    'map_exact_once': set(entries) == rooms and len(entries) == len(rooms),
}
assert preflight['eligible_in_file_order'] == [740, 744, 766]
assert preflight['courtyard_items'] == 0
assert preflight['map_exact_once']
(HERE / 'preflight.json').write_text(json.dumps(preflight, indent=2) + '\n')
print(json.dumps(preflight, indent=2), flush=True)
helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
fetch = helper['fetch']
fetch.__globals__['ROOT'] = HERE
pairs = [
    ('web-schedule', 'https://search.brave.com/search?q=' + quote('"yhetil" "orgmode" "update"')),
    ('archive-schedule', 'https://public-inbox.org/meta/?q=' + quote('f:kyleam.com (cron OR timer OR schedule)')),
]
with ThreadPoolExecutor(max_workers=2) as pool:
    for outcome in pool.map(fetch, pairs):
        print(json.dumps(outcome), flush=True)
