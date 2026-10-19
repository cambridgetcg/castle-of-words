"""Offline gap audit of an already selected slice; no collector or network imports."""
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

def read(path):
    p = path.resolve()
    assert ROOT in p.parents and 'garden' not in p.relative_to(ROOT).parts
    data = p.read_bytes()
    used[str(p.relative_to(ROOT))] = sha256(data).hexdigest()
    return data

def load(path): return json.loads(read(path))

def view(path):
    rec = load(path)
    assert rec['url'] == 'https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack'
    if rec['curl_exit'] != 0:
        assert rec['curl_exit'] == 28 and not rec['body_present'] and not path.with_suffix('.body').exists()
        return rec, None
    assert rec['curl_metrics']['http_code'] == '200' and rec['body_present']
    body = read(path.with_suffix('.body'))
    assert sha256(body).hexdigest() == rec['body_sha256'] and len(body) == rec['body_bytes']
    packets, offset = [], 0
    while offset < len(body):
        assert re.fullmatch(rb'[0-9a-fA-F]{4}', body[offset:offset+4])
        size = int(body[offset:offset+4], 16)
        if size == 0:
            packets.append(None); offset += 4
        else:
            assert 4 <= size <= len(body)-offset
            packets.append(body[offset+4:offset+size]); offset += size
    assert len(packets) == 5 and packets[:2] == [b'# service=git-upload-pack\n', None] and packets[-1] is None
    reference, capabilities = packets[2].rstrip(b'\n').split(b'\x00', 1)
    pairs = [reference, packets[3].rstrip(b'\n')]
    refs = {}
    for pair in pairs:
        oid, name = pair.decode('ascii').split(' ', 1)
        assert re.fullmatch('[0-9a-f]{40}', oid) and name not in refs
        refs[name] = oid
    assert set(refs) == {'HEAD', 'refs/heads/master'} and refs['HEAD'] == refs['refs/heads/master']
    return rec, (refs, capabilities)

def difference_seconds(start, finish):
    delta = datetime.fromisoformat(finish)-datetime.fromisoformat(start)
    return D(delta.days*86400 + delta.seconds) + D(delta.microseconds)/D(1000000)

def median(values):
    values = sorted(values); n = len(values)
    return values[n//2] if n%2 else (values[n//2-1]+values[n//2])/D(2)

previous = load(ROOT/'evidence/gardener-2026-10-19-request-order/analysis.json')
for name, expected in previous['input_sha256'].items():
    assert sha256(read(ROOT/name)).hexdigest() == expected, name
rows = []
last_complete = None
last_attempt = None
settings = None
for old in previous['rows']:
    directory = ROOT/old['directory']
    prior_path = ROOT/old['previous_complete_capture']
    prior, prior_view = view(prior_path)
    first, first_view = view(directory/'r1-orgmode.json')
    second, second_view = view(directory/'r2-orgmode.json')
    assert prior_view is not None and first_view is not None
    if last_complete: assert old['previous_complete_capture'] == last_complete
    for record in (prior, first, second):
        command = record['command'][:]
        for flag in ('--output', '--dump-header'): command[command.index(flag)+1] = '<capture>'
        if settings is None: settings = command
        assert command == settings
        assert record['url'] == record['curl_metrics']['url_effective']
    changed = prior_view[0] != first_view[0]
    assert changed == old['first_view_changed'] and prior_view[1] == first_view[1]
    gap = difference_seconds(prior['finish_utc'], first['start_utc'])
    assert gap >= 0 and gap == D(old['previous_finish_to_first_start_seconds'])
    interrupted = False
    attempt_finish = attempt_gap = None
    if last_attempt is not None and last_attempt['curl_exit'] != 0:
        interrupted = True
        assert datetime.fromisoformat(prior['finish_utc']) < datetime.fromisoformat(last_attempt['start_utc']) < datetime.fromisoformat(last_attempt['finish_utc']) < datetime.fromisoformat(first['start_utc'])
        attempt_finish = last_attempt['finish_utc']
        attempt_gap = str(difference_seconds(attempt_finish, first['start_utc']))
    rows.append(dict(directory=old['directory'], previous_complete_capture=old['previous_complete_capture'], previous_finish_utc=prior['finish_utc'], first_start_utc=first['start_utc'], first_finish_utc=first['finish_utc'], first_view_changed=changed, previous_finish_to_first_start_seconds=str(gap), gap_hours=str(gap/D(3600)), intervening_timeout_in_selected_series=interrupted, last_attempt_finish_utc=attempt_finish, last_attempt_finish_to_first_start_seconds=attempt_gap))
    last_complete = str((directory/('r2-orgmode.json' if second_view is not None else 'r1-orgmode.json')).relative_to(ROOT))
    last_attempt = second

summary = {}
for label, chosen in [('changed', [r for r in rows if r['first_view_changed']]), ('no_detected_change', [r for r in rows if not r['first_view_changed']]), ('all', rows)]:
    gaps = [D(r['previous_finish_to_first_start_seconds']) for r in chosen]
    summary[label] = dict(comparisons=len(gaps), min_seconds=str(min(gaps)), median_seconds=str(median(gaps)), max_seconds=str(max(gaps)), total_seconds=str(sum(gaps)), min_hours=str(min(gaps)/D(3600)), median_hours=str(median(gaps)/D(3600)), max_hours=str(max(gaps)/D(3600)), total_hours=str(sum(gaps)/D(3600)))
longest = max(rows, key=lambda r:D(r['previous_finish_to_first_start_seconds']))
shortest = min(rows, key=lambda r:D(r['previous_finish_to_first_start_seconds']))
result = dict(date='2026-10-19', question=740, input_sha256=used, rows=rows, summary=summary, longest_gap=longest, shortest_gap=shortest, interrupted_gaps=[r for r in rows if r['intervening_timeout_in_selected_series']], limits='Wall-clock subtraction of recorded endpoints, not continuous observation, event counts, update times, exposure-adjusted host rates, a model fit, or a causal test. No new service requests.')
(OUT/'analysis.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('summary','longest_gap','shortest_gap','interrupted_gaps')},indent=2))
print('VERIFIED INPUT HASHES',len(used))
print('ROWS: directory, changed, recorded gap hours')
for r in rows: print(r['directory'].split('/')[-1], r['first_view_changed'], format(D(r['gap_hours']),'.6f'))
