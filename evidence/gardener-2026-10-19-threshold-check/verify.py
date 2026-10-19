"""Separate offline checks of the calculation and this visit's edit boundaries."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent

def data(relative):
    p = (ROOT / relative).resolve()
    assert ROOT in p.parents
    return p.read_bytes()

def text(relative):
    return data(relative).decode('utf-8')

def load(relative):
    return json.loads(data(relative))

analysis = json.loads((OUT / 'analysis.json').read_text())
before = json.loads((OUT / 'before.json').read_text())
for path, digest in analysis['input_sha256'].items():
    assert sha256(data(path)).hexdigest() == digest, path
rows = []
for row in analysis['rows']:
    records = [load(row['directory'] + f'/r{r}-orgmode.json') for r in (1, 2)]
    waits = [Fraction(r['curl_metrics']['time_total']) for r in records]
    assert max(waits) == Fraction(row['maximum_seconds'])
    body = data(row['directory'] + '/r1-orgmode.body')
    old = load('evidence/gardener-2026-10-19-saved-comparison/analysis.json')['rows'][row['visit']-1]
    prior_body = data(str(Path(old['previous_complete_capture']).with_suffix('.body')))
    # A second limited check for these fixtures: both advertised names have one ID.
    pattern = rb'([a-f0-9]{40}) (HEAD|refs/heads/master)(?=[\x00\n])'
    current_refs = {name: oid for oid, name in re.findall(pattern, body)}
    prior_refs = {name: oid for oid, name in re.findall(pattern, prior_body)}
    assert set(current_refs) == set(prior_refs) == {b'HEAD', b'refs/heads/master'}
    changed = current_refs != prior_refs
    assert changed == row['changed']
    rows.append((row['visit'], changed, max(waits)))

def counts(t):
    c = Counter((changed, maximum >= t) for _, changed, maximum in rows)
    return [c[True,True], c[True,False], c[False,True], c[False,False]]

def labels(t):
    return [i for i, _, maximum in rows if maximum >= t]

for table in analysis['selected_thresholds']:
    assert counts(Fraction(table['threshold_seconds'])) == table['cells']
levels = sorted({r[2] for r in rows})
regimes = analysis['all_positive_threshold_regimes']
assert len(regimes) == len(levels)+1
for i, regime in enumerate(regimes):
    lower = Fraction(regime['lower_exclusive_seconds'])
    assert lower == (levels[i-1] if i else 0)
    if regime['upper_inclusive_seconds'] is None:
        assert i == len(levels)
        test_points = [lower+1, lower+100]
    else:
        upper = Fraction(regime['upper_inclusive_seconds'])
        assert upper == levels[i] and lower < upper
        test_points = [upper, (lower+upper)/2]
    for point in test_points:
        assert counts(point) == regime['cells']
stable = analysis['same_labels_as_1s']
lower, upper = Fraction(stable['lower_exclusive_seconds']), Fraction(stable['upper_inclusive_seconds'])
assert labels(Fraction(1)) == labels((lower+upper)/2) == labels(upper)
assert labels(lower) != labels(Fraction(1)) != labels(upper+Fraction(1,10**9))

# Input prose and machinery not touched by this visit.
changed_paths = {'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md'}
for path, entry in before['files'].items():
    if path not in changed_paths:
        assert sha256(data(path)).hexdigest() == entry['sha256'], path
current_garden = {str(p.relative_to(ROOT)) for p in (ROOT / 'garden').rglob('*') if p.is_file()}
assert current_garden == {p for p in before['files'] if p.startswith('garden/')}
questions = [line for line in text('questions.md').splitlines() if line.startswith('- [ ] ')]
reserved = [line for line in questions if re.search(r'commission|waits for: yu|yu decides|needs yu|being grown', line)]
assert len(questions) == 16 and len(reserved) == 13
assert not any(line.startswith('- ') for line in text('courtyard.md').splitlines())
assert sorted(p.name for p in (ROOT / 'rooms').glob('*.md')) == before['rooms']
assert set(p.name for p in (ROOT / 'words').glob('*.md')) - set(before['words']) == {'threshold-sensitivity.md'}
assert set(before['words']) <= {p.name for p in (ROOT / 'words').glob('*.md')}

room = text('rooms/what-the-gaps-can-say.md')
pattern = r'\n## Move the line without moving the observations — 2026-10-19\n.*?(?=\n## Sources\n)'
blocks = re.findall(pattern, room, flags=re.S)
assert len(blocks) == 1
restored_room = re.sub(pattern, '', room, flags=re.S)
assert sha256(restored_room.encode()).hexdigest() == before['files']['rooms/what-the-gaps-can-say.md']['sha256']
for table in analysis['selected_thresholds']:
    a,b,c,d = table['cells']
    assert f"| {table['threshold_seconds']} | {a} / {b} | {c} / {d} |" in blocks[0]
assert 'Question 740 remains open' in blocks[0]

old_glance = '> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-19 (all 697 rooms listed once in the Map; an [offline comparison of eight saved visits](evidence/gardener-2026-10-19-saved-comparison/README.md) found all four combinations of changed/unchanged advertised maps and shorter/longer orgmode waits; three questions researched, all still open, none planted, no new service probes or watch)'
old_map = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — an eight-visit comparison keeps changed and unchanged Git views beside their waits, without turning snapshots into an update schedule or a cause (updated 2026-10-19)'
gate = text('gate.md')
new_glance = next(line for line in gate.splitlines() if line.startswith('> rooms:'))
new_map = next(line for line in gate.splitlines() if line.startswith('- [what-the-gaps-can-say]'))
restored_gate = gate.replace(new_glance, old_glance, 1).replace(new_map, old_map, 1)
assert sha256(restored_gate.encode()).hexdigest() == before['files']['gate.md']['sha256']
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/]+)\.md\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(entries) == len(set(entries)) == len(rooms) == 697 and set(entries) == rooms

word = text('words/threshold-sensitivity.md')
assert word.startswith('# threshold-sensitivity\n\nThreshold sensitivity asks whether moving a dividing line changes the answer.')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
link_count = 0
for location, content in [('rooms/what-the-gaps-can-say.md', blocks[0]), ('words/threshold-sensitivity.md', word), (str(OUT.relative_to(ROOT) / 'README.md'), (OUT / 'README.md').read_text())]:
    for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]+)?\]\]', content):
        assert any((ROOT / folder / (target + '.md')).is_file() for folder in ('rooms', 'words', '')), target
        link_count += 1
    for target in re.findall(r'(?<!!)\[[^]\n]*\]\(([^)]+)\)', content):
        if re.match(r'https?://', target) or target.startswith('#'):
            continue
        destination = (ROOT / location).parent / target.split('#', 1)[0]
        assert ROOT in destination.resolve().parents and destination.is_file(), target
        link_count += 1
for item in json.loads((OUT / 'sources.json').read_text()):
    assert sha256((OUT / item['file']).read_bytes()).hexdigest() == item['sha256']

chron = data('chronicle.md')
old_size = before['files']['chronicle.md']['bytes']
assert sha256(chron[:old_size]).hexdigest() == before['files']['chronicle.md']['sha256']
extra = chron[old_size:].decode('utf-8')
assert len(extra.splitlines()) == 1, repr(extra)
assert re.fullmatch(r'- 2026-10-19 \d\d:\d\d · visit: filed 0, researched 1, planted 0 — [^\n]+\n', extra)
diff_check = subprocess.run(['git', 'diff', '--check'], cwd=ROOT, capture_output=True, text=True)
assert diff_check.returncode == 0, diff_check.stdout + diff_check.stderr
report = {'result': 'PASS', 'verified_utc': datetime.now(timezone.utc).isoformat(), 'input_hashes_checked': len(analysis['input_sha256']), 'visits': len(rows), 'threshold_regimes_verified': len(regimes), 'table_recomputed_with': 'fractions.Fraction from saved per-request records', 'map_rooms_listed_once': len(entries), 'open_questions': len(questions), 'reserved_questions': len(reserved), 'new_word': 'threshold-sensitivity', 'new_links_checked': link_count, 'unchanged': ['courtyard.md','questions.md','quests.md','garden/'], 'prior_room_and_gate_prose_preserved': True, 'chronicle_lines_appended': 1, 'git_diff_check': 'PASS', 'review_scope': 'same session; no independent reviewer'}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
