"""Same-session verification of saved evidence and the finite gardener visit."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents

def read(path):
    path = path.resolve()
    assert ROOT in path.parents
    return path.read_bytes()

def digest(data):
    return sha256(data).hexdigest()

before = json.loads(read(OUT / 'before.json'))
analysis = json.loads(read(OUT / 'analysis.json'))
for name, expected in analysis['input_sha256'].items():
    assert digest(read(ROOT / name)) == expected, name
for source in json.loads(read(OUT / 'sources.json')):
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert digest(read(OUT / source['file'])) == source['sha256']

# Verify prior prose was preserved, including the historical gate archive.
changed = {'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md', 'words/latency-by-outcome.md'}
for name, meta in before.items():
    current = read(ROOT / name)
    if name not in changed:
        assert digest(current) == meta['sha256'], name
assert {str(p.relative_to(ROOT)) for p in (ROOT / 'garden').rglob('*') if p.is_file()} == {n for n in before if n.startswith('garden/')}
new_sections = {}
for name, start, end in [
    ('rooms/what-the-gaps-can-say.md', '## Count the kept visits before sending another request — 2026-10-19', '## Sources'),
    ('rooms/measuring-the-window.md', '## Eight looks are still not eight fault lifetimes — 2026-10-19', 'Links:'),
    ('words/latency-by-outcome.md', '## Count the comparison, not every reply — 2026-10-19', 'Links:'),
]:
    text = read(ROOT / name).decode()
    left, rest = text.split(start, 1)
    section, right = rest.split(end, 1)
    reconstructed = left + end + right
    if name.startswith('words/'):
        reconstructed = reconstructed.replace('Links: [[unit-of-analysis]] · [[independence]] · ', 'Links: ', 1)
    assert digest(reconstructed.encode()) == before[name]['sha256'], name
    new_sections[name] = start + section
    lines = text.splitlines()
    assert lines[0] == '# ' + Path(name).stem
    if name.startswith('rooms/'):
        assert lines[2].startswith('*') and lines[2].endswith('*')
        assert lines[4] and not lines[4].startswith(('#', '*'))
    else:
        assert lines[2] and text.rstrip().splitlines()[-1].startswith('Links:')

gate = read(ROOT / 'gate.md').decode()
base_gate = subprocess.run(['git', 'show', 'HEAD:gate.md'], cwd=ROOT, check=True, capture_output=True).stdout
assert digest(base_gate) == before['gate.md']['sha256']
old_lines, new_lines = base_gate.decode().splitlines(), gate.splitlines()
assert len(old_lines) == len(new_lines)
differing = [(old, new) for old, new in zip(old_lines, new_lines) if old != new]
assert len(differing) == 3
allowed_prefixes = ('> rooms:', '- [measuring-the-window]', '- [what-the-gaps-can-say]')
assert all(any(a.startswith(p) and b.startswith(p) for p in allowed_prefixes) for a, b in differing)
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/]+)\.md\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(entries) == len(set(entries)) == 697 and set(entries) == rooms
assert len([line for line in read(ROOT / 'questions.md').decode().splitlines() if line.startswith('- [ ] ')]) == 16
assert not any(line.startswith('- ') for line in read(ROOT / 'courtyard.md').decode().splitlines())

# Cross-check table/row values in the prose against the executed analysis.
receipt = read(OUT / 'README.md').decode()
room = read(ROOT / 'rooms/what-the-gaps-can-say.md').decode()
assert [cell['visits'] for cell in analysis['table']] == [1, 5, 1, 1]
assert '| Changed | 1 | 5 | 6 |' in room and '| No detected change | 1 | 1 | 2 |' in room
for row in analysis['rows']:
    line = next(line for line in receipt.splitlines() if line.startswith('| [%d]' % row['visit']))
    times = ' / '.join(row['orgmode_time_total_seconds'])
    assert times in line and ('| yes |' if row['changed_advertised_map'] else '| no |') in line
    assert str(row['collection_span_seconds']) in line
    assert row['start_utc'].replace('T', ' ').replace('+00:00', '') in line
assert analysis['visit_count'] == 8 and analysis['request_count'] == 48
assert analysis['http_status_counts'] == {'200': 16, '500': 32}
assert all(v['visits'] == 2 and v['orgmode_requests'] == 4 for v in analysis['utc_bands'].values())
assert [v['visits_at_least_1s'] for v in analysis['utc_bands'].values()] == [1, 0, 0, 1]

# Check the newly added local links; old dangling invitations are out of scope.
new_sections[str((OUT / 'README.md').relative_to(ROOT))] = receipt
link_count = 0
for name, text in new_sections.items():
    parent = (ROOT / name).parent
    for target in re.findall(r'(?<!!)\[[^\[\]\n]+\]\(([^)\s]+)\)', text):
        if target.startswith(('https://', 'http://', '#')):
            continue
        target = target.split('#', 1)[0]
        assert (parent / target).resolve().is_file(), (name, target)
        link_count += 1
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
        target = target.split('#', 1)[0]
        assert any((base / (target + '.md')).is_file() for base in (ROOT, ROOT / 'rooms', ROOT / 'words')), (name, target)
        link_count += 1

chronicle = read(ROOT / 'chronicle.md')
size = before['chronicle.md']['bytes']
assert digest(chronicle[:size]) == before['chronicle.md']['sha256']
addition = chronicle[size:].decode()
assert re.fullmatch(r'- 2026-10-19 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', addition)
assert len(chronicle.splitlines()) == before['chronicle.md']['lines'] + 1

# No tracked mutation outside our named files and the pre-existing heartbeat.
tracked = subprocess.run(['git', 'diff', '--name-only'], cwd=ROOT, check=True, capture_output=True, text=True).stdout.splitlines()
assert set(tracked) <= changed | {'.heartbeat'}, tracked
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
result = dict(verified_utc=datetime.now(timezone.utc).isoformat(), result='PASS', same_session_not_independent_review=True, input_hashes=len(analysis['input_sha256']), saved_requests=48, compared_visits=8, table=[1, 5, 1, 1], source_fetches_checked=4, new_local_links_checked=link_count, map_rooms=697, map_duplicates=0, open_questions=16, questions_courtyard_quests_unchanged=True, garden_unchanged=True, prior_prose_preserved=True, chronicle_lines_appended=1, chronicle_line=addition.rstrip(), git_diff_check='PASS')
(OUT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
