"""Offline descriptive comparison; no network, database or repository mutation."""
from collections import Counter
from datetime import datetime
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents and 'garden' not in OUT.relative_to(ROOT).parts
used = {}

def safe(path):
    resolved = path.resolve()
    assert ROOT in resolved.parents, resolved
    return resolved

def raw(path):
    path = safe(path)
    data = path.read_bytes()
    used[str(path.relative_to(ROOT))] = sha256(data).hexdigest()
    return data

def load(path):
    return json.loads(raw(path))

def stamp(value):
    return datetime.fromisoformat(value)

def packet_view(body):
    # Limited parser for the saved SHA-1 Git protocol-v0 advertisements.
    packets, pos = [], 0
    while pos < len(body):
        assert re.fullmatch(b'[0-9a-fA-F]{4}', body[pos:pos+4])
        size = int(body[pos:pos+4], 16)
        pos += 4
        if size == 0:
            packets.append(None)
        else:
            assert size >= 4 and pos + size - 4 <= len(body)
            packets.append(body[pos:pos+size-4])
            pos += size - 4
    assert packets[:2] == [b'# service=git-upload-pack\n', None]
    assert packets[-1] is None
    refs, caps = {}, []
    for index, packet in enumerate(packets[2:-1]):
        assert packet is not None
        line = packet.rstrip(b'\n')
        if index == 0:
            namepart, capabilities = line.split(b'\x00', 1)
            caps = capabilities.decode('ascii').split()
        else:
            assert b'\x00' not in line
            namepart = line
        oid, name = namepart.decode('ascii').split(' ', 1)
        assert re.fullmatch('[0-9a-f]{40}', oid) and name not in refs
        refs[name] = oid
    assert refs and len(caps) == len(set(caps))
    return {'references': refs, 'capabilities': caps}

# Metadata snapshot for later scope and append checks; no original file is copied.
before_path = OUT / 'before.json'
if not before_path.exists():
    paths = [ROOT / x for x in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md', 'words/latency-by-outcome.md')]
    paths += sorted((ROOT / 'garden').rglob('*'))
    before = {}
    for path in paths:
        if path.is_file():
            path = safe(path)
            data = path.read_bytes()
            before[str(path.relative_to(ROOT))] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data), 'lines': len(data.splitlines())}
    before_path.write_text(json.dumps(before, indent=2) + '\n')

paths = [ROOT / 'evidence' / ('gardener-2026-10-18-service-check' + ('' if n == 1 else '-' + str(n))) for n in range(1, 9)]
# Ensure the declared slice includes every directory with this exact date/name shape.
found = {p for p in (ROOT / 'evidence').glob('gardener-2026-10-18-service-check*') if p.is_dir() and re.fullmatch(r'gardener-2026-10-18-service-check(?:-[0-9]+)?', p.name)}
assert set(paths) == found
rows, table, bands, status_counts = [], Counter(), {}, Counter()
previous_finish = None
settings = None
for number, path in enumerate(paths, 1):
    manifest = load(path / 'manifest.json')
    comparison = load(path / 'comparison.json')
    records = manifest['records']
    expected_ids = ['r%d-%s' % (r, name) for r in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
    assert [r['id'] for r in records] == expected_ids
    bodies = {}
    for rec in records:
        assert rec == load(path / (rec['id'] + '.json'))
        body = raw(path / (rec['id'] + '.body'))
        assert sha256(body).hexdigest() == rec['body_sha256']
        assert len(body) == rec['body_bytes'] == int(rec['curl_metrics']['size_download'])
        assert rec['curl_exit'] == 0 and rec['curl_metrics']['num_redirects'] == '0'
        assert rec['curl_metrics']['ssl_verify_result'] == '0'
        status_counts[rec['curl_metrics']['http_code']] += 1
        assert rec['url'] == 'https://yhetil.org/' + rec['id'].split('-', 1)[1] + '/0.git/info/refs?service=git-upload-pack'
        start, finish = stamp(rec['start_utc']), stamp(rec['finish_utc'])
        assert start <= finish
        if previous_finish:
            assert start >= previous_finish
        previous_finish = finish
        command = rec['command'][:]
        for flag in ('--dump-header', '--output'):
            command[command.index(flag) + 1] = '<capture>'
        command[-1] = '<same endpoint family>'
        if settings is None:
            settings = command
        assert settings == command
        bodies[rec['id']] = body
        if not rec['id'].endswith('orgmode'):
            assert rec['curl_metrics']['http_code'] == '500'
            assert body == b'Internal Server Error'
    org = [r for r in records if r['id'].endswith('orgmode')]
    assert all(r['curl_metrics']['http_code'] == '200' for r in org)
    views = [packet_view(bodies[r['id']]) for r in org]
    assert views[0] == views[1] and bodies['r1-orgmode'] == bodies['r2-orgmode']
    prior_pointer = next(c for c in comparison['comparisons'] if c['id'] == 'r1-orgmode')['previous_complete_capture']
    prior_path = safe(ROOT / prior_pointer)
    prior = load(prior_path)
    prior_body = raw(prior_path.with_suffix('.body'))
    assert sha256(prior_body).hexdigest() == prior['body_sha256']
    assert prior['curl_exit'] == 0 and prior['curl_metrics']['http_code'] == '200'
    prior_view = packet_view(prior_body)
    if number > 1:
        assert prior_path == (paths[number-2] / 'r2-orgmode.json').resolve()
    changed = views[0]['references'] != prior_view['references']
    assert set(views[0]['references']) == set(prior_view['references'])
    assert views[0]['capabilities'] == prior_view['capabilities']
    if changed:
        old_id, new_id = prior_view['references']['HEAD'], views[0]['references']['HEAD']
        assert prior_body.replace(old_id.encode(), new_id.encode()) == bodies['r1-orgmode']
    else:
        assert prior_body == bodies['r1-orgmode']
    times = [Decimal(r['curl_metrics']['time_total']) for r in org]
    slow = any(t >= Decimal('1') for t in times)
    table[('changed' if changed else 'unchanged', 'at_least_1s' if slow else 'both_below_1s')] += 1
    start, finish = stamp(records[0]['start_utc']), stamp(records[-1]['finish_utc'])
    band = '%02d:00–%02d:00 UTC' % ((start.hour // 6) * 6, (start.hour // 6 + 1) * 6)
    bandrow = bands.setdefault(band, {'visits': 0, 'orgmode_requests': 0, 'visits_at_least_1s': 0})
    bandrow['visits'] += 1
    bandrow['orgmode_requests'] += len(org)
    bandrow['visits_at_least_1s'] += int(slow)
    row = {'visit': number, 'directory': str(path.relative_to(ROOT)), 'start_utc': records[0]['start_utc'], 'finish_utc': records[-1]['finish_utc'], 'previous_complete_capture': prior_pointer, 'changed_advertised_map': changed, 'orgmode_time_total_seconds': [str(t) for t in times], 'at_least_one_orgmode_wait_ge_1s': slow, 'collection_span_seconds': round((finish-start).total_seconds(), 6), 'same_path_gap_seconds': round((start-stamp(prior['finish_utc'])).total_seconds(), 6), 'orgmode_head': views[0]['references']['HEAD'], 'utc_band': band}
    rows.append(row)

map_text = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/]+)\.md\)', map_text, re.M)
rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
assert len(entries) == len(set(entries)) and set(entries) == rooms
open_questions = [line for line in (ROOT / 'questions.md').read_text().splitlines() if line.startswith('- [ ] ')]
summary = {'analysis_date': '2026-10-19', 'visit_count': len(rows), 'request_count': sum(status_counts.values()), 'http_status_counts': dict(status_counts), 'table': [{'change': c, 'timing': t, 'visits': table[c,t]} for c in ('changed', 'unchanged') for t in ('at_least_1s', 'both_below_1s')], 'utc_bands': dict(sorted(bands.items())), 'minimum_collection_span_seconds': min(r['collection_span_seconds'] for r in rows), 'maximum_collection_span_seconds': max(r['collection_span_seconds'] for r in rows), 'minimum_same_path_gap_seconds': min(r['same_path_gap_seconds'] for r in rows), 'maximum_same_path_gap_seconds': max(r['same_path_gap_seconds'] for r in rows), 'map_rooms': len(rooms), 'open_questions': len(open_questions), 'all_capture_hashes_validated': True, 'request_settings_equal': True, 'rows': rows, 'input_sha256': used}
(OUT / 'analysis.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k not in ('input_sha256', 'rows')}, indent=2))
for r in rows:
    print(r['visit'], r['start_utc'], 'changed=' + str(r['changed_advertised_map']), r['orgmode_time_total_seconds'], 'collection', r['collection_span_seconds'], 'gap', r['same_path_gap_seconds'])
