"""Offline consistency checks for this bounded gardening visit."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
assert ROOT == Path('/Users/yu/castle').resolve()
closed = sys.argv[1:] == ['--closed']
assert sys.argv[1:] in ([], ['--closed'])
before = json.loads((HERE / 'before.json').read_text())
original_summary = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [hosting-report reading](evidence/gardener-2026-10-21-deployment-search/README.md) adds a 2021 account naming nginx and Varnish without treating it as today's configuration or a cause of delays; one question researched and still open, none planted, no new service probes or watch)"
new_summary = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [bounded upkeep search](evidence/gardener-2026-10-21-upkeep-search/README.md) found no new evidence about the mirror's update schedule or delays; one question researched and still open, none planted, no new service probes or watch)"
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
assert {str(p.relative_to(ROOT)) for p in paths} == set(before)
changed = []
for relative, record in before.items():
    raw = (ROOT / relative).read_bytes()
    if sha256(raw).hexdigest() != record['sha256']:
        changed.append(relative)
assert sorted(changed) == sorted(['gate.md', 'chronicle.md'] if closed else ['gate.md']), changed

gate = (ROOT / 'gate.md').read_text()
assert gate.count(new_summary) == 1
reverted_gate = gate.replace(new_summary, original_summary, 1).encode()
assert sha256(reverted_gate).hexdigest() == before['gate.md']['sha256']
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\).*$', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(entries) == len(rooms) == 697 and set(entries) == rooms
assert sum(s.startswith('- [ ]') for s in (ROOT / 'questions.md').read_text().splitlines()) == 16
assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())

helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
sources = []
for label in ('web-repack', 'operator-gc'):
    receipt = json.loads((HERE / (label + '-receipt.json')).read_text())
    raw = (HERE / (label + '.html')).read_bytes()
    assert receipt['sha256'] == sha256(raw).hexdigest()
    assert receipt['bytes'] == len(raw)
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    text = helper['Text']()
    text.feed(raw.decode('utf-8', errors='replace'))
    cleaned = '\n'.join(s.strip() for s in ''.join(text.parts).splitlines() if s.strip()) + '\n'
    assert cleaned == (HERE / (label + '-text.txt')).read_text()
    assert list(dict.fromkeys(text.links)) == json.loads((HERE / (label + '-links.json')).read_text())
    sources.append({'label': label, 'status': receipt['curl']['http_code'], 'sha256_matches': True})
for link in re.findall(r'\[\[([^\]]+)\]\]', (HERE / 'README.md').read_text()):
    assert any((ROOT / kind / (link + '.md')).is_file() for kind in ('rooms', 'words')), link

chronicle_line = None
if closed:
    raw = (ROOT / 'chronicle.md').read_bytes()
    n = before['chronicle.md']['bytes']
    assert sha256(raw[:n]).hexdigest() == before['chronicle.md']['sha256']
    added = raw[n:].decode()
    pattern = r'- 2026-10-21 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — Two bounded upkeep searches added no evidence about the mirror’s updates or delays, so the oldest eligible question stayed open\.\n'
    assert re.fullmatch(pattern, added), repr(added)
    chronicle_line = added.rstrip('\n')
report = {
    'verified_utc': datetime.now(timezone.utc).isoformat(),
    'phase': 'closed' if closed else 'preclose',
    'ok': True,
    'changed_existing_markdown': changed,
    'rooms': len(rooms), 'map_entries': len(entries),
    'rooms_words_and_queues_unchanged': True,
    'open_questions': 16, 'open_quests': 8, 'courtyard_items': 0,
    'gate_only_summary_replaced': True,
    'sources': sources,
    'chronicle_appended_lines': 1 if closed else 0,
    'chronicle_line': chronicle_line,
}
name = 'verification.json' if closed else 'preclose-verification.json'
(HERE / name).write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
