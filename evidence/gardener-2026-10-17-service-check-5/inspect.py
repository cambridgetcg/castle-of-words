"""Check saved advertisements and request intervals, without network access."""
from datetime import datetime
from pathlib import Path
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / 'evidence/gardener-2026-10-17-service-check-4'
PARSER = ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'


def inspect():
    parse = runpy.run_path(str(PARSER))['parse']
    records = json.loads((HERE / 'manifest.json').read_text())['records']
    old_body = (OLD / 'r2-orgmode.body').read_bytes()
    new_body = (HERE / 'r1-orgmode.body').read_bytes()
    old, new = parse(old_body), parse(new_body)
    old_id, new_id = (view['references']['HEAD'] for view in (old, new))
    old_record = json.loads((OLD / 'r2-orgmode.json').read_text())
    return {
        'old_id': old_id,
        'new_id': new_id,
        'same_reference_names': sorted(old['references']) == sorted(new['references']),
        'same_capabilities': old['capabilities'] == new['capabilities'],
        'id_substitution_explains_all_changed_bytes': old_body.replace(old_id.encode(), new_id.encode()) == new_body,
        'current_orgmode_bodies_equal': new_body == (HERE / 'r2-orgmode.body').read_bytes(),
        'new_orgmode_sha256': hashlib.sha256(new_body).hexdigest(),
        'same_path_gap_seconds': (datetime.fromisoformat(records[0]['start_utc']) - datetime.fromisoformat(old_record['finish_utc'])).total_seconds(),
        'table_rows': [
            f"| [{r['id']}]({r['id']}.json) | {datetime.fromisoformat(r['start_utc']).strftime('%H:%M:%S.%f')} | {datetime.fromisoformat(r['finish_utc']).strftime('%H:%M:%S.%f')} | {r['curl_metrics']['http_code']} | {r['body_bytes']} | {r['curl_metrics']['time_total']} |"
            for r in records
        ],
    }


if __name__ == '__main__':
    result = inspect()
    with (HERE / 'inspection.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))
