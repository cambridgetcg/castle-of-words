"""One bounded search for the oldest available question; no service probes."""
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
paths = sorted(ROOT.glob('*.md'))
for name in ('rooms', 'words', 'garden'):
    paths += sorted(p for p in (ROOT / name).rglob('*') if p.is_file())
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
        questions.append({'line': n, 'reserved': reserved, 'planted': re.findall(r'planted[^)]*?\d{4}-\d{2}-\d{2}', line)})
map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
preflight = {
    'captured_utc': datetime.now(timezone.utc).isoformat(),
    'questions': questions,
    'eligible_oldest_first': [q['line'] for q in questions if not q['reserved']],
    'open_questions': len(questions),
    'courtyard_items': sum(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines()),
    'room_count': len(rooms), 'map_entries': len(entries),
    'map_exact_once': set(entries) == rooms and len(entries) == len(rooms),
    'chronicle_lines': len((ROOT / 'chronicle.md').read_text().splitlines()),
}
(HERE / 'preflight.json').write_text(json.dumps(preflight, indent=2) + '\n')
assert preflight['eligible_oldest_first'] == [740, 744, 766]
assert preflight['open_questions'] == 16
assert preflight['courtyard_items'] == 0
assert preflight['map_exact_once']
print(json.dumps({k: v for k, v in preflight.items() if k != 'questions'}), flush=True)
helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
fetch = helper['fetch']
fetch.__globals__['ROOT'] = HERE
pairs = [
    ('web-status', 'https://search.brave.com/search?q=' + quote('"yhetil.org" "status" "maintenance"')),
    ('archive-delays', 'https://public-inbox.org/meta/?q=' + quote('f:kyleam.com (slow OR latency OR stall OR delayed)')),
]
with ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(fetch, pairs):
        print(json.dumps(result), flush=True)
