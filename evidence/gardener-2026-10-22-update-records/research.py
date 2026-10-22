"""A bounded public-source reading for the oldest unreserved question."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import quote
import json
import re
import runpy
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')


def baseline():
    assert not (HERE / 'before.json').exists()
    paths = list(ROOT.glob('*.md'))
    for folder in ('rooms', 'words', 'garden'):
        paths.extend(p for p in (ROOT / folder).rglob('*') if p.is_file())
    before = {}
    for path in sorted(paths):
        assert path.resolve().is_relative_to(ROOT)
        data = path.read_bytes()
        before[str(path.relative_to(ROOT))] = {'bytes': len(data), 'sha256': sha256(data).hexdigest()}
    (HERE / 'before.json').write_text(json.dumps(before, indent=2) + '\n')
    questions = []
    for n, line in enumerate((ROOT / 'questions.md').read_text().splitlines(), 1):
        if line.startswith('- [ ]'):
            reserved = bool(re.search(r'commissioned|waits for: commission|waits for: yu|yu decides|being grown by another builder|needs yu', line, re.I))
            questions.append({'line': n, 'reserved': reserved})
    map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
    entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
    rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
    summary = {
        'captured_utc': datetime.now(timezone.utc).isoformat(),
        'questions': questions,
        'eligible_oldest_first': [q['line'] for q in questions if not q['reserved']],
        'open_questions': len(questions),
        'courtyard_items': sum(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines()),
        'room_count': len(rooms), 'map_entries': len(entries),
        'map_exact_once': set(entries) == rooms and len(entries) == len(rooms),
    }
    (HERE / 'preflight.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary), flush=True)


def fetch_pairs(pairs):
    assert 0 < len(pairs) <= 3
    helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
    fetch = helper['fetch']
    fetch.__globals__['ROOT'] = HERE
    with ThreadPoolExecutor(max_workers=len(pairs)) as pool:
        for result in pool.map(fetch, pairs):
            print(json.dumps(result), flush=True)


if __name__ == '__main__':
    if sys.argv[1:] == ['start']:
        baseline()
        fetch_pairs([
            ('schedule-search', 'https://search.brave.com/search?q=' + quote('"yhetil.org" "cron"')),
            ('update-record-search', 'https://search.brave.com/search?q=' + quote('"yhetil.org" "git" "maintenance"')),
        ])
    else:
        args = sys.argv[1:]
        assert args and len(args) % 2 == 0
        fetch_pairs(list(zip(args[::2], args[1::2])))
