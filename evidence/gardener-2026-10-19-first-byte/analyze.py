"""Decompose saved client timing marks; no network access or collector imports."""
from datetime import datetime, timezone
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
URL = 'https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack'
used = {}

def read(relative):
    path = (ROOT/relative).resolve()
    assert ROOT in path.parents and 'garden' not in path.relative_to(ROOT).parts
    b = path.read_bytes()
    used[str(path.relative_to(ROOT))] = sha256(b).hexdigest()
    return b

def load(relative): return json.loads(read(relative))
def exact(value): return format(value, '.6f')

def capture(relative):
    record = load(relative)
    assert record['url'] == URL
    m = record['curl_metrics']
    assert m['url_effective'] == URL and m['num_redirects'] == '0'
    cmd = record['command']
    assert cmd[cmd.index('--retry')+1] == '0'
    assert cmd[cmd.index('--max-time')+1] == '45'
    assert '--location' not in cmd and '--next' not in cmd
    assert dict(line.split('=', 1) for line in record['stdout'].splitlines()) == m
    body_path = Path(relative).with_suffix('.body')
    if record['curl_exit']:
        assert record['curl_exit'] == 28 and m['http_code'] == '000'
        assert m['time_starttransfer'] == '0.000000' and m['size_download'] == '0'
        assert not record['body_present'] and not (ROOT/body_path).exists()
        assert read(Path(relative).with_suffix('.headers')) == b''
        return record, None
    assert record['body_present'] and m['http_code'] == '200'
    b = read(body_path)
    assert sha256(b).hexdigest() == record['body_sha256'] and len(b) == record['body_bytes']
    packets = []; pos = 0
    while pos < len(b):
        n = int(b[pos:pos+4], 16)
        assert n == 0 or 4 <= n <= len(b)-pos
        packets.append(b[pos+4:pos+n] if n else None)
        pos += n or 4
    assert pos == len(b) and len(packets) == 5
    assert packets[:2] == [b'# service=git-upload-pack\n', None] and packets[-1] is None
    refs = {}
    for part in (packets[2].split(b'\0', 1)[0], packets[3].rstrip(b'\n')):
        oid, name = part.decode('ascii').split(' ')
        assert re.fullmatch('[0-9a-f]{40}', oid) and name not in refs
        refs[name] = oid
    assert set(refs) == {'HEAD', 'refs/heads/master'} and len(set(refs.values())) == 1
    return record, refs

prior = load('evidence/gardener-2026-10-19-request-order/analysis.json')
assert len(prior['rows']) == 14
rows = []
for visit in prior['rows']:
    old, old_refs = capture(visit['previous_complete_capture'])
    directory = Path(visit['directory'])
    first, first_refs = capture(directory/'r1-orgmode.json')
    assert old_refs is not None and first_refs is not None
    changed = first_refs != old_refs
    assert changed == visit['first_view_changed']
    assert datetime.fromisoformat(old['finish_utc']) <= datetime.fromisoformat(first['start_utc'])
    for round_no in (1, 2):
        path = directory/f'r{round_no}-orgmode.json'
        record, refs = capture(path)
        assert refs is None or refs == first_refs
        m = record['curl_metrics']
        pre, first_byte, total = (Decimal(m[key]) for key in ('time_pretransfer', 'time_starttransfer', 'time_total'))
        row: dict = dict(capture=str(path), start_utc=record['start_utc'], round=round_no, complete=refs is not None, view_comparison=('changed from previous complete capture' if changed else 'no detected change from previous complete capture') if round_no == 1 else ('matches this visit\'s first reply' if refs is not None else 'no reply to compare'), pretransfer_seconds=exact(pre), raw_first_byte_seconds=exact(first_byte), total_seconds=exact(total))
        if refs is not None:
            assert 0 <= pre <= first_byte <= total
            parts = [pre, first_byte-pre, total-first_byte]
            assert sum(parts) == total
            row.update(pretransfer_to_first_byte_seconds=exact(parts[1]), first_byte_to_finish_seconds=exact(parts[2]), total_ge_1s=total >= 1, pretransfer_to_first_byte_share_percent=str(parts[1]/total*100))
        else:
            assert total > pre >= 0
            row.update(pretransfer_to_first_byte_seconds=None, first_byte_to_finish_seconds=None, total_ge_1s=None, pretransfer_to_abort_seconds=exact(total-pre))
        rows.append(row)
rows.sort(key=lambda r: r['start_utc'])
complete = [r for r in rows if r['complete']]
slow = [r for r in complete if r['total_ge_1s']]
failed = [r for r in rows if not r['complete']]
summary = dict(visits=len(prior['rows']), attempts=len(rows), completed=len(complete), timed_out=len(failed), completed_ge_1s=len(slow), completed_lt_1s=len(complete)-len(slow), changed_first_views=sum(v['first_view_changed'] for v in prior['rows']), received_rechecks_equal_to_first=sum(r['round'] == 2 for r in complete), slow_max_first_byte_to_finish_seconds=max(Decimal(r['first_byte_to_finish_seconds']) for r in slow), slow_min_pretransfer_to_first_byte_share_percent=min(Decimal(r['pretransfer_to_first_byte_share_percent']) for r in slow))
result = dict(date=datetime.now(timezone.utc).date().isoformat(), scope='Same fourteen saved visits; orgmode only; seconds; inherited descriptive one-second cutoff; no new network observations.', summary=summary, long_completed=slow, timed_out=failed, rows=rows, input_sha256=used, limits='Client milestone differences do not identify server processing, component responsibility, event boundaries or an update-delay association. Timeout zero is not an observed first-byte time. Hashes establish local consistency, not independent remote-history authentication.')
(OUT/'analysis.json').write_text(json.dumps(result, indent=2, default=str)+'\n')
print(json.dumps(dict(summary=summary, long_completed=slow, timed_out=failed, input_hashes=len(used)), indent=2, default=str))
