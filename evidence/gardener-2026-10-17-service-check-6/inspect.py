"""Offline inspection: missing replies are not changed or matching replies."""
from datetime import datetime
from pathlib import Path
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / 'evidence/gardener-2026-10-17-service-check-5'


def inspect():
    records = json.loads((HERE / 'manifest.json').read_text())['records']
    parse = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'))['parse']
    old = (OLD / 'r2-orgmode.body').read_bytes()
    new = (HERE / 'r1-orgmode.body').read_bytes()
    old_parsed, new_parsed = parse(old), parse(new)
    old_id = old_parsed['references']['HEAD']
    new_id = new_parsed['references']['HEAD']
    old_record = json.loads((OLD / 'r2-orgmode.json').read_text())
    previous_finish = datetime.fromisoformat(old_record['finish_utc'])
    rows, comparisons, timing = [], [], []
    for record in records:
        rid = record['id']
        metrics = record['curl_metrics']
        name = rid.split('-', 1)[1]
        body_path = HERE / (rid + '.body')
        old_body = (OLD / ('r2-' + name + '.body')).read_bytes()
        body = body_path.read_bytes() if body_path.exists() else None
        comparisons.append({'id': rid, 'body_present': body is not None,
                            'body_equal_to_previous': None if body is None else body == old_body})
        status = metrics['http_code'] if metrics['http_code'] != '000' else 'none'
        size = str(record['body_bytes']) if body is not None else 'not received'
        start = datetime.fromisoformat(record['start_utc']).strftime('%H:%M:%S.%f')
        finish = datetime.fromisoformat(record['finish_utc']).strftime('%H:%M:%S.%f')
        rows.append(f'| [{rid}]({rid}.json) | {start} | {finish} | {status} | {record["curl_exit"]} | {size} | {metrics["time_total"]} |')
        # These are client milestones, not component-specific processing clocks.
        first = float(metrics['time_starttransfer'])
        prep = float(metrics['time_pretransfer'])
        timing.append({'id': rid,
                       'pretransfer_to_first_byte_seconds': round(first - prep, 6) if first else None,
                       'pretransfer_to_stop_seconds': round(float(metrics['time_total']) - prep, 6)})
    return {
        'old_id': old_id, 'new_id': new_id,
        'same_reference_names': old_parsed['references'].keys() == new_parsed['references'].keys(),
        'same_capabilities': old_parsed['capabilities'] == new_parsed['capabilities'],
        'id_substitution_explains_all_changed_bytes': old.replace(old_id.encode(), new_id.encode()) == new,
        'new_orgmode_sha256': hashlib.sha256(new).hexdigest(),
        'same_path_gap_seconds': (datetime.fromisoformat(records[0]['start_utc']) - previous_finish).total_seconds(),
        'collection_span_seconds': (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds(),
        'completed_transfer_times_seconds': [float(r['curl_metrics']['time_total']) for r in records if r['curl_exit'] == 0],
        'timed_out_operation_seconds': [float(r['curl_metrics']['time_total']) for r in records if r['curl_exit'] == 28],
        'body_comparisons': comparisons,
        'client_milestone_differences': timing,
        'table_rows': rows,
    }


if __name__ == '__main__':
    result = inspect()
    with (HERE / 'inspection.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))
