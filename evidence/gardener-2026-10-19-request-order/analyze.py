"""Offline request-order audit. Reads kept bytes; never runs a collector or network call."""
from collections import Counter
from datetime import datetime
from decimal import Decimal as D
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
used = {}

def raw(path):
    path = path.resolve()
    assert ROOT in path.parents and 'garden' not in path.relative_to(ROOT).parts
    data = path.read_bytes()
    used[str(path.relative_to(ROOT))] = sha256(data).hexdigest()
    return data

def load(path):
    return json.loads(raw(path))

def parse(body):
    """Validate only the complete two-reference SHA-1 protocol-v0 form in this slice."""
    packets, pos = [], 0
    while pos < len(body):
        prefix = body[pos:pos+4]
        assert re.fullmatch(b'[0-9a-fA-F]{4}', prefix)
        size = int(prefix, 16)
        if size == 0:
            packets.append(None); pos += 4
        else:
            assert size >= 4 and pos+size <= len(body)
            packets.append(body[pos+4:pos+size]); pos += size
    assert len(packets) == 5 and packets[:2] == [b'# service=git-upload-pack\n', None] and packets[-1] is None
    first, capbytes = packets[2].rstrip(b'\n').split(b'\x00', 1)
    caps = capbytes.decode('ascii').split()
    refs = {}
    for line in (first, packets[3].rstrip(b'\n')):
        oid, name = line.decode('ascii').split(' ', 1)
        assert re.fullmatch(r'[0-9a-f]{40}', oid) and name not in refs
        refs[name] = oid
    assert set(refs) == {'HEAD', 'refs/heads/master'} and refs['HEAD'] == refs['refs/heads/master']
    assert len(caps) == len(set(caps))
    return refs, caps

def elapsed(a, b):
    delta = datetime.fromisoformat(b) - datetime.fromisoformat(a)
    return str(D(delta.days*86400+delta.seconds) + D(delta.microseconds)/D(1000000))

def capture(path):
    rec = load(path)
    assert rec['url'] == 'https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack'
    # October 18 omits the explicit method field; retain that absence.
    # The full normalized curl commands are checked across the slice below.
    if 'method' in rec:
        assert rec['method'] == 'GET'
    bodypath = path.with_suffix('.body')
    if rec['curl_exit'] == 0:
        assert rec['curl_metrics']['http_code'] == '200' and rec['body_present']
        body = raw(bodypath)
        assert sha256(body).hexdigest() == rec['body_sha256']
        assert len(body) == rec['body_bytes'] == int(rec['curl_metrics']['size_download'])
        return rec, body, parse(body)
    assert rec['curl_exit'] == 28 and rec['curl_metrics']['http_code'] == '000'
    assert not rec['body_present'] and not bodypath.exists() and rec['body_sha256'] is None and rec['body_bytes'] is None
    assert rec['curl_metrics']['size_download'] == '0'
    return rec, None, None

old = load(ROOT/'evidence/gardener-2026-10-19-missing-reads/analysis.json')
# Validate every saved input of the preceding audit, not just its final table.
for name, expected in old['input_sha256'].items():
    assert sha256(raw(ROOT/name)).hexdigest() == expected, name

selected = sorted(p for p in (ROOT/'evidence').glob('gardener-2026-10-1*-service-check*')
                  if p.is_dir() and re.fullmatch(r'gardener-2026-10-(17|18)-service-check(?:-[0-9]+)?', p.name))
assert {str(p.relative_to(ROOT)) for p in selected} == {r['directory'] for r in old['rows']}
selected.sort(key=lambda p: load(p/'r1-orgmode.json')['start_utc'])
counts = {k: Counter() for k in ('first_wait', 'second_wait', 'either_wait', 'second_response_outcome', 'within_visit_view')}
rows, last_complete, settings = [], None, None
for directory in selected:
    manifest = load(directory/'manifest.json')
    comp = next(c for c in load(directory/'comparison.json')['comparisons'] if c['id']=='r1-orgmode')
    pointer = comp.get('previous_complete_capture', comp.get('previous_capture'))
    assert pointer
    if last_complete is not None: assert pointer == last_complete
    prior, priorbody, priorview = capture(ROOT/pointer)
    first, firstbody, firstview = capture(directory/'r1-orgmode.json')
    second, secondbody, secondview = capture(directory/'r2-orgmode.json')
    assert firstview is not None and priorview is not None
    for rec in (first, second):
        assert rec == next(r for r in manifest['records'] if r['id'] == rec['id'])
        assert datetime.fromisoformat(rec['start_utc']) <= datetime.fromisoformat(rec['finish_utc'])
        command = rec['command'][:]
        for flag in ('--output', '--dump-header'): command[command.index(flag)+1] = '<capture>'
        if settings is None: settings = command
        assert command == settings
        assert command[command.index('--retry')+1] == '0'
    assert datetime.fromisoformat(prior['finish_utc']) <= datetime.fromisoformat(first['start_utc'])
    assert datetime.fromisoformat(first['finish_utc']) <= datetime.fromisoformat(second['start_utc'])
    changed = firstview[0] != priorview[0]
    assert firstview[1] == priorview[1] and set(firstview[0]) == set(priorview[0])
    assert comp['body_equal_to_previous'] == (firstbody == priorbody)
    within = None
    if secondview is not None:
        within = secondview[0] != firstview[0]
        assert not within and secondview == firstview and secondbody == firstbody
    label = 'changed' if changed else 'no_detected_change'
    waits = [D(r['curl_metrics']['time_total']) for r in (first, second)]
    for key, value in zip(('first_wait','second_wait','either_wait'), (waits[0], waits[1], max(waits))):
        counts[key][label, 'ge_1s' if value >= 1 else 'lt_1s'] += 1
    response_label = 'missing_timeout' if secondview is None else ('completed_ge_1s' if waits[1] >= 1 else 'completed_lt_1s')
    counts['second_response_outcome'][label, response_label] += 1
    counts['within_visit_view'][label, 'missing_timeout' if within is None else ('changed' if within else 'no_detected_change')] += 1
    prior_to_first = elapsed(prior['finish_utc'], first['start_utc'])
    first_to_second = elapsed(first['finish_utc'], second['start_utc'])
    row = dict(directory=str(directory.relative_to(ROOT)), previous_complete_capture=pointer,
               first_view_changed=changed, within_visit_view_changed=within,
               first_request_interval_utc=[first['start_utc'], first['finish_utc']],
               second_request_interval_utc=[second['start_utc'], second['finish_utc']],
               previous_finish_to_first_start_seconds=prior_to_first,
               first_finish_to_second_start_seconds=first_to_second,
               first_wait_seconds=str(waits[0]), second_client_wait_seconds=str(waits[1]),
               second_curl_exit=second['curl_exit'], second_response_complete=secondview is not None,
               old_either_wait_label_differs_from_first_wait=(max(waits)>=1)!=(waits[0]>=1))
    oldrow = next(r for r in old['rows'] if r['directory']==row['directory'])
    assert changed == oldrow['first_advertised_map_changed']
    assert [str(x) for x in waits] == [r['client_wait_seconds'] for r in oldrow['orgmode_slots']]
    assert (max(waits)>=1) == oldrow['at_least_one_client_wait_ge_1s']
    rows.append(row)
    last_complete = str((directory/('r2-orgmode.json' if secondview is not None else 'r1-orgmode.json')).relative_to(ROOT))

def table(counter, outcomes):
    return {label: {outcome: counter[label,outcome] for outcome in outcomes} for label in ('changed','no_detected_change')}

tables = {k: table(counts[k], ('ge_1s','lt_1s')) for k in ('first_wait','second_wait','either_wait')}
tables['second_response_outcome'] = table(counts['second_response_outcome'], ('completed_ge_1s','completed_lt_1s','missing_timeout'))
tables['within_visit_view'] = table(counts['within_visit_view'], ('changed','no_detected_change','missing_timeout'))
summary = dict(analysis_date='2026-10-19', threshold_seconds='1', visits=len(rows), orgmode_attempts=2*len(rows),
               completed_first_responses=sum(1 for r in rows),
               completed_second_responses=sum(r['second_response_complete'] for r in rows),
               changed_first_views=sum(r['first_view_changed'] for r in rows),
               labels_changed_by_using_first_wait_only=sum(r['old_either_wait_label_differs_from_first_wait'] for r in rows),
               verified_prior_input_hashes=len(old['input_sha256']),
               tables=tables, rows=rows, input_sha256=used,
               limits='Retrospective descriptive comparison of received views and request waits; no update times, causal inference, p-values or independent event draws.')
(OUT/'analysis.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('rows','input_sha256')},indent=2))
print('VISITS WITH ANY WAIT AT LEAST ONE SECOND')
for row in rows:
    if max(D(row['first_wait_seconds']),D(row['second_client_wait_seconds'])) >= 1:
        print(json.dumps(row,indent=2))
print('INPUT HASHES',len(used))
