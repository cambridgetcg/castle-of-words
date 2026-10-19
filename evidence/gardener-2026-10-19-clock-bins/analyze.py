"""Recount the fixed fourteen-visit slice into stated UTC bins, offline."""
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
used = {}
LABELS = ['00:00–06:00', '06:00–12:00', '12:00–18:00', '18:00–24:00']
URL = 'https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack'

def read(relative):
    p = (ROOT/relative).resolve()
    assert ROOT in p.parents and 'garden' not in p.relative_to(ROOT).parts
    b = p.read_bytes(); used[str(p.relative_to(ROOT))] = sha256(b).hexdigest()
    return b

def load(relative): return json.loads(read(relative))
def stamp(text):
    d = datetime.fromisoformat(text)
    assert d.utcoffset() == timedelta(0)
    return d

def bin_index(d): return d.hour // 6

def view(relative):
    record = load(relative)
    assert record['url'] == URL
    body_path = Path(relative).with_suffix('.body')
    if record['curl_exit']:
        assert record['curl_exit'] == 28 and record['curl_metrics']['http_code'] == '000'
        assert not record['body_present'] and not (ROOT/body_path).exists()
        return record, None
    assert record['curl_metrics']['http_code'] == '200' and record['body_present']
    b = read(body_path)
    assert sha256(b).hexdigest() == record['body_sha256'] and len(b) == record['body_bytes']
    packets = []; pos = 0
    while pos < len(b):
        size = int(b[pos:pos+4], 16)
        assert size == 0 or 4 <= size <= len(b)-pos
        packets.append(b[pos+4:pos+size] if size else None)
        pos += size or 4
    assert pos == len(b) and len(packets) == 5
    assert packets[0:2] == [b'# service=git-upload-pack\n', None] and packets[-1] is None
    pairs = [packets[2].split(b'\0', 1)[0], packets[3].rstrip(b'\n')]
    refs = {}
    for pair in pairs:
        oid, name = pair.decode('ascii').split(' ')
        assert re.fullmatch('[0-9a-f]{40}', oid) and name not in refs
        refs[name] = oid
    assert set(refs) == {'HEAD', 'refs/heads/master'} and len(set(refs.values())) == 1
    return record, refs

prior = load('evidence/gardener-2026-10-19-request-order/analysis.json')
assert len(prior['rows']) == 14
columns = ['first_views', 'changed', 'no_detected_change', 'first_wait_ge_1s', 'rechecks', 'completed_recheck_ge_1s', 'timeout_recheck', 'changed_cross_bin_gap', 'all_cross_bin_gaps']
table: list[dict] = [dict(utc_bin=label, **{key: 0 for key in columns}) for label in LABELS]
rows = []
for old in prior['rows']:
    directory = Path(old['directory'])
    previous, pv = view(old['previous_complete_capture'])
    first, fv = view(directory/'r1-orgmode.json')
    second, sv = view(directory/'r2-orgmode.json')
    assert pv is not None and fv is not None
    changed = pv != fv
    assert changed == old['first_view_changed']
    assert sv is None or sv == fv
    start = stamp(first['start_utc']); finish = stamp(first['finish_utc'])
    second_start = stamp(second['start_utc']); prior_finish = stamp(previous['finish_utc'])
    assert prior_finish <= start <= finish <= second_start
    boundaries = []
    boundary = prior_finish.replace(hour=(prior_finish.hour//6)*6, minute=0, second=0, microsecond=0) + timedelta(hours=6)
    while boundary <= start:
        boundaries.append(boundary.isoformat()); boundary += timedelta(hours=6)
    i = bin_index(start); j = bin_index(second_start)
    table[i]['first_views'] += 1
    table[i]['changed' if changed else 'no_detected_change'] += 1
    table[i]['first_wait_ge_1s'] += int(Decimal(first['curl_metrics']['time_total']) >= 1)
    table[i]['changed_cross_bin_gap'] += int(changed and bool(boundaries))
    table[i]['all_cross_bin_gaps'] += int(bool(boundaries))
    table[j]['rechecks'] += 1
    table[j]['timeout_recheck'] += int(sv is None)
    table[j]['completed_recheck_ge_1s'] += int(sv is not None and Decimal(second['curl_metrics']['time_total']) >= 1)
    rows.append(dict(directory=str(directory), previous_complete_capture=old['previous_complete_capture'], prior_finish_utc=previous['finish_utc'], first_start_utc=first['start_utc'], first_finish_utc=first['finish_utc'], second_start_utc=second['start_utc'], first_bin=LABELS[i], second_bin=LABELS[j], changed=changed, first_wait=first['curl_metrics']['time_total'], second_client_wait=second['curl_metrics']['time_total'], second_complete=sv is not None, completed_view_gap_crossed_boundaries_utc=boundaries))
result: dict = dict(read_date=datetime.now(timezone.utc).date().isoformat(), bins='UTC; include lower bound, exclude upper bound; per-request start; fixed before calculation', threshold='one second, inherited descriptive convention', table=table, totals={key: sum(row[key] for row in table) for key in columns}, rows=rows, input_sha256=used, limits='Neither bin assignment nor crossed gap dates a hidden update. No event kinds, independence, host-local time, exposure-adjusted rates, statistical test or causation inferred. No new service probes.')
assert result['totals']['first_views'] == 14 and result['totals']['changed'] == 10
assert result['totals']['timeout_recheck'] == 1
(OUT/'analysis.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({key:result[key] for key in ('table','totals')}, indent=2, ensure_ascii=False))
print('Verified source files:', len(used))
