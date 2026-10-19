"""Separate recount and document checks; no imports from the calculation script."""
from collections import Counter
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent

def get(relative):
    p = (ROOT/relative).resolve()
    assert ROOT in p.parents
    return p.read_bytes()

def load(relative): return json.loads(get(relative))

before = json.loads((OUT/'before.json').read_text())
a = json.loads((OUT/'analysis.json').read_text())
for name, digest in a['input_sha256'].items():
    assert sha256(get(name)).hexdigest() == digest, name
for source in json.loads((OUT/'sources.json').read_text()):
    b = (OUT/source['file']).read_bytes()
    assert sha256(b).hexdigest() == source['sha256'] and len(b) == source['bytes']
    assert source['http_status'] == '200' and source['curl_exit'] == 0

# The analysis has already validated packet framing. This path extracts the
# two explicitly scoped reference records independently of its packet parser.
def raw_map(path):
    rec = load(path)
    if rec['curl_exit'] != 0:
        assert rec['curl_exit'] == 28 and not rec['body_present']
        return rec, None
    body = get(Path(path).with_suffix('.body'))
    assert len(body) == rec['body_bytes'] and sha256(body).hexdigest() == rec['body_sha256']
    pairs = re.findall(rb'([0-9a-f]{40}) (HEAD|refs/heads/master)(?=\x00|\n)', body)
    assert len(pairs) == 2
    return rec, dict((name.decode(), oid.decode()) for oid, name in pairs)

def cell(stamp):
    d = datetime.fromisoformat(stamp)
    offset = d.utcoffset()
    assert offset is not None and offset.total_seconds() == 0
    minute = d.hour*60 + d.minute
    return next(i for i, (lo, hi) in enumerate(((0,360),(360,720),(720,1080),(1080,1440))) if lo <= minute < hi)

counts = [Counter() for _ in range(4)]
late_wait_visits = []; failed_visits = []
for row in a['rows']:
    directory = Path(row['directory'])
    prior, pm = raw_map(row['previous_complete_capture'])
    first, fm = raw_map(directory/'r1-orgmode.json')
    second, sm = raw_map(directory/'r2-orgmode.json')
    changed = pm != fm
    assert changed == row['changed'] and fm is not None
    assert sm is None or sm == fm
    i, j = cell(first['start_utc']), cell(second['start_utc'])
    # Six-hour epoch blocks give an independent crossing check for these
    # modern UTC stamps, rather than reusing the analysis's boundary loop.
    cross = int(datetime.fromisoformat(first['start_utc']).timestamp() // 21600) != int(datetime.fromisoformat(prior['finish_utc']).timestamp() // 21600)
    assert cross == bool(row['completed_view_gap_crossed_boundaries_utc'])
    counts[i]['first_views'] += 1
    counts[i]['changed' if changed else 'no_detected_change'] += 1
    first_long = Fraction(first['curl_metrics']['time_total']) >= 1
    counts[i]['first_wait_ge_1s'] += int(first_long)
    counts[i]['changed_cross_bin_gap'] += int(changed and cross)
    counts[i]['all_cross_bin_gaps'] += int(cross)
    counts[j]['rechecks'] += 1
    counts[j]['completed_recheck_ge_1s'] += int(sm is not None and Fraction(second['curl_metrics']['time_total']) >= 1)
    counts[j]['timeout_recheck'] += int(sm is None)
    if first_long: late_wait_visits.append(row['directory'])
    if sm is None: failed_visits.append(row['directory'])
for row, counted in zip(a['table'], counts):
    for key, value in row.items():
        if key != 'utc_bin': assert counted[key] == value, (key, counted, row)
assert len(late_wait_visits) == len(failed_visits) == 1 and late_wait_visits != failed_visits
for key, value in a['totals'].items(): assert sum(c[key] for c in counts) == value

for name in ('courtyard.md','questions.md','quests.md'):
    assert get(name).decode() == before['files'][name]['text'], name
questions = get('questions.md').decode().splitlines()
opens = [(i,s) for i,s in enumerate(questions,1) if s.startswith('- [ ]')]
eligible = [i for i,s in opens if not re.search(r'commissioned|waits for: commission|waits for: yu|yu decides|being grown|needs yu', s, re.I)]
assert len(opens) == 16 and eligible == [740,744,766]
assert not any(s.startswith('- ') for s in get('courtyard.md').decode().splitlines())

room = get('rooms/what-the-gaps-can-say.md').decode()
marker = '## Put the clock on the count — 2026-10-19\n\n'
prefix, rest = room.split(marker)
section, suffix = rest.split('## Sources\n', 1)
assert prefix + '## Sources\n' + suffix == before['files']['rooms/what-the-gaps-can-say.md']['text']
assert room.startswith('# what-the-gaps-can-say\n\n*')
for row in a['table']:
    line = f"| {row['utc_bin']} | {row['first_views']} | {row['changed']} / {row['no_detected_change']} | {row['first_wait_ge_1s']} | {row['rechecks']} | {row['completed_recheck_ge_1s']} | {row['timeout_recheck']} |"
    assert line in section, line
word = get('words/time-bin.md').decode()
assert before['files']['words/time-bin.md'] is None
assert word.startswith('# time-bin\n\nA time bin is a named stretch of the clock')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]', section + word):
    assert any((ROOT/folder/(target+'.md')).exists() for folder in ('rooms','words','')), target
for link in re.findall(r'\]\(([^)]+)\)', section):
    if not link.startswith(('http:','https:')):
        target = (ROOT/'rooms'/link).resolve()
        assert ROOT in target.parents and target.exists(), link

gate = get('gate.md').decode()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/)]+\.md)\) — [^\n]+$', map_text, re.M)
rooms = sorted(p.name for p in (ROOT/'rooms').glob('*.md'))
assert len(entries) == len(set(entries)) and sorted(entries) == rooms
assert rooms == before['rooms']
old_lines = before['files']['gate.md']['text'].splitlines()
new_lines = gate.splitlines()
assert len(old_lines) == len(new_lines)
changes = [(x,y) for x,y in zip(old_lines,new_lines) if x != y]
assert len(changes) == 1 and all(x.startswith('- [what-the-gaps-can-say]') for x in changes[0])
for name, digest in before['garden_sha256'].items(): assert sha256(get(name)).hexdigest() == digest
assert sorted(str(p.relative_to(ROOT)) for p in (ROOT/'garden').rglob('*') if p.is_file()) == sorted(before['garden_sha256'])

chronicle = get('chronicle.md').decode()
old_chronicle = before['files']['chronicle.md']['text']
if '--closed' in sys.argv:
    assert chronicle.startswith(old_chronicle)
    appended = chronicle[len(old_chronicle):].strip().splitlines()
    assert len(appended) == 1
    assert re.fullmatch(r'- 2026-10-19 \d{2}:\d{2} · visit: filed 0, researched 2, planted 0 — .+', appended[0])
else:
    assert chronicle == old_chronicle

result = dict(passed=True, closed='--closed' in sys.argv, researched=2, open_questions=len(opens), eligible_questions=eligible, mapped_rooms=len(rooms), verified_inputs=len(a['input_sha256']), checked_public_sources=3, garden_unchanged=True, prior_prose_preserved=True, separate_recount_agrees=True)
(OUT/('verification.json' if result['closed'] else 'preflight.json')).write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
