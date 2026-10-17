"""Offline comparison and a narrow Via received-by token check; no requests."""
from pathlib import Path
from datetime import datetime
import hashlib
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREVIOUS = ROOT / 'evidence/gardener-2026-10-17-service-check-3'
TOKEN = re.compile(r"[!#$%&'*+.^_`|~0-9A-Za-z-]+\Z")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inspect():
    assert ROOT == Path('/Users/yu/castle')
    parse = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'))['parse']
    records = json.loads((HERE / 'manifest.json').read_text())['records']
    old_body = (PREVIOUS / 'r2-orgmode.body').read_bytes()
    new_body = (HERE / 'r1-orgmode.body').read_bytes()
    old_parsed, new_parsed = parse(old_body), parse(new_body)
    old_id, new_id = (r['references']['HEAD'] for r in (old_parsed, new_parsed))
    headers = []
    for row in records:
        data = (HERE / (row['id'] + '.headers')).read_bytes()
        values = [line.split(':', 1)[1].strip() for line in data.decode('iso-8859-1').splitlines()
                  if line.lower().startswith('via:')]
        # These captures contain one member per field line. This deliberately
        # does not parse arbitrary lists, quoted content, comments or ports.
        assert len(values) == 2 and all(',' not in value for value in values)
        parts = []
        for value in values:
            received_by = value.split()[1]
            assert ':' not in received_by, 'port syntax outside this narrow check'
            parts.append({'raw': value, 'received_by_candidate': received_by,
                          'matches_rfc9110_token': bool(TOKEN.fullmatch(received_by)),
                          'forbidden_characters': sorted({c for c in received_by if not TOKEN.fullmatch(c)})})
        headers.append({'id': row['id'], 'header_sha256': digest(data),
                        'client_proxy_used': row['curl_metrics']['proxy_used'], 'via': parts})
    # Synthetic token cases test only the declared character boundary.
    fixtures = {'varnish': True, 'fred.example': True, 'node-1': True,
                'node/path': False, 'node@build': False, '': False}
    for value, expected in fixtures.items():
        assert bool(TOKEN.fullmatch(value)) == expected
    old_record = json.loads((PREVIOUS / 'r2-orgmode.json').read_text())
    return {
        'old_id': old_id, 'new_id': new_id,
        'same_reference_names': sorted(old_parsed['references']) == sorted(new_parsed['references']),
        'same_capabilities': old_parsed['capabilities'] == new_parsed['capabilities'],
        'id_substitution_explains_all_body_changes': old_body.replace(old_id.encode(), new_id.encode()) == new_body,
        'current_orgmode_bodies_equal': new_body == (HERE / 'r2-orgmode.body').read_bytes(),
        'new_body_sha256': digest(new_body), 'old_body_sha256': digest(old_body),
        'same_path_gap_seconds': (datetime.fromisoformat(records[0]['start_utc']) - datetime.fromisoformat(old_record['finish_utc'])).total_seconds(),
        'header_checks': headers, 'synthetic_token_cases_passed': len(fixtures),
        'scope': 'Received-by token test for these no-port, single-member fields, not a general Via or HTTP validator.'}


def main():
    result = inspect()
    with (HERE / 'inspection.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
