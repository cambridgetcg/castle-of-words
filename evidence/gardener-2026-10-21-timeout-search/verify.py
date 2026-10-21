"""Check only this finite visit's changes against its saved starting hashes."""
from collections import Counter
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
before = json.loads((HERE / 'before.json').read_text())
preclose = '--preclose' in sys.argv
old_summary = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [historical bug reading](evidence/gardener-2026-10-21-mail-route-search/README.md) found a reported missing-message error, fix and confirmation from 2025, not a diagnosis of later Git waits; one question researched and still open, none planted, no new service probes or watch)"
new_summary = "> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-21 (all 697 rooms listed once in the Map; a [bounded timeout search](evidence/gardener-2026-10-21-timeout-search/README.md) supplied no new evidence connecting the archive's changed Git views with delayed replies; one question researched and still open, none planted, no new service probes or watch)"
paths = sorted(ROOT.glob('*.md')) + sorted((ROOT / 'rooms').glob('*.md')) + sorted((ROOT / 'words').glob('*.md'))
assert {str(p.relative_to(ROOT)) for p in paths} == set(before), 'Unexpected markdown addition or removal'
changed = []
for path in paths:
    assert path.resolve().is_relative_to(ROOT)
    name = str(path.relative_to(ROOT))
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != before[name]['sha256']:
        changed.append(name)
assert set(changed) == ({'gate.md'} if preclose else {'gate.md', 'chronicle.md'}), changed

gate = (ROOT / 'gate.md').read_text()
assert gate.count(new_summary) == 1
restored = gate.replace(new_summary, old_summary, 1).encode()
assert sha256(restored).hexdigest() == before['gate.md']['sha256'], 'Unexpected gate edit'
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/#)]+)\.md(?:#[^)]*)?\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(rooms) == 697 and set(entries) == rooms
assert all(n == 1 for n in Counter(entries).values())
assert len(entries) == len(rooms)
assert sum(s.startswith('- [ ]') for s in (ROOT / 'questions.md').read_text().splitlines()) == 16
assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())

helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-20-operator-notes/fetch.py'))
source_results = []
for label in ('web-timeout', 'operator-timeout'):
    receipt = json.loads((HERE / f'{label}-receipt.json').read_text())
    raw = (HERE / f'{label}.html').read_bytes()
    assert len(raw) == receipt['bytes'] and sha256(raw).hexdigest() == receipt['sha256']
    assert receipt['exit_code'] == 0 and receipt['curl']['http_code'] == 200
    assert 'info/refs' not in receipt['url']
    text = helper['Text']()
    text.feed(raw.decode('utf-8', errors='replace'))
    cleaned = '\n'.join(s.strip() for s in ''.join(text.parts).splitlines() if s.strip()) + '\n'
    assert cleaned == (HERE / f'{label}-text.txt').read_text()
    assert list(dict.fromkeys(text.links)) == json.loads((HERE / f'{label}-links.json').read_text())
    source_results.append({'label': label, 'status': 200, 'bytes_verified': len(raw)})

chronicle = (ROOT / 'chronicle.md').read_bytes()
size = before['chronicle.md']['bytes']
assert sha256(chronicle[:size]).hexdigest() == before['chronicle.md']['sha256']
addition = chronicle[size:].decode()
if preclose:
    assert addition == ''
else:
    assert re.fullmatch(r'- 2026-10-21 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — A bounded timeout search supplied no evidence connecting the archive’s changed Git views with delayed replies\.\n', addition), addition
report = {
    'verified_utc': datetime.now(timezone.utc).isoformat(), 'mode': 'preclose' if preclose else 'final',
    'checks_passed': True, 'changed_existing_markdown': changed,
    'rooms': len(rooms), 'map_entries': len(entries), 'open_questions': 16, 'open_quests': 8,
    'new_rooms': 0, 'new_words': 0, 'filed': 0, 'researched': 1, 'answered': 0, 'planted': 0,
    'source_results': source_results, 'chronicle_addition': addition,
    'scope': 'Local consistency only; no claim of search completeness or independent service verification.',
}
output = HERE / ('preclose-verification.json' if preclose else 'verification.json')
output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(report, indent=2, ensure_ascii=False))
