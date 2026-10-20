"""Check this visit's evidence, limited prose edits, Map, and one-line close."""
from collections import Counter, defaultdict
from email import policy
from email.parser import BytesParser
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import re
import sys

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
closed = '--closed' in sys.argv
before = json.loads((OUT/'before.json').read_text())['files']
boundaries = json.loads((OUT/'edit-boundaries.json').read_text())
changed = {'gate.md','chronicle.md','rooms/what-the-gaps-can-say.md','words/transfer-coding.md'}

def read(relative):
    path=(ROOT/relative).resolve()
    assert ROOT in path.parents
    return path.read_bytes()

def digest(data): return sha256(data).hexdigest()

for path, old in before.items():
    if path not in changed:
        assert digest(read(path)) == old['sha256'], path
actual_garden = {str(p.relative_to(ROOT)) for p in (ROOT/'garden').rglob('*') if p.is_file()}
assert actual_garden == {p for p in before if p.startswith('garden/')}

room=read('rooms/what-the-gaps-can-say.md')
start=room.index(b'## The wrapper changed while the list stayed the same ')
stop=room.index(b'## Sources\n',start)
assert digest(room[:start]+room[stop:]) == before['rooms/what-the-gaps-can-say.md']['sha256']
assert room.startswith(b'# what-the-gaps-can-say\n\n*')
word=read('words/transfer-coding.md')
wstart=word.index(b'## The wrapper can change along the path ')
restored=word[:wstart]+(boundaries['word_original_links']+'\n').encode()
assert digest(restored) == before['words/transfer-coding.md']['sha256']
new_word=read('words/message-framing.md')
for name,data in [('transfer-coding',word),('message-framing',new_word)]:
    assert data.startswith(('# '+name+'\n\n').encode())
    assert data.splitlines()[-1].startswith(b'Links: ')
    assert b'2026-10-20' in data and b'https://www.rfc-editor.org/rfc/rfc9112.txt' in data

gate=read('gate.md').decode()
reconstructed=gate
prefixes=['> rooms: ','- [what-the-gaps-can-say]']
for old,prefix in zip(boundaries['gate_original_lines'],prefixes):
    found=[line for line in reconstructed.splitlines() if line.startswith(prefix)]
    assert len(found)==1 and found[0]!=old
    reconstructed=reconstructed.replace(found[0],old,1)
assert digest(reconstructed.encode())==before['gate.md']['sha256']
map_text=gate.split('## Map\n',1)[1].split('\n## ',1)[0]
entries=re.findall(r'^- \[[^\]]+\]\(rooms/([^\)]+\.md)\)',map_text,re.M)
rooms=sorted(p.name for p in (ROOT/'rooms').glob('*.md'))
assert sorted(entries)==rooms and len(entries)==len(set(entries))
questions=read('questions.md').decode()
open_count=sum(s.startswith('- [ ]') for s in questions.splitlines())
assert open_count==16
assert f'rooms: **{len(rooms)}**' in gate and f'open doors: **{open_count}**' in gate
assert not any(s.startswith('- ') for s in read('courtyard.md').decode().splitlines())

sources=json.loads((OUT/'sources.json').read_text())
for source in sources:
    assert source['curl_exit']==0 and source['result'].splitlines()[0]=='200'
    assert digest((OUT/source['file']).read_bytes())==source['sha256']
analysis=json.loads((OUT/'analysis.json').read_text())
for path,expected in analysis['input_sha256'].items():
    assert digest(read(path))==expected,path

# Recount from original captures with an email header parser and exact fractions;
# do not import the audit's header splitting or its Decimal calculations.
by_content=defaultdict(list); by_visit=defaultdict(list); counts=Counter()
waits={f:{'below_1s':0,'at_or_above_1s':0} for f in ('content-length','chunked')}
for row in analysis['rows']:
    relative=Path(row['capture']); record=json.loads(read(relative))
    raw=read(relative.with_suffix('.headers'))
    if record['curl_exit']==0:
        first,header_bytes=raw.split(b'\r\n',1)
        assert first==b'HTTP/1.1 200 OK'
        fields=BytesParser(policy=policy.default).parsebytes(header_bytes)
        assert not fields.defects and 'Content-Encoding' not in fields
        body=read(relative.with_suffix('.body'))
        assert len(body)==370
        if 'Transfer-Encoding' in fields:
            assert fields.get_all('Transfer-Encoding')==['chunked']
            assert 'Content-Length' not in fields
            kind='chunked'
        else:
            assert fields.get_all('Content-Length')==['370']
            kind='content-length'
        assert row['framing']==kind and row['content_sha256']==digest(body)
        counts[kind]+=1
        long=Fraction(record['curl_metrics']['time_total'])>=1
        waits[kind]['at_or_above_1s' if long else 'below_1s']+=1
        by_content[body].append(kind)
        by_visit[str(relative.parent)].append((body,kind))
    else:
        assert record['curl_exit']==28 and raw==b''
        assert not (ROOT/relative.with_suffix('.body')).exists()
        assert row['framing']=='unobserved' and row['content_sha256'] is None
        counts['unobserved']+=1
        by_visit[str(relative.parent)].append((None,'unobserved'))

complete_pairs=[p for p in by_visit.values() if len(p)==2 and all(v[0] is not None for v in p)]
assert all(p[0][0]==p[1][0] for p in complete_pairs)
mixed_pairs=sum(p[0][1]!=p[1][1] for p in complete_pairs)
mixed_contents=sum(len(set(kinds))==2 for kinds in by_content.values())
assert len(by_visit)==14 and len(complete_pairs)==13
assert len(by_content)==11 and mixed_contents==5 and mixed_pairs==6
assert dict(counts)==analysis['summary']['framing_counts']=={'content-length':19,'chunked':8,'unobserved':1}
assert waits==analysis['summary']['framing_by_completed_wait']
assert waits=={'content-length':{'below_1s':17,'at_or_above_1s':2},'chunked':{'below_1s':7,'at_or_above_1s':1}}

added_writing=(room[start:stop]+word[wstart:]+new_word).decode()
links=set(re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',added_writing))
for name in links:
    assert any((ROOT/area/(name+'.md')).is_file() for area in ('words','rooms')),name
for text,base in [(room[start:stop].decode(),ROOT/'rooms'),(word[wstart:].decode(),ROOT/'words'),(new_word.decode(),ROOT/'words')]:
    for link in re.findall(r'\]\(([^\)]+)\)',text):
        if not link.startswith(('http://','https://')):
            target=(base/link).resolve(); assert ROOT in target.parents and target.is_file(),link

chronicle=read('chronicle.md'); old=before['chronicle.md']
assert digest(chronicle[:old['bytes']])==old['sha256']
added=chronicle[old['bytes']:].decode()
if closed:
    assert re.fullmatch(r'- 2026-10-20 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n',added),added
else:
    assert added==''

summary=dict(all_checks_passed=True,closed=closed,rooms=len(rooms),map_entries=len(entries),
    map_duplicates=0,map_missing=0,map_extra=0,open_questions=open_count,courtyard_insights=0,
    garden_files_unchanged=len(actual_garden),questions_and_quests_unchanged=True,
    source_download_hashes_checked=len(sources),evidence_hashes_checked=len(analysis['input_sha256']),
    same_content_different_framing_pairs=mixed_pairs,distinct_contents=len(by_content),
    contents_seen_under_both_framings=mixed_contents,framing_counts=dict(counts),framing_by_wait=waits,
    original_prose_preserved=True,gate_changed_lines=2,new_wiki_link_targets_checked=len(links),
    chronicle_lines_added=len(added.splitlines()))
(OUT/('verification.json' if closed else 'preflight.json')).write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
