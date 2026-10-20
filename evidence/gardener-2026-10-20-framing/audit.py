"""Compare retained framing and decoded bytes, without making network requests."""
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
from typing import Any
import json

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
used = {}

def read(relative):
    path = (ROOT/relative).resolve()
    assert ROOT in path.parents and 'garden' not in path.relative_to(ROOT).parts
    data = path.read_bytes()
    used[str(path.relative_to(ROOT))] = sha256(data).hexdigest()
    return data

def load(relative):
    return json.loads(read(relative))

prior = load('evidence/gardener-2026-10-20-response-boundary/analysis.json')
for relative, expected in prior['input_sha256'].items():
    assert sha256(read(relative)).hexdigest() == expected, relative

rows = []
bodies = {}
for entry in prior['rows']:
    relative = Path(entry['capture'])
    record = load(relative)
    header = read(relative.with_suffix('.headers'))
    command = record['command']
    assert command[0:2] == ['curl', '--disable']
    assert '--raw' not in command and '--compressed' not in command
    assert '--location' not in command
    assert command[command.index('--retry')+1] == '0'
    # Some older records omit a redundant method field. Inspect the command
    # instead of filling that field in or modifying the historical capture.
    assert record.get('method') in (None, 'GET')
    expected_command = [
        'curl', '--disable', '--silent', '--show-error', '--proto', '=https',
        '--connect-timeout', '10', '--max-time', '45', '--max-filesize', '1048576',
        '--retry', '0', '--user-agent', 'castle-gardener/1.0',
        '--header', 'Accept-Encoding: identity', '--header', 'Git-Protocol: version=0',
        '--dump-header', str(relative.with_suffix('.headers')),
        '--output', str(relative.with_suffix('.body')),
        '--write-out', command[command.index('--write-out')+1], record['url']]
    assert command == expected_command
    assert record['url'] == 'https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack'
    assert 'Accept-Encoding: identity' in command and 'Git-Protocol: version=0' in command
    metrics = record['curl_metrics']
    assert dict(line.split('=', 1) for line in record['stdout'].splitlines()) == metrics
    row: dict[str, Any] = dict(capture=str(relative), start_utc=record['start_utc'],
        round=record['round'], curl_exit=record['curl_exit'],
        total_seconds=metrics['time_total'])
    if record['curl_exit'] != 0:
        assert record['curl_exit'] == 28 and header == b''
        assert not record['body_present'] and not (ROOT/relative.with_suffix('.body')).exists()
        row.update(framing='unobserved', content_sha256=None, body_bytes=None, completed_ge_1s=None)
    else:
        blocks = [x for x in header.split(b'\r\n\r\n') if x]
        assert len(blocks) == 1
        lines = blocks[0].decode('iso-8859-1').split('\r\n')
        assert lines[0] == 'HTTP/1.1 200 OK'
        fields = defaultdict(list)
        for line in lines[1:]:
            key, value = line.split(':', 1)
            fields[key.lower()].append(value.strip())
        assert 'content-encoding' not in fields
        body = read(relative.with_suffix('.body'))
        assert sha256(body).hexdigest() == record['body_sha256']
        assert len(body) == record['body_bytes'] == int(metrics['size_download'])
        if 'transfer-encoding' in fields:
            assert fields['transfer-encoding'] == ['chunked'] and 'content-length' not in fields
            framing = 'chunked'
        else:
            assert fields['content-length'] == [str(len(body))]
            framing = 'content-length'
        bodies[str(relative)] = body
        row.update(framing=framing, content_sha256=sha256(body).hexdigest(),
            body_bytes=len(body), completed_ge_1s=Decimal(metrics['time_total']) >= 1)
    rows.append(row)

# Keep byte equality, not just a digest, as the comparison criterion.
groups = defaultdict(list)
for row in rows:
    if row['content_sha256']:
        groups[row['content_sha256']].append(row)
mixed = []
for digest, group in groups.items():
    assert all(bodies[r['capture']] == bodies[group[0]['capture']] for r in group)
    if len({r['framing'] for r in group}) > 1:
        mixed.append(dict(content_sha256=digest,
            captures=[{k:r[k] for k in ('capture','start_utc','framing','total_seconds')} for r in group]))

visits = defaultdict(list)
for row in rows:
    visits[str(Path(row['capture']).parent)].append(row)
paired = []
for visit, group in visits.items():
    group.sort(key=lambda r:r['round'])
    assert [r['round'] for r in group] == [1,2]
    if all(r['content_sha256'] for r in group):
        equal = bodies[group[0]['capture']] == bodies[group[1]['capture']]
        paired.append(dict(visit=visit, same_content=equal,
            framing_pair=[r['framing'] for r in group],
            different_framing=group[0]['framing'] != group[1]['framing']))

cross = {f:dict(below_1s=sum(r['framing']==f and r['completed_ge_1s'] is False for r in rows),
               at_or_above_1s=sum(r['framing']==f and r['completed_ge_1s'] is True for r in rows))
         for f in ('content-length','chunked')}
summary = dict(attempts=len(rows), visits=len(visits),
    completed=sum(r['curl_exit']==0 for r in rows), timeouts=sum(r['curl_exit']==28 for r in rows),
    framing_counts=dict(Counter(r['framing'] for r in rows)),
    distinct_completed_contents=len(groups), contents_seen_with_both_framings=len(mixed),
    complete_within_visit_pairs=len(paired), same_content_pairs=sum(p['same_content'] for p in paired),
    same_content_different_framing_pairs=sum(p['same_content'] and p['different_framing'] for p in paired),
    framing_by_completed_wait=cross, inherited_input_hashes_verified=len(prior['input_sha256']))
result=dict(read_date=datetime.now().astimezone().date().isoformat(),
    scope='Same 28 saved orgmode attempts from 14 visits; no new service requests.',
    summary=summary, mixed_framing_contents=mixed, within_visit_pairs=paired, rows=rows, input_sha256=used,
    limits='Client-visible header dumps and decoded content only, not original chunk boundaries or a wire trace. The one-second cutoff is inherited and descriptive. Repeated requests are not independent events. No backend identity, cause, hidden update time or update-delay association is established.')
(OUT/'analysis.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print('MIXED FRAMING EXAMPLES:')
print(json.dumps(mixed,indent=2))
