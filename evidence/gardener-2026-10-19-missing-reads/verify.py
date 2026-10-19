"""Second calculation and scope checks. No network and no old-file mutations."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
before = json.loads((OUT / 'before.json').read_text())
analysis = json.loads((OUT / 'analysis.json').read_text())
checks = {}

def digest(data): return sha256(data).hexdigest()
def safe(path):
    path = path.resolve()
    assert ROOT in path.parents
    return path

for name, expected in analysis['input_sha256'].items():
    assert digest(safe(ROOT / name).read_bytes()) == expected, name
checks['input_hashes'] = len(analysis['input_sha256'])

sources = json.loads((OUT / 'sources.json').read_text())
for source in sources:
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert digest(safe(OUT / source['file']).read_bytes()) == source['sha256']
checks['fetched_sources'] = len(sources)

# Separate, simple extraction for these fixed two-reference captures, not the
# packet parser used by analyze.py. Classification uses exact rational times.
def map_from_body(path):
    body = safe(path).read_bytes()
    matches = re.findall(rb'([0-9a-f]{40}) (HEAD|refs/heads/master)(?=\x00|\n)', body)
    assert len(matches) == 2
    return {name.decode(): oid.decode() for oid, name in matches}

allwait, complete = Counter(), Counter()
request_count, absent_count, outcome = 0, 0, Counter()
selected = sorted(p for p in (ROOT / 'evidence').glob('gardener-2026-10-1*-service-check*') if p.is_dir() and re.fullmatch(r'gardener-2026-10-(17|18)-service-check(?:-[0-9]+)?', p.name))
assert {str(p.relative_to(ROOT)) for p in selected} == {r['directory'] for r in analysis['rows']}
for path in selected:
    meta = json.loads((path / 'manifest.json').read_text())
    records = meta['records']
    request_count += len(records); absent_count += 6 - len(records)
    comp = json.loads((path / 'comparison.json').read_text())['comparisons'][0]
    pointer = comp.get('previous_complete_capture', comp.get('previous_capture'))
    changed = map_from_body(path / 'r1-orgmode.body') != map_from_body((ROOT / pointer).with_suffix('.body'))
    org = [json.loads((path / (r['id']+'.json')).read_text()) for r in records if r['id'].endswith('orgmode')]
    assert len(org) == 2
    long = max(Fraction(r['curl_metrics']['time_total']) for r in org) >= 1
    key = ('changed' if changed else 'unchanged', 'at_least_one_ge_1s' if long else 'both_below_1s')
    allwait[key] += 1
    if all(r['curl_exit'] == 0 and r['curl_metrics']['http_code'] == '200' for r in org):
        complete[key] += 1
    for r in records:
        outcome[(r['curl_exit'], r['curl_metrics']['http_code'])] += 1
for name, computed in [('complete_response_pair_table', complete), ('all_attempted_client_wait_table', allwait)]:
    for row in analysis[name]: assert computed[row['view'], row['wait_label']] == row['visits']
assert request_count == analysis['attempted_requests'] == 82
assert absent_count == len(analysis['unattempted_slots']) == 2
assert outcome == {(0,'200'):27, (0,'500'):54, (28,'000'):1}
assert sum(complete.values()) == 13 and sum(allwait.values()) == 14
assert complete == {('changed','at_least_one_ge_1s'):1, ('changed','both_below_1s'):8, ('unchanged','at_least_one_ge_1s'):2, ('unchanged','both_below_1s'):2}
assert allwait == {('changed','at_least_one_ge_1s'):2, ('changed','both_below_1s'):8, ('unchanged','at_least_one_ge_1s'):2, ('unchanged','both_below_1s'):2}
checks['separately_recomputed_tables'] = True

for name, old in before['files'].items():
    if name in ('gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md'): continue
    assert digest(safe(ROOT / name).read_bytes()) == old['sha256'], name
assert {str(p.relative_to(ROOT)) for p in (ROOT / 'garden').rglob('*') if p.is_file()} == {n for n in before['files'] if n.startswith('garden/')}
assert len([x for x in (ROOT/'questions.md').read_text().splitlines() if x.startswith('- [ ]')]) == 16
assert not any(x.startswith('- ') for x in (ROOT/'courtyard.md').read_text().splitlines())
checks['unchanged_questions_quests_courtyard_and_garden'] = True

room = (ROOT/'rooms/what-the-gaps-can-say.md').read_text()
start = room.index('## Keep the interrupted visit — 2026-10-19\n')
end = room.index('## Sources\n', start)
addition = room[start:end]
assert digest((room[:start] + room[end:]).encode()) == before['files']['rooms/what-the-gaps-can-say.md']['sha256']
assert room.splitlines()[0] == '# what-the-gaps-can-say'
assert room.splitlines()[2].startswith('*') and room.splitlines()[2].endswith('*')
checks['older_room_prose_preserved'] = True

gate = (ROOT/'gate.md').read_text()
maptext = gate.split('## Map\n',1)[1].split('\n## ',1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/]+)\.md\)',maptext,re.M)
rooms = {p.stem for p in (ROOT/'rooms').glob('*.md')}
assert len(entries) == len(set(entries)) == len(rooms) == 697
assert set(entries) == rooms
assert sorted(p.name for p in (ROOT/'rooms').glob('*.md')) == before['rooms']
checks['map_rooms_once_each'] = len(rooms)

old_glance = '> rooms: **697** · last full recorded knock: **107** (2026-10-09 07:55 UTC) · open doors: **16** · checked 2026-10-19 (all 697 rooms listed once in the Map; an [offline threshold check](evidence/gardener-2026-10-19-threshold-check/README.md) found the same eight-visit labels at one, five and ten seconds, without proving an update–delay relationship; one question researched and still open, none planted, no new service probes or watch)'
old_map = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — eight saved visits keep changed Git views beside their waits; checking different timing cutoffs tests the labels, not an update schedule or a cause (updated 2026-10-19)'
lines = gate.splitlines(keepends=True)
for i,line in enumerate(lines):
    if line.startswith('> rooms: '): lines[i] = old_glance+'\n'
    if line.startswith('- [what-the-gaps-can-say]'): lines[i] = old_map+'\n'
assert digest(''.join(lines).encode()) == before['files']['gate.md']['sha256']
checks['gate_only_current_glance_and_one_summary_changed'] = True

wordpath = ROOT/'words/complete-case-analysis.md'
word = wordpath.read_text()
assert word.startswith('# complete-case-analysis\n\nComplete-case analysis compares only the rows that have every answer the comparison needs.\n')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
assert {p.name for p in (ROOT/'words').glob('*.md')} - set(before['words']) == {'complete-case-analysis.md'}
for text, base in [(addition, ROOT/'rooms'), (word, ROOT/'words'), ((OUT/'README.md').read_text(), OUT)]:
    for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]+)?\]\]',text):
        assert any((ROOT/folder/(target+'.md')).is_file() for folder in ('rooms','words','')), target
    for target in re.findall(r'(?<!!)\[[^]\n]*\]\(([^)\s]+)\)',text):
        if '://' in target or target.startswith('#'): continue
        assert safe(base/target.split('#',1)[0]).is_file(), target
checks['new_word_shape_and_new_links'] = True

chronicle = (ROOT/'chronicle.md').read_bytes()
old = before['files']['chronicle.md']
assert digest(chronicle[:old['bytes']]) == old['sha256']
suffix = chronicle[old['bytes']:].decode()
if '--preflight' in sys.argv:
    assert suffix == ''
    checks['chronicle_ready_for_one_line'] = True
else:
    assert len(suffix.splitlines()) == 1
    assert re.fullmatch(r'- 2026-10-19 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — Keeping an interrupted visit preserved a changed view and a failed wait without inventing the missing answer\.\n',suffix)
    checks['exactly_one_chronicle_line_appended'] = True

proc = subprocess.run(['git','diff','--check'],cwd=ROOT,text=True,capture_output=True)
assert proc.returncode == 0, proc.stdout + proc.stderr
checks['git_diff_check'] = 'PASS'
result = {'status':'PASS', 'phase':'preflight' if '--preflight' in sys.argv else 'final', 'checks':checks}
(OUT/('preflight.json' if '--preflight' in sys.argv else 'verification.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
