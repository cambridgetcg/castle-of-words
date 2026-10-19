"""Independent extraction within this session, plus scope and prose checks. No network."""
from collections import Counter
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import subprocess
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
closed = '--closed' in sys.argv

def safe(path):
    assert ROOT in path.resolve().parents, path
    return path

def digest(data): return sha256(data).hexdigest()
def text(path): return safe(path).read_text()
def load(path): return json.loads(text(path))

before = load(OUT/'before.json')
analysis = load(OUT/'analysis.json')
checks = {}
for name, expected in analysis['input_sha256'].items():
    assert digest(safe(ROOT/name).read_bytes()) == expected, name
checks['input_hashes'] = len(analysis['input_sha256'])
sources = load(OUT/'sources.json')
for source in sources:
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert digest(safe(OUT/source['file']).read_bytes()) == source['sha256']
    assert urlparse(source['url']).hostname in {'search.brave.com','www.rfc-editor.org','raw.githubusercontent.com','www.itl.nist.gov'}
checks['public_sources'] = len(sources)

# A separate extraction for these fixed captures; no reuse of analyze.py's packet parser.
def refs(path):
    body = safe(path).read_bytes()
    pairs = re.findall(rb'([0-9a-f]{40}) (HEAD|refs/heads/master)(?=\x00|\n)', body)
    assert len(pairs) == 2 and len(dict((name, oid) for oid, name in pairs)) == 2
    return {name: oid for oid, name in pairs}

def exact_gap(start, finish):
    delta = datetime.fromisoformat(finish)-datetime.fromisoformat(start)
    return Fraction(delta.days*86400+delta.seconds) + Fraction(delta.microseconds,1000000)

counts = {key: Counter() for key in analysis['tables']}
changed_labels = 0
selected = sorted(p for p in (ROOT/'evidence').glob('gardener-2026-10-1*-service-check*')
                  if p.is_dir() and re.fullmatch(r'gardener-2026-10-(17|18)-service-check(?:-[0-9]+)?',p.name))
assert {str(p.relative_to(ROOT)) for p in selected} == {r['directory'] for r in analysis['rows']}
for directory in selected:
    first = load(directory/'r1-orgmode.json')
    second = load(directory/'r2-orgmode.json')
    comparison = next(c for c in load(directory/'comparison.json')['comparisons'] if c['id']=='r1-orgmode')
    pointer = comparison.get('previous_complete_capture',comparison.get('previous_capture'))
    assert pointer is not None
    different = refs(directory/'r1-orgmode.body') != refs((ROOT/pointer).with_suffix('.body'))
    label = 'changed' if different else 'no_detected_change'
    a, b = [Fraction(r['curl_metrics']['time_total']) for r in (first,second)]
    for key, value in [('first_wait',a),('second_wait',b),('either_wait',max(a,b))]:
        counts[key][label, 'ge_1s' if value>=1 else 'lt_1s'] += 1
    complete = second['curl_exit']==0
    outcome = 'missing_timeout' if not complete else ('completed_ge_1s' if b>=1 else 'completed_lt_1s')
    counts['second_response_outcome'][label,outcome] += 1
    if complete:
        assert safe(directory/'r2-orgmode.body').read_bytes() == safe(directory/'r1-orgmode.body').read_bytes()
        within = refs(directory/'r2-orgmode.body') != refs(directory/'r1-orgmode.body')
        counts['within_visit_view'][label,'changed' if within else 'no_detected_change'] += 1
    else:
        assert second['curl_exit']==28 and not (directory/'r2-orgmode.body').exists()
        within = None
        counts['within_visit_view'][label,'missing_timeout'] += 1
    changed_labels += (a>=1)!=(max(a,b)>=1)
    row = next(r for r in analysis['rows'] if r['directory']==str(directory.relative_to(ROOT)))
    assert row['first_view_changed']==different and row['within_visit_view_changed']==within
    assert Fraction(row['first_finish_to_second_start_seconds'])==exact_gap(first['finish_utc'],second['start_utc'])
    prior = load(ROOT/pointer)
    assert Fraction(row['previous_finish_to_first_start_seconds'])==exact_gap(prior['finish_utc'],first['start_utc'])
for key, table in analysis['tables'].items():
    for label, outcomes in table.items():
        for outcome, count in outcomes.items():
            assert counts[key][label,outcome] == count, (key,label,outcome)
    assert sum(counts[key].values()) == 14
assert changed_labels == analysis['labels_changed_by_using_first_wait_only'] == 3
assert analysis['visits']==len(selected)==14 and analysis['orgmode_attempts']==28
assert analysis['completed_first_responses']==14 and analysis['completed_second_responses']==13
assert analysis['changed_first_views']==10
checks['separate_fraction_recount'] = True
checks['all_completed_recheck_bodies_match_first'] = 13
checks['changed_timing_labels'] = changed_labels

for name, old in before['files'].items():
    if name in ('gate.md','chronicle.md','rooms/what-the-gaps-can-say.md'): continue
    assert digest(safe(ROOT/name).read_bytes()) == old['sha256'], name
assert {str(p.relative_to(ROOT)) for p in (ROOT/'garden').rglob('*') if p.is_file()} == {n for n in before['files'] if n.startswith('garden/')}
assert not any(s.startswith('- ') for s in text(ROOT/'courtyard.md').splitlines())
assert sum(s.startswith('- [ ]') for s in text(ROOT/'questions.md').splitlines())==16
checks['questions_quests_courtyard_and_garden_unchanged'] = True

room = text(ROOT/'rooms/what-the-gaps-can-say.md')
heading = '## Keep the first look beside its own wait — 2026-10-19\n'
assert room.count(heading)==1
start = room.index(heading); end = room.index('## Sources\n',start)
addition = room[start:end]
assert digest((room[:start]+room[end:]).encode()) == before['files']['rooms/what-the-gaps-can-say.md']['sha256']
assert room.startswith('# what-the-gaps-can-say\n\n*')
assert room.splitlines()[2].endswith('*')
checks['older_room_prose_preserved'] = True

gate = text(ROOT/'gate.md')
map_text = gate.split('## Map\n',1)[1].split('\n## ',1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/]+)\.md\) — .+$',map_text,re.M)
room_names = {p.stem for p in (ROOT/'rooms').glob('*.md')}
assert set(entries)==room_names and len(entries)==len(set(entries))==697
assert sorted(p.name for p in (ROOT/'rooms').glob('*.md'))==before['rooms']
restored = gate
for key, old in before['old_gate_lines'].items():
    matches = [s for s in restored.splitlines() if s.startswith(key)]
    assert len(matches)==1
    restored = restored.replace(matches[0],old,1)
assert digest(restored.encode())==before['files']['gate.md']['sha256']
checks['map_rooms_once_each'] = len(entries)
checks['gate_archive_preserved'] = True

word = text(ROOT/'words/temporal-alignment.md')
assert word.startswith('# temporal-alignment\n\nTemporal alignment means ')
assert word.splitlines()[-1].startswith('Links: ')
assert sorted(p.name for p in (ROOT/'words').glob('*.md')) == sorted(before['words']+['temporal-alignment.md'])
link_count = 0
for content in (word,addition):
    for target in re.findall(r'\[\[([^\]]+)\]\]',content):
        target = target.split('|',1)[0].split('#',1)[0]
        assert any(safe(ROOT/f'{folder}/{target}.md').exists() for folder in ('words','rooms')),target
        link_count += 1
    assert 'uncertain:' in content and '2026-10-19' in content
checks['new_wikilinks_resolve'] = link_count
checks['new_word_shape'] = True
for label in ('changed','no_detected_change'):
    cells = [f"{analysis['tables'][key][label]['ge_1s']} / {analysis['tables'][key][label]['lt_1s']}" for key in ('first_wait','second_wait','either_wait')]
    title = 'Changed' if label=='changed' else 'No detected change'
    assert '| '+title+' | '+' | '.join(cells)+' |' in addition
checks['written_table_matches_output'] = True

chronicle = safe(ROOT/'chronicle.md').read_bytes()
old = before['files']['chronicle.md']
assert digest(chronicle[:old['bytes']])==old['sha256']
extra = chronicle[old['bytes']:].decode()
if closed:
    assert re.fullmatch(r'- 2026-10-19 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — Separating first looks from later waits changed three timing labels without revealing when the hidden updates happened\.\n',extra),repr(extra)
    checks['exactly_one_chronicle_line_appended'] = True
else:
    assert extra==''
    checks['chronicle_still_unmodified'] = True

proc = subprocess.run(['git','--no-optional-locks','diff','--check'],cwd=ROOT,capture_output=True,text=True)
assert proc.returncode==0,proc.stdout+proc.stderr
checks['git_diff_check'] = 'PASS'
result = {'status':'PASS','closed':closed,'checks':checks,'limits':'Same-session verification, not distinct-session review or independent authentication of service history.'}
(OUT/('verification.json' if closed else 'preflight.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
