"""Separate exact-fraction checks against raw records, plus scope and prose checks."""
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

def data(path):
    p = path if isinstance(path, Path) and path.is_absolute() else ROOT/path
    assert ROOT in p.resolve().parents
    return p.read_bytes()

def load(path): return json.loads(data(path))
def refs(path):
    body = data(Path(path).with_suffix('.body'))
    pairs = re.findall(rb'([0-9a-f]{40}) (HEAD|refs/heads/master)(?=\x00|\n)', body)
    assert len(pairs) == 2
    return {name: oid for oid, name in pairs}

before = load(OUT/'before.json')
a = load(OUT/'analysis.json')
prior = load('evidence/gardener-2026-10-19-request-order/analysis.json')
lookup = {v['directory']: v for v in prior['rows']}
assert len(lookup) == 14 and len(a['rows']) == 28
for relative, expected in a['input_sha256'].items():
    assert sha256(data(relative)).hexdigest() == expected, relative

long_rows = []; timeout_rows = []; rechecks = 0; changed = 0
for row in a['rows']:
    p = Path(row['capture'])
    r = load(p); m = r['curl_metrics']
    pre = Fraction(m['time_pretransfer']); first = Fraction(m['time_starttransfer']); total = Fraction(m['time_total'])
    assert Fraction(row['pretransfer_seconds']) == pre
    assert Fraction(row['raw_first_byte_seconds']) == first
    assert Fraction(row['total_seconds']) == total
    assert r['start_utc'] == row['start_utc'] and r['round'] == row['round']
    if r['curl_exit'] == 0:
        assert row['complete'] and m['http_code'] == '200'
        assert Fraction(row['pretransfer_to_first_byte_seconds']) == first-pre
        assert Fraction(row['first_byte_to_finish_seconds']) == total-first
        assert pre >= 0 and first >= pre and total >= first
        assert pre + Fraction(row['pretransfer_to_first_byte_seconds']) + Fraction(row['first_byte_to_finish_seconds']) == total
        assert row['total_ge_1s'] == (total >= 1)
        if r['round'] == 1:
            previous = lookup[str(p.parent)]['previous_complete_capture']
            different = refs(p) != refs(previous)
            changed += different
            assert row['view_comparison'] == ('changed from previous complete capture' if different else 'no detected change from previous complete capture')
        else:
            assert refs(p) == refs(p.parent/'r1-orgmode.json')
            assert row['view_comparison'] == "matches this visit's first reply"
            rechecks += 1
        if total >= 1:
            long_rows.append(row)
            assert (first-pre)/total > Fraction(98, 100)
    else:
        timeout_rows.append(row)
        assert not row['complete'] and r['curl_exit'] == 28 and m['http_code'] == '000'
        assert first == 0 and r['body_present'] is False
        assert data(p.with_suffix('.headers')) == b'' and not (ROOT/p.with_suffix('.body')).exists()
        assert '0 bytes received' in r['stderr']
        assert row['pretransfer_to_first_byte_seconds'] is None and row['first_byte_to_finish_seconds'] is None and row['total_ge_1s'] is None
        assert Fraction(row['pretransfer_to_abort_seconds']) == total-pre == Fraction('44.891925')
assert len(long_rows) == 3 and len(timeout_rows) == 1 and rechecks == 13 and changed == 10
assert a['long_completed'] == long_rows and a['timed_out'] == timeout_rows
assert max(Fraction(r['first_byte_to_finish_seconds']) for r in long_rows) == Fraction('0.001174')
assert a['summary']['completed'] == 27 and a['summary']['completed_lt_1s'] == 24

sources = load(OUT/'sources.json')
for source in sources:
    assert source['curl_exit'] == 0 and source['http_status'] == '200'
    assert sha256(data(OUT/source['file'])).hexdigest() == source['sha256']

for name in ('courtyard.md', 'questions.md', 'quests.md'):
    assert data(name).decode() == before['files'][name]['text'], name
questions = data('questions.md').decode()
assert sum(line.startswith('- [ ]') for line in questions.splitlines()) == 16
assert not any(line.startswith('- ') for line in data('courtyard.md').decode().splitlines())
garden = {}
for p in (ROOT/'garden').rglob('*'):
    if p.is_file(): garden[str(p.relative_to(ROOT))] = sha256(data(p)).hexdigest()
assert garden == before['garden_sha256']

room = data('rooms/what-the-gaps-can-say.md').decode()
marker = '## Put the first byte on the ruler — 2026-10-19\n'
assert room.count(marker) == 1
left, rest = room.split(marker)
addition, right = rest.split('## Sources\n', 1)
assert left + '## Sources\n' + right == before['files']['rooms/what-the-gaps-can-say.md']['text']
assert room.splitlines()[0] == '# what-the-gaps-can-say' and room.splitlines()[2].startswith('*')
for r in long_rows:
    for key in ('pretransfer_seconds', 'pretransfer_to_first_byte_seconds', 'first_byte_to_finish_seconds', 'total_seconds'):
        assert r[key] in addition
assert '**740 remains open.**' in addition and 'uncertain:' in addition

word = data('words/time-to-first-byte.md').decode()
assert before['files']['words/time-to-first-byte.md'] is None
assert word.splitlines()[0] == '# time-to-first-byte'
assert word.splitlines()[2].startswith('Time to first byte is ')
assert word.rstrip().splitlines()[-1].startswith('Links: ')
links = set(re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', addition + word))
for name in links:
    assert any((ROOT/sub/(name+'.md')).exists() for sub in ('words', 'rooms', '')), name

old_gate = before['files']['gate.md']['text']
gate = data('gate.md').decode()
old_lines, new_lines = old_gate.splitlines(), gate.splitlines()
assert len(old_lines) == len(new_lines)
changes = [(old, new) for old, new in zip(old_lines, new_lines) if old != new]
assert len(changes) == 1 and all(line.startswith('- [what-the-gaps-can-say]') for line in changes[0])
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
listed = re.findall(r'^- \[[^\]]+\]\(rooms/([^/)]+)\.md\) — .+$', map_text, re.M)
rooms = sorted(p.stem for p in (ROOT/'rooms').glob('*.md'))
assert Counter(listed) == Counter(rooms)
assert sorted(name+'.md' for name in rooms) == before['rooms']

chronicle = data('chronicle.md').decode()
closed = '--closed' in sys.argv
if closed:
    original = before['files']['chronicle.md']['text']
    assert chronicle.startswith(original)
    added = chronicle[len(original):]
    assert len(added.splitlines()) == 1
    assert re.fullmatch(r'- 2026-10-19 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', added)
else:
    assert chronicle == before['files']['chronicle.md']['text']

result = dict(status='PASS', checked_at=datetime.now(timezone.utc).isoformat(), closed=closed, raw_attempts=28, completed=27, long_completed=3, timeout_separate=1, input_hashes=len(a['input_sha256']), source_hashes=len(sources), all_rooms_once=len(rooms), resolving_new_wikilinks=len(links), garden_files_unchanged=len(garden), open_questions=16, preserved_old_room=True, changed_gate_lines=1, chronicle_lines_added=int(closed), review_limit='Same-session exact-fraction checks, not independent review or remote-history authentication.')
(OUT/('verification.json' if closed else 'preflight.json')).write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
