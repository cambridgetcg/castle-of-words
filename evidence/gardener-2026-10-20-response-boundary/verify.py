"""Check evidence, narrow edits, the full Map, and the one-line close."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
closed = '--closed' in sys.argv
before = json.loads((OUT/'before.json').read_text())['files']
edited = {'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/time-to-first-byte.md', 'chronicle.md'}

def digest(data): return sha256(data).hexdigest()

def grounded(relative):
    p = (ROOT/relative).resolve()
    assert ROOT in p.parents
    return p.read_bytes()

for relative, old in before.items():
    if relative not in edited:
        assert digest(grounded(relative)) == old['sha256'], relative

original = {}
for relative in edited:
    data = subprocess.check_output(['git', 'show', 'HEAD:'+relative], cwd=ROOT)
    assert digest(data) == before[relative]['sha256'], ('git baseline moved', relative)
    original[relative] = data

room = grounded('rooms/what-the-gaps-can-say.md')
heading = b'## The first piece can be the envelope '
start = room.index(heading)
stop = room.index(b'## Sources\n', start)
assert room[:start]+room[stop:] == original['rooms/what-the-gaps-can-say.md']
assert room.startswith(b'# what-the-gaps-can-say\n\n*')
word = grounded('words/time-to-first-byte.md')
word_start = word.index(b'## The envelope can arrive before the letter ')
old_word = original['words/time-to-first-byte.md']
old_links = old_word[old_word.index(b'Links: '):]
assert word[:word_start]+old_links == old_word
assert word.startswith(b'# time-to-first-byte\n\n') and word.splitlines()[-1].startswith(b'Links: ')

old_gate = original['gate.md'].splitlines()
gate = grounded('gate.md').decode()
new_gate = gate.encode().splitlines()
assert len(old_gate) == len(new_gate)
changes = [(a,b) for a,b in zip(old_gate,new_gate) if a != b]
assert len(changes) == 2
assert any(a.startswith(b'> rooms: ') and b.startswith(b'> rooms: ') for a,b in changes)
assert any(a.startswith(b'- [what-the-gaps-can-say]') and b.startswith(b'- [what-the-gaps-can-say]') for a,b in changes)
map_section = gate.split('## Map\n',1)[1].split('\n## ',1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^\)]+\.md)\)', map_section, re.M)
rooms = sorted(p.name for p in (ROOT/'rooms').glob('*.md'))
assert sorted(entries) == rooms and len(entries) == len(set(entries))
questions = grounded('questions.md').decode()
open_count = sum(line.startswith('- [ ]') for line in questions.splitlines())
assert open_count == 16
assert f'rooms: **{len(rooms)}**' in gate and f'open doors: **{open_count}**' in gate
assert not any(line.startswith('- ') for line in grounded('courtyard.md').decode().splitlines())

for source in json.loads((OUT/'sources.json').read_text()):
    assert source['curl_exit'] == 0 and source['status'].splitlines()[0] == '200'
    assert digest((OUT/source['file']).read_bytes()) == source['sha256']
analysis = json.loads((OUT/'analysis.json').read_text())
for relative, expected in analysis['input_sha256'].items():
    assert digest(grounded(relative)) == expected, relative
# A separate raw-line count, without importing the audit's header parser.
statuses = Counter(); lengths = Counter(); framing = Counter(); failed = 0
for row in analysis['rows']:
    path = Path(row['capture'])
    record = json.loads(grounded(path))
    header = grounded(path.with_suffix('.headers'))
    found = re.findall(rb'^HTTP/[^\r\n]+', header, re.M)
    statuses.update(s.decode() for s in found)
    if record['curl_exit'] == 0:
        assert found == [b'HTTP/1.1 200 OK']
        body = grounded(path.with_suffix('.body'))
        lengths[len(body)] += 1
        assert row['saved_body_bytes'] == len(body)
        if re.search(rb'^Content-Length: 370\r$', header, re.M | re.I):
            framing['content_length'] += 1
        elif re.search(rb'^Transfer-Encoding: chunked\r$', header, re.M | re.I):
            framing['chunked'] += 1
        else:
            raise AssertionError(str(path))
    else:
        assert record['curl_exit'] == 28 and header == b'' and found == []
        failed += 1
assert statuses == {'HTTP/1.1 200 OK':27}
assert lengths == {370:27} and framing == {'content_length':19,'chunked':8} and failed == 1

chronicle = grounded('chronicle.md')
assert chronicle.startswith(original['chronicle.md'])
added = chronicle[len(original['chronicle.md']):].decode()
if closed:
    assert re.fullmatch(r'- 2026-10-20 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', added), added
else:
    assert added == ''

link_names = set(re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', (room[start:stop]+word[word_start:]).decode()))
for name in link_names:
    assert any((ROOT/where/(name+'.md')).exists() for where in ('words','rooms')), name
summary = dict(all_checks_passed=True, closed=closed, rooms=len(rooms), map_entries=len(entries),
    map_missing=0, map_extra=0, map_duplicates=0, open_questions=open_count,
    courtyard_insights=0, unchanged_preexisting_files_checked=len(before)-len(edited),
    garden_files_unchanged=sum(p.startswith('garden/') for p in before),
    source_downloads_checked=len(json.loads((OUT/'sources.json').read_text())),
    evidence_hashes_checked=len(analysis['input_sha256']), independently_counted_statuses=dict(statuses),
    saved_body_byte_counts=dict(lengths), framing_counts=dict(framing), timeouts=failed,
    prior_room_and_word_prose_preserved=True, gate_changed_lines=len(changes),
    chronicle_lines_added=len(added.splitlines()), new_section_link_targets_checked=len(link_names))
(OUT/('verification.json' if closed else 'preflight.json')).write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
