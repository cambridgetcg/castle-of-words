"""Offline missing-read audit of two complete, explicitly named directory slices."""
from collections import Counter
from datetime import datetime
from decimal import Decimal
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

def parse_view(body):
    """Only the complete SHA-1 protocol-v0 form present in these saved bodies."""
    packets, pos = [], 0
    while pos < len(body):
        prefix = body[pos:pos+4]
        assert re.fullmatch(b'[0-9a-fA-F]{4}', prefix)
        size = int(prefix, 16)
        if size == 0:
            packets.append(None); pos += 4
        else:
            assert size >= 4 and pos + size <= len(body)
            packets.append(body[pos+4:pos+size]); pos += size
    assert packets[:2] == [b'# service=git-upload-pack\n', None] and packets[-1] is None
    refs, caps = {}, []
    for i, packet in enumerate(packets[2:-1]):
        assert packet is not None
        line = packet.rstrip(b'\n')
        if i == 0:
            line, capbytes = line.split(b'\x00', 1)
            caps = capbytes.decode('ascii').split()
        else:
            assert b'\x00' not in line
        oid, name = line.decode('ascii').split(' ', 1)
        assert re.fullmatch(r'[0-9a-f]{40}', oid) and name not in refs
        refs[name] = oid
    assert set(refs) == {'HEAD', 'refs/heads/master'}
    assert refs['HEAD'] == refs['refs/heads/master']
    assert len(caps) == len(set(caps))
    return {'references': refs, 'capabilities': caps}

# The inspected collector supplies the planned two-round order and stop rule.
# Read it as evidence only: importing it could start or prepare live collection.
collector_source = raw(ROOT / 'evidence/gardener-2026-10-17-service-check/observe.py').decode()
assert "for round_number in (1, 2):" in collector_source
assert "for name in ('orgmode', 'emacs', 'guix'):" in collector_source
assert "if result['stopped_reason']:" in collector_source

paths = sorted(p for p in (ROOT / 'evidence').glob('gardener-2026-10-1*-service-check*') if p.is_dir() and re.fullmatch(r'gardener-2026-10-(17|18)-service-check(?:-[0-9]+)?', p.name))
assert paths
manifests = [(p, load(p / 'manifest.json')) for p in paths]
manifests.sort(key=lambda item: item[1]['records'][0]['start_utc'])
expected = ['r%d-%s' % (r, name) for r in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
rows, missing_slots, attempts = [], [], []
complete_table, wait_table, status_counts = Counter(), Counter(), Counter()
settings, previous_finish, last_complete = None, None, None
for p, manifest in manifests:
    comparison = load(p / 'comparison.json')
    records = manifest['records']
    assert ('stopped_reason' in manifest) != ('stop_reason' in manifest)
    stopped = manifest['stopped_reason'] if 'stopped_reason' in manifest else manifest['stop_reason']
    assert [r['id'] for r in records] == expected[:len(records)]
    if len(records) < len(expected):
        assert stopped and records[-1]['curl_exit'] != 0
    else:
        assert stopped is None
    bodies, views, slots = {}, {}, []
    for rec in records:
        recpath = p / (rec['id'] + '.json')
        assert rec == load(recpath)
        bodypath = recpath.with_suffix('.body')
        metrics = rec['curl_metrics']
        assert rec['body_present'] == bodypath.exists()
        if bodypath.exists():
            body = raw(bodypath)
            assert sha256(body).hexdigest() == rec['body_sha256']
            assert len(body) == rec['body_bytes'] == int(metrics['size_download'])
            bodies[rec['id']] = body
        else:
            assert rec['body_sha256'] is None and rec['body_bytes'] is None and metrics['size_download'] == '0'
        endpoint = rec['id'].split('-', 1)[1]
        assert rec['url'] == 'https://yhetil.org/' + endpoint + '/0.git/info/refs?service=git-upload-pack'
        assert metrics['num_redirects'] == '0' and metrics['ssl_verify_result'] == '0'
        start, finish = [datetime.fromisoformat(rec[key]) for key in ('start_utc', 'finish_utc')]
        assert start <= finish
        if previous_finish is not None: assert previous_finish <= start
        previous_finish = finish
        command = rec['command'][:]
        for flag in ('--dump-header', '--output'):
            command[command.index(flag)+1] = '<capture>'
        command[-1] = '<endpoint>'
        if settings is None: settings = command
        assert command == settings
        assert command[command.index('--max-time')+1] == '45'
        assert command[command.index('--retry')+1] == '0'
        status = metrics['http_code']
        if rec['curl_exit'] == 0:
            assert status == ('200' if endpoint == 'orgmode' else '500')
            if endpoint == 'orgmode': views[rec['id']] = parse_view(bodies[rec['id']])
            else: assert bodies[rec['id']] == b'Internal Server Error'
            status_counts['HTTP ' + status] += 1
        else:
            assert rec['curl_exit'] == 28 and status == '000' and rec['body_present'] is False
            status_counts['timeout without HTTP response'] += 1
        attempt = {'record': str(recpath.relative_to(ROOT)), 'id': rec['id'], 'start_utc': rec['start_utc'], 'finish_utc': rec['finish_utc'], 'curl_exit': rec['curl_exit'], 'http_code': status, 'client_wait_seconds': metrics['time_total'], 'completed_response': rec['curl_exit'] == 0}
        attempts.append(attempt)
        if endpoint == 'orgmode': slots.append(attempt)
    absent = expected[len(records):]
    missing_slots.extend({'directory': str(p.relative_to(ROOT)), 'id': rid, 'kind': 'not attempted after stop'} for rid in absent)
    firstcomp = next(c for c in comparison['comparisons'] if c['id'] == 'r1-orgmode')
    pointer = firstcomp.get('previous_complete_capture', firstcomp.get('previous_capture'))
    assert pointer
    priorpath = (ROOT / pointer).resolve()
    if last_complete is not None: assert priorpath == last_complete
    prior = load(priorpath)
    priorbody = raw(priorpath.with_suffix('.body'))
    assert prior['curl_exit'] == 0 and prior['curl_metrics']['http_code'] == '200'
    assert sha256(priorbody).hexdigest() == prior['body_sha256']
    priorview = parse_view(priorbody)
    firstview = views['r1-orgmode']
    changed = firstview['references'] != priorview['references']
    assert firstview['capabilities'] == priorview['capabilities']
    assert set(firstview['references']) == set(priorview['references'])
    assert firstcomp['body_equal_to_previous'] == (bodies['r1-orgmode'] == priorbody)
    if changed:
        assert priorbody.replace(priorview['references']['HEAD'].encode(), firstview['references']['HEAD'].encode()) == bodies['r1-orgmode']
    for rid, view in views.items():
        assert view == firstview and bodies[rid] == bodies['r1-orgmode']
        last_complete = (p / (rid + '.json')).resolve()
    assert len(slots) == 2, 'This audit expects both orgmode slots to have been attempted.'
    complete_pair = all(slot['completed_response'] for slot in slots)
    long_wait = any(Decimal(slot['client_wait_seconds']) >= Decimal('1') for slot in slots)
    change_label = 'changed' if changed else 'unchanged'
    wait_label = 'at_least_one_ge_1s' if long_wait else 'both_below_1s'
    wait_table[(change_label, wait_label)] += 1
    if complete_pair: complete_table[(change_label, wait_label)] += 1
    row = {'directory': str(p.relative_to(ROOT)), 'start_utc': records[0]['start_utc'], 'previous_complete_capture': pointer, 'first_advertised_map_changed': changed, 'orgmode_slots': slots, 'complete_response_pair': complete_pair, 'at_least_one_client_wait_ge_1s': long_wait, 'unattempted_slots': absent, 'stopped_reason': stopped}
    rows.append(row)

def table(counter):
    return [{'view': c, 'wait_label': w, 'visits': counter[c,w]} for c in ('changed', 'unchanged') for w in ('at_least_one_ge_1s', 'both_below_1s')]

# The preceding eight-visit calculation should be an exact contained slice.
old = load(ROOT / 'evidence/gardener-2026-10-19-saved-comparison/analysis.json')
for oldrow in old['rows']:
    row = next(r for r in rows if r['directory'] == oldrow['directory'])
    assert row['first_advertised_map_changed'] == oldrow['changed_advertised_map']
    assert [s['client_wait_seconds'] for s in row['orgmode_slots']] == oldrow['orgmode_time_total_seconds']

summary = {'analysis_date': '2026-10-19', 'visit_count': len(rows), 'planned_slots': len(expected)*len(rows), 'attempted_requests': len(attempts), 'unattempted_slots': missing_slots, 'outcomes': dict(status_counts), 'complete_response_pair_visits': sum(r['complete_response_pair'] for r in rows), 'interrupted_visits': sum(not r['complete_response_pair'] for r in rows), 'complete_response_pair_table': table(complete_table), 'all_attempted_client_wait_table': table(wait_table), 'rows': rows, 'attempts': attempts, 'input_sha256': used, 'request_settings_equal': True, 'previous_eight_visit_slice_reproduced': True}
(OUT / 'analysis.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('rows', 'attempts', 'input_sha256')}, indent=2))
for row in rows:
    print(Path(row['directory']).name, 'changed', row['first_advertised_map_changed'], 'complete', row['complete_response_pair'], [s['client_wait_seconds'] for s in row['orgmode_slots']])
print('INPUT HASHES', len(used))
