"""Recompute a threshold sensitivity table from saved captures only."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents and 'garden' not in OUT.relative_to(ROOT).parts
used = {}

def raw(relative):
    path = (ROOT / relative).resolve()
    assert ROOT in path.parents
    data = path.read_bytes()
    used[str(path.relative_to(ROOT))] = sha256(data).hexdigest()
    return data

def load(relative):
    return json.loads(raw(relative))

def refs(body):
    """Limited parser for the saved protocol-v0 SHA-1 advertisements."""
    packets, pos = [], 0
    while pos < len(body):
        prefix = body[pos:pos+4]
        assert re.fullmatch(b'[0-9a-fA-F]{4}', prefix)
        size = int(prefix, 16)
        pos += 4
        if size == 0:
            packets.append(None)
        else:
            assert size >= 4 and pos + size - 4 <= len(body)
            packets.append(body[pos:pos+size-4])
            pos += size - 4
    assert packets[:2] == [b'# service=git-upload-pack\n', None] and packets[-1] is None
    mapping = {}
    for index, packet in enumerate(packets[2:-1]):
        assert packet is not None
        fields = packet.rstrip(b'\n').split(b'\x00')
        assert len(fields) == (2 if index == 0 else 1)
        oid, name = fields[0].decode('ascii').split(' ', 1)
        assert re.fullmatch(r'[0-9a-f]{40}', oid) and name not in mapping
        mapping[name] = oid
    return mapping

prior = load('evidence/gardener-2026-10-19-saved-comparison/analysis.json')
# Check every previously cited input, not only the derived table.
for relative, digest in prior['input_sha256'].items():
    assert sha256(raw(relative)).hexdigest() == digest, relative
assert prior['visit_count'] == len(prior['rows']) == 8
found = {str(p.relative_to(ROOT)) for p in (ROOT / 'evidence').glob('gardener-2026-10-18-service-check*') if p.is_dir() and re.fullmatch(r'gardener-2026-10-18-service-check(?:-[0-9]+)?', p.name)}
assert found == {r['directory'] for r in prior['rows']}
rows = []
status_counts = Counter()
for old in prior['rows']:
    directory = old['directory']
    manifest = load(directory + '/manifest.json')
    records = manifest['records']
    assert [r['id'] for r in records] == [f'r{r}-{name}' for r in (1,2) for name in ('orgmode','emacs','guix')]
    for rec in records:
        assert load(directory + '/' + rec['id'] + '.json') == rec
        body = raw(directory + '/' + rec['id'] + '.body')
        assert sha256(body).hexdigest() == rec['body_sha256']
        assert len(body) == rec['body_bytes'] == int(rec['curl_metrics']['size_download'])
        assert rec['curl_exit'] == 0
        status_counts[rec['curl_metrics']['http_code']] += 1
    org = [r for r in records if r['id'].endswith('orgmode')]
    assert len(org) == 2 and all(r['curl_metrics']['http_code'] == '200' for r in org)
    bodies = [raw(directory + '/' + r['id'] + '.body') for r in org]
    assert bodies[0] == bodies[1]
    previous = load(old['previous_complete_capture'])
    previous_body = raw(str(Path(old['previous_complete_capture']).with_suffix('.body')))
    assert sha256(previous_body).hexdigest() == previous['body_sha256']
    changed = refs(previous_body) != refs(bodies[0])
    times = [Decimal(r['curl_metrics']['time_total']) for r in org]
    assert changed == old['changed_advertised_map']
    assert [str(t) for t in times] == old['orgmode_time_total_seconds']
    rows.append({'visit': old['visit'], 'directory': directory, 'changed': changed, 'waits_seconds': [str(t) for t in times], 'maximum_seconds': str(max(times))})

def classify(t):
    high_changed = [r['visit'] for r in rows if r['changed'] and Decimal(r['maximum_seconds']) >= t]
    high_unchanged = [r['visit'] for r in rows if not r['changed'] and Decimal(r['maximum_seconds']) >= t]
    cells = [len(high_changed), sum(r['changed'] for r in rows)-len(high_changed), len(high_unchanged), sum(not r['changed'] for r in rows)-len(high_unchanged)]
    return {'cells': cells, 'at_or_above_visits_changed': high_changed, 'at_or_above_visits_unchanged': high_unchanged, 'all_four_cells_nonzero': all(c > 0 for c in cells)}

# These reporting thresholds are retrospective, not chosen for a p-value.
thresholds = [Decimal(x) for x in ('0.5','1','5','10','20','25')]
tables = [dict(threshold_seconds=str(t), **classify(t)) for t in thresholds]
levels = sorted({Decimal(r['maximum_seconds']) for r in rows})
regimes = []
for i, upper in enumerate(levels):
    lower = levels[i-1] if i else Decimal(0)
    regimes.append(dict(lower_exclusive_seconds=str(lower), upper_inclusive_seconds=str(upper), **classify(upper)))
regimes.append(dict(lower_exclusive_seconds=str(levels[-1]), upper_inclusive_seconds=None, **classify(levels[-1] + 1)))
# There is one observed high/low vector throughout this interval, not just the same totals.
reference_threshold = Decimal('1')
low = [Decimal(r['maximum_seconds']) for r in rows if Decimal(r['maximum_seconds']) < reference_threshold]
high = [Decimal(r['maximum_seconds']) for r in rows if Decimal(r['maximum_seconds']) >= reference_threshold]
stable = {'lower_exclusive_seconds': str(max(low)), 'upper_inclusive_seconds': str(min(high)), **classify(reference_threshold)}
assert stable['cells'] == [1, 5, 1, 1]
assert classify(Decimal(stable['upper_inclusive_seconds'])) == classify(reference_threshold)
assert classify(Decimal(stable['lower_exclusive_seconds'])) != classify(reference_threshold)
summary = {'executed_utc': datetime.now(timezone.utc).isoformat(), 'question_researched': 740, 'still_open': True, 'visit_count': len(rows), 'request_count': sum(status_counts.values()), 'status_counts': dict(status_counts), 'cell_order': ['changed_at_or_above', 'changed_below', 'unchanged_at_or_above', 'unchanged_below'], 'rule': 'A visit is at-or-above when max of its two orgmode time_total readings is >= threshold; one visit is one row.', 'rows': rows, 'selected_thresholds': tables, 'all_positive_threshold_regimes': regimes, 'same_labels_as_1s': stable, 'limitations': ['Retrospective descriptive sensitivity analysis, not a preregistered test or a service threshold.', 'No p-value or independence or causal claim.', 'The old observations are not new service measurements.', 'No update times, unseen changes or event boundaries recovered.'], 'input_sha256': used}
(OUT / 'analysis.json').write_text(json.dumps(summary, indent=2) + '\n')
print('Validated saved inputs:', len(used), 'visits:', len(rows), 'requests:', sum(status_counts.values()))
for t in tables:
    print(t['threshold_seconds'], t['cells'])
print('Same labels as 1 second:', json.dumps(stable))
print('All positive threshold regimes:', len(regimes))
