"""Verify the dated claim, preservation boundaries and one-line close offline."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
ROOM = 'rooms/what-the-gaps-can-say.md'
HEADING = '## The date on the envelope is not the update time — 2026-10-20'


def read(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    assert ROOT in path.resolve().parents, path
    return path.read_bytes()


def load(path):
    return json.loads(read(path))


def seconds(delta):
    return Fraction((delta.days * 86400 + delta.seconds) * 1000000 + delta.microseconds, 1000000)


before = load(OUT / 'before.json')
analysis = load(OUT / 'analysis.json')
verified = 0
for path, expected in analysis['input_sha256'].items():
    assert sha256(read(path)).hexdigest() == expected, path
    verified += 1
complete = []
missing = 0
for row in analysis['rows']:
    capture = load(row['capture'])
    path = Path(row['capture'])
    raw = read(path.with_suffix('.headers')).decode('ascii')
    dates = re.findall(r'^Date: (.+)\r$', raw, re.M)
    if capture['curl_exit']:
        assert capture['curl_exit'] == 28 and not raw and not dates
        assert all(row[k] is None for k in ['date', 'date_utc', 'date_minus_start_seconds', 'finish_minus_date_seconds'])
        assert not (ROOT / path.with_suffix('.body')).exists()
        missing += 1
        continue
    assert len(dates) == 1 and dates[0] == row['date']
    # Deliberately use strptime instead of the analysis's email date parser.
    date = datetime.strptime(dates[0], '%a, %d %b %Y %H:%M:%S GMT').replace(tzinfo=timezone.utc)
    start = datetime.fromisoformat(capture['start_utc'])
    finish = datetime.fromisoformat(capture['finish_utc'])
    assert date.isoformat() == row['date_utc']
    assert seconds(date - start) == Fraction(row['date_minus_start_seconds'])
    assert seconds(finish - date) == Fraction(row['finish_minus_date_seconds'])
    complete.append((row, date, start, finish))
assert len(analysis['rows']) == 28 and len(complete) == 27 and missing == 1
assert sum(date < start for _, date, start, _ in complete) == 13
assert all(Fraction(-1) < seconds(date-start) < 0 for _,date,start,_ in complete if date < start)
assert sum(start <= date <= finish for _,date,start,finish in complete) == 14
assert not any(date > finish for _,date,_,finish in complete)
assert min(seconds(finish-date) for _,date,_,finish in complete) == Fraction('0.113426')
assert max(seconds(finish-date) for _,date,_,finish in complete) == Fraction('1.073911')
long_rows = [(r,d,s,f) for r,d,s,f in complete if Fraction(r['curl_total_seconds']) >= 1]
assert len(long_rows) == 3
assert all(d == f.replace(microsecond=0) and d != s.replace(microsecond=0) for _,d,s,f in long_rows)

# Protect prior rooms, word files, machinery and the input/queue files.
protected = 0
for path, expected in before['protected_sha256'].items():
    if path != ROOM:
        assert sha256(read(path)).hexdigest() == expected, path
        protected += 1
old_rooms = {p for p in before['protected_sha256'] if p.startswith('rooms/')}
old_words = {p for p in before['protected_sha256'] if p.startswith('words/')}
now_rooms = {str(p.relative_to(ROOT)) for p in (ROOT/'rooms').glob('*.md')}
now_words = {str(p.relative_to(ROOT)) for p in (ROOT/'words').glob('*.md')}
assert now_rooms == old_rooms
assert now_words - old_words == {'words/http-date.md'}
assert not old_words - now_words
room = read(ROOM).decode()
assert room.count(HEADING) == 1
start = room.index(HEADING)
end = room.index('## Sources\n', start)
new_section = room[start:end]
restored = room[:start] + room[end:]
assert sha256(restored.encode()).hexdigest() == before['protected_sha256'][ROOM]
for row, date, begin, finish in long_rows:
    line = '| ' + begin.strftime('%b %d %H:%M:%S.%f') + ' | ' + date.strftime('%b %d %H:%M:%S') + ' | ' + finish.strftime('%b %d %H:%M:%S.%f') + ' | ' + row['curl_total_seconds'] + ' |'
    assert line in new_section, line
assert room.splitlines()[0] == '# what-the-gaps-can-say'
assert room.splitlines()[2].startswith('*') and room.splitlines()[2].endswith('*')
word = read('words/http-date.md').decode()
assert word.startswith('# http-date\n\nAn HTTP date')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
assert 'uncertain:' in word and 'uncertain:' in new_section

# Match the entire Map, not only the edited entry.
gate = read('gate.md').decode()
map_match = re.search(r'^## Map[^\n]*\n(.*?)(?=^## |\Z)', gate, re.M|re.S)
assert map_match
map_lines = re.findall(r'^- \[[^\n]+\]\((rooms/[^)]+\.md)\).*$', map_match[1], re.M)
counts = Counter(map_lines)
assert set(counts) == now_rooms and all(n == 1 for n in counts.values())
new_glance = next(s for s in gate.splitlines() if s.startswith('> rooms:'))
new_map = next(s for s in gate.splitlines() if s.startswith('- [what-the-gaps-can-say]'))
restored_gate = gate.replace(new_glance, before['old_glance'], 1).replace(new_map, before['old_map_line'], 1)
assert sha256(restored_gate.encode()).hexdigest() == before['gate_sha256']
assert '**697**' in new_glance and '**16**' in new_glance
assert before['eligible_question_lines'] == [740, 744, 766] and before['researched_question_lines'] == [740]
assert before['courtyard_entries'] == 0 and before['open_questions'] == 16

# Resolve newly written links. Existing invitation links are not rewritten.
for text, base in [(new_section, ROOT/'rooms'), (word, ROOT/'words'), (read(OUT/'README.md').decode(), OUT)]:
    for target in re.findall(r'\[\[([^\]|#]+)(?:[^\]]*)\]\]', text):
        assert any((ROOT/d/(target+'.md')).exists() for d in ['', 'rooms', 'words']), target
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        resolved = (base/target.split('#')[0]).resolve()
        assert ROOT in resolved.parents and resolved.is_file(), target
for source in load(OUT/'sources.json'):
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert sha256(read(source['retained_excerpt'])).hexdigest() == source['excerpt_sha256']

chronicle = read('chronicle.md')
prefix = chronicle[:before['chronicle_bytes']]
assert sha256(prefix).hexdigest() == before['chronicle_sha256']
added = chronicle[before['chronicle_bytes']:].decode()
if '--closed' in sys.argv:
    assert re.fullmatch(r'- 2026-10-20 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', added), repr(added)
else:
    assert not added
result = dict(status='PASS', closed='--closed' in sys.argv,
    saved_attempts=28, completed_dates=27, headerless_timeouts=1,
    independently_recomputed_date_pairs=27, input_hashes_verified=verified,
    protected_files_unchanged=protected, garden_unchanged=True,
    old_room_prose_preserved=True, old_gate_preserved_except_two_lines=True,
    map_rooms=len(counts), map_missing=0, map_duplicates=0,
    open_questions=16, filed=0, researched=1, planted=0,
    new_words=['http-date'], chronicle_lines_added=len(added.splitlines()))
name = 'verification.json' if '--closed' in sys.argv else 'preflight.json'
(OUT/name).write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
