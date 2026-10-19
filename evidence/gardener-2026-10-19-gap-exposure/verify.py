"""Separate fraction-based recomputation and bounded-edit checks; no network calls."""
from collections import Counter
from datetime import datetime
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from statistics import median
import json
import re
import subprocess
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent

def read(name):
    p = (ROOT/name).resolve()
    assert ROOT in p.parents
    return p.read_bytes()

def load(name): return json.loads(read(name))

def seconds(a, b):
    x = datetime.fromisoformat(b)-datetime.fromisoformat(a)
    return F(x.days*86400+x.seconds) + F(x.microseconds, 1000000)

def refs(record_path):
    rec = load(record_path)
    assert rec['curl_exit'] == 0 and rec['curl_metrics']['http_code'] == '200'
    data = read(str(Path(record_path).with_suffix('.body')))
    assert sha256(data).hexdigest() == rec['body_sha256'] and len(data) == rec['body_bytes']
    # Deliberately separate from the analysis packet parser; two expected records only.
    found = re.findall(rb'([0-9a-f]{40}) (HEAD|refs/heads/master)(?=\x00|\n)', data)
    assert len(found) == 2 and {name for oid,name in found} == {b'HEAD', b'refs/heads/master'}
    return rec, dict((name,oid) for oid,name in found)

before = json.loads((OUT/'before.json').read_text())
a = json.loads((OUT/'analysis.json').read_text())
for name, expected in a['input_sha256'].items(): assert sha256(read(name)).hexdigest() == expected, name
sources = json.loads((OUT/'sources.json').read_text())
for source in sources:
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert sha256((OUT/source['file']).read_bytes()).hexdigest() == source['sha256']
    assert 'yhetil.' not in source['url'] and 'lore.kernel.org' not in source['url']
assert len(sources) == 4

values = {'changed': [], 'no_detected_change': [], 'all': []}
interrupted = []
for row in a['rows']:
    p, pv = refs(row['previous_complete_capture'])
    q, qv = refs(row['directory']+'/r1-orgmode.json')
    difference = pv != qv
    assert difference == row['first_view_changed']
    assert p['finish_utc'] == row['previous_finish_utc'] and q['start_utc'] == row['first_start_utc']
    gap = seconds(p['finish_utc'], q['start_utc'])
    assert gap == F(row['previous_finish_to_first_start_seconds'])
    values['changed' if difference else 'no_detected_change'].append(gap)
    values['all'].append(gap)
    if row['intervening_timeout_in_selected_series']:
        timeout_path = str(Path(row['previous_complete_capture']).with_name('r2-orgmode.json'))
        t = load(timeout_path)
        assert t['curl_exit'] == 28 and not t['body_present'] and t['body_sha256'] is None
        assert not (ROOT/timeout_path).with_suffix('.body').exists()
        assert t['finish_utc'] == row['last_attempt_finish_utc']
        short_gap = seconds(t['finish_utc'], q['start_utc'])
        assert short_gap == F(row['last_attempt_finish_to_first_start_seconds'])
        assert gap-short_gap == F('128.781537')
        interrupted.append(row)
assert len(interrupted) == 1
assert len(values['all']) == 14 and len(values['changed']) == 10 and len(values['no_detected_change']) == 4
for group,v in values.items():
    s=a['summary'][group]
    assert s['comparisons'] == len(v)
    for name, actual in [('min',min(v)),('median',median(v)),('max',max(v)),('total',sum(v))]:
        assert F(s[name+'_seconds']) == actual
        assert abs(F(s[name+'_hours'])-actual/3600) < F(1,10**23)
assert max(values['all']) == F('23171.193229') and not a['longest_gap']['first_view_changed']

for name in ('courtyard.md', 'questions.md', 'quests.md'):
    assert sha256(read(name)).hexdigest() == before['files'][name]['sha256'], name
questions = read('questions.md').decode().splitlines()
assert sum(s.startswith('- [ ]') for s in questions) == 16
eligible=[n for n,s in enumerate(questions,1) if s.startswith('- [ ]') and not re.search(r'commissioned|waits for: commission|waits for: yu|yu decides|needs yu|being grown',s,re.I)]
assert eligible == [740,744,766]
assert not any(s.startswith('- ') for s in read('courtyard.md').decode().splitlines())
assert sum(s.startswith('- [ ]') for s in read('quests.md').decode().splitlines()) == 8

current_garden = {}
for p in (ROOT/'garden').rglob('*'):
    if p.is_file():
        assert ROOT in p.resolve().parents
        current_garden[str(p.relative_to(ROOT))] = sha256(p.read_bytes()).hexdigest()
assert current_garden == before['garden_sha256']
rooms = sorted(p.name for p in (ROOT/'rooms').glob('*.md'))
words = sorted(p.name for p in (ROOT/'words').glob('*.md'))
assert rooms == before['rooms'] and words == before['words']
gate = read('gate.md').decode()
maptext = gate.split('## Map',1)[1].split('\n## ',1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^\)]+\.md)\)',maptext,re.M)
assert len(entries) == len(rooms) == 697 and Counter(entries) == Counter(rooms)
def omit_updated_lines(text):
    return '\n'.join(s for s in text.splitlines() if not s.startswith('> rooms:') and not s.startswith('- [what-the-gaps-can-say]'))
assert omit_updated_lines(gate) == omit_updated_lines(before['files']['gate.md']['text'])

room = read('rooms/what-the-gaps-can-say.md').decode()
heading = '## Put the length of the blank beside the view — 2026-10-19\n'
assert room.count(heading) == 1
left,section = room.split(heading,1)
addition,right = section.split('## Sources\n',1)
assert left+'## Sources\n'+right == before['files']['rooms/what-the-gaps-can-say.md']['text']
nonempty=[s for s in room.splitlines() if s.strip()]
assert nonempty[0] == '# what-the-gaps-can-say' and nonempty[1].startswith('*') and nonempty[1].endswith('*')
assert nonempty[2].startswith('This room gathers')
new_text = heading+addition
for name in ('detection-exposure','observation-gap'):
    path='words/'+name+'.md'
    text=read(path).decode()
    old=before['files'][path]['text']
    assert text.startswith(old.split('Links:',1)[0])
    lines=[s for s in text.splitlines() if s.strip()]
    assert lines[0] == '# '+name and not lines[1].startswith(('#','*','Links:'))
    assert lines[-1].startswith('Links:')
    new_text += '\n'+text[len(old.split('Links:',1)[0]):]
links=set(re.findall(r'\[\[([^\]|#]+)',new_text))
for name in links:
    assert any((ROOT/folder/(name+'.md')).exists() for folder in ('rooms','words','')),name
for text,base in [(heading+addition,ROOT/'rooms'),(read('words/detection-exposure.md').decode(),ROOT/'words'),(read('words/observation-gap.md').decode(),ROOT/'words'),((OUT/'README.md').read_text(),OUT)]:
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
        if '://' not in target and target not in ('preflight.json','verification.json'):
            p=(base/target.split('#',1)[0]).resolve()
            assert ROOT in p.parents and p.exists(),str(p)
assert '| Changed | 10 | 3.162 | 3.199 | 3.288 |' in new_text
assert '| No detected change | 4 | 3.180 | 3.228 | 6.436 |' in new_text
assert '128.781537' in new_text and '**740 remains open.**' in new_text

closed = '--closed' in sys.argv
chronicle=read('chronicle.md').decode()
prior=before['files']['chronicle.md']['text']
assert chronicle.startswith(prior)
appended=chronicle[len(prior):].splitlines()
if closed:
    assert len(appended)==1
    assert re.fullmatch(r'- 2026-10-19 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — Measuring the gaps behind fourteen saved comparisons kept a failed attempt from becoming a newer view\.',appended[0])
else:
    assert not appended
check=subprocess.run(['git','diff','--check'],cwd=ROOT,capture_output=True,text=True)
assert check.returncode == 0, check.stdout+check.stderr
result=dict(status='PASS',closed=closed,verified_input_hashes=len(a['input_sha256']),public_source_hashes=len(sources),comparisons=len(a['rows']),changed_views=10,no_detected_change=4,interrupted_gaps=len(interrupted),rooms_listed_once=len(entries),resolving_wikilinks=len(links),open_questions=16,open_quests=8,garden_files_unchanged=len(current_garden),prior_prose_preserved=True,chronicle_lines_appended=len(appended),git_diff_check='PASS',limits='Same-session offline verification, not independent service evidence or a clock-accuracy audit.')
(OUT/('verification.json' if closed else 'preflight.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
