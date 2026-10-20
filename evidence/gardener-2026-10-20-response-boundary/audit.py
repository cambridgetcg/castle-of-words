"""Audit saved response headers and timing arithmetic; no network calls."""
from collections import Counter
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import re

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

prior = load('evidence/gardener-2026-10-19-first-byte/analysis.json')
for relative, expected in prior['input_sha256'].items():
    assert sha256(read(relative)).hexdigest() == expected, relative
assert len(prior['rows']) == 28
rows = []
for old in prior['rows']:
    path = Path(old['capture'])
    record = load(path)
    header = read(path.with_suffix('.headers'))
    metrics = record['curl_metrics']
    assert record['url'] == 'https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack'
    assert metrics['num_redirects'] == '0'
    assert '--location' not in record['command']
    assert dict(line.split('=', 1) for line in record['stdout'].splitlines()) == metrics
    pre, first, total = [Fraction(metrics[k]) for k in ('time_pretransfer', 'time_starttransfer', 'time_total')]
    parsed = []
    if header:
        assert header.endswith(b'\r\n\r\n')
        for block in header.split(b'\r\n\r\n'):
            if not block:
                continue
            lines = block.decode('iso-8859-1').split('\r\n')
            match = re.fullmatch(r'HTTP/(\d(?:\.\d)?) ([0-9]{3})(?: .*)?', lines[0])
            assert match, lines[0]
            fields = {}
            for line in lines[1:]:
                name, value = line.split(':', 1)
                fields.setdefault(name.lower(), []).append(value.strip())
            parsed.append({'status_line': lines[0], 'version': match[1], 'code': int(match[2]), 'fields': fields})
    if record['curl_exit'] == 0:
        assert old['complete']
        assert len(parsed) == 1 and parsed[0]['code'] == 200
        assert parsed[0]['version'] == metrics['http_version'] == '1.1'
        fields = parsed[0]['fields']
        body = read(path.with_suffix('.body'))
        assert sha256(body).hexdigest() == record['body_sha256']
        assert len(body) == record['body_bytes'] == int(metrics['size_download'])
        # Compare lengths only when declared: some saved responses use chunked framing.
        if 'content-length' in fields:
            assert fields['content-length'] == [str(len(body))]
            assert 'transfer-encoding' not in fields
        else:
            assert fields.get('transfer-encoding') == ['chunked'], (str(path), fields)
        assert fields['content-type'] == ['application/x-git-upload-pack-advertisement']
        assert 'content-encoding' not in fields
        assert 0 <= pre <= first <= total
        assert first - pre == Fraction(old['pretransfer_to_first_byte_seconds'])
        assert total - first == Fraction(old['first_byte_to_finish_seconds'])
        assert pre + (first-pre) + (total-first) == total
        if total >= 1:
            assert (first-pre)/total > Fraction(98, 100)
    else:
        assert record['curl_exit'] == 28 and not old['complete']
        assert parsed == [] and header == b''
        assert metrics['http_code'] == '000' and metrics['size_download'] == '0'
        assert not record['body_present'] and not (ROOT/path.with_suffix('.body')).exists()
        assert first == 0
    rows.append({'capture': str(path), 'start_utc': record['start_utc'],
        'curl_exit': record['curl_exit'], 'status_lines': [p['status_line'] for p in parsed],
        'header_bytes': len(header), 'saved_body_bytes': record.get('body_bytes') if record['body_present'] else None,
        'content_lengths': [p['fields'].get('content-length') for p in parsed],
        'transfer_encodings': [p['fields'].get('transfer-encoding') for p in parsed],
        'informational_responses': sum(100 <= p['code'] < 200 for p in parsed),
        'time_starttransfer': metrics['time_starttransfer'], 'time_total': metrics['time_total'],
        'separate_content_start_timestamp': None})

summary = dict(attempts=len(rows), completed=sum(r['curl_exit'] == 0 for r in rows),
    timed_out=sum(r['curl_exit'] == 28 for r in rows),
    status_line_counts=dict(Counter(s for r in rows for s in r['status_lines'])),
    informational_response_blocks=sum(r['informational_responses'] for r in rows),
    multiple_response_blocks=sum(len(r['status_lines']) > 1 for r in rows),
    headerless_attempts=sum(r['header_bytes'] == 0 for r in rows),
    responses_with_content_length=sum(v is not None for r in rows for v in r['content_lengths']),
    responses_with_chunked_framing=sum(v == ['chunked'] for r in rows for v in r['transfer_encodings']),
    prior_input_hashes_verified=len(prior['input_sha256']),
    prior_timing_partitions_recomputed_exactly=sum(r['curl_exit'] == 0 for r in rows))
result = dict(read_date=datetime.now().astimezone().date().isoformat(),
    scope='Same 28 orgmode attempts from 14 saved visits. No new service traffic. Header dump is not a packet trace.',
    summary=summary, rows=rows, input_sha256=used,
    limits='Only saved client-visible header blocks are inspected. No separately timestamped content arrival, server reference-selection time, hidden update time, delay cause, or event-kind evidence is supplied. Hashes check local consistency, not independent authentication of remote history.')
(OUT/'analysis.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(summary, indent=2))
