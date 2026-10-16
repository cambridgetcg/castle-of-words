"""Offline, same-session verification. Never imports or runs the collector."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from io import BytesIO
from pathlib import Path
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
PRE_CLOSE = '--pre-close' in sys.argv


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text())


def decode(body):
    """A second implementation, using a stream, for these v0 SHA-1 captures."""
    stream = BytesIO(body)
    frames = []
    while stream.tell() < len(body):
        header = stream.read(4)
        assert re.fullmatch(rb'[0-9a-f]{4}', header)
        length = int(header, 16)
        if length == 0:
            frames.append(None)
        else:
            assert 4 <= length <= 65520
            payload = stream.read(length-4)
            assert len(payload) == length-4
            frames.append(payload.rstrip(b'\n'))
    assert frames[0] == b'# service=git-upload-pack'
    assert frames[1] is None and frames[-1] is None
    assert len(frames) == 5, 'narrow verifier expects the observed two-reference form'
    first_ref, capabilities = frames[2].split(b'\x00')
    refs = {}
    for line in (first_ref, frames[3]):
        oid, name = line.decode('ascii').split(' ', 1)
        assert re.fullmatch('[0-9a-f]{40}', oid)
        assert name not in refs
        refs[name] = oid
    return refs, capabilities.decode('ascii').split()


before = load(HERE/'before.json')
manifest = load(HERE/'manifest.json')
comparison = load(HERE/'comparison.json')
calc = load(HERE/'calculations.json')
rows = manifest['records']
assert [r['id'] for r in rows] == ['r1-orgmode', 'r1-emacs', 'r1-guix']
assert [r['curl_exit'] for r in rows] == [0, 0, 28]
assert [r['curl_metrics']['http_code'] for r in rows] == ['200', '500', '000']
assert manifest['stopped_reason'] and manifest['retries'] == 0
assert not manifest['redirects_followed'] and not manifest['new_watch_started']
assert 'curl 8.7.1 ' in manifest['curl_version']
assert not list(HERE.glob('r2-*')), 'stop rule must leave the entire second round unrun'
for i, r in enumerate(rows):
    assert load(HERE/f'{r["id"]}.json') == r
    cmd = r['command']
    assert cmd[:2] == ['curl', '--disable']
    for flag, value in [('--retry', '0'), ('--max-time', '45'), ('--connect-timeout', '10'),
                        ('--max-filesize', '1048576'), ('--proto', '=https')]:
        assert cmd[cmd.index(flag)+1] == value
    assert not set(cmd) & {'--location', '-L', '--insecure', '-k', '--netrc', '--user'}
    assert r['curl_metrics']['proxy_used'] == '0'
    assert r['curl_metrics']['num_redirects'] == '0'
    assert r['curl_metrics']['ssl_verify_result'] == '0'
    assert datetime.fromisoformat(r['finish_utc']) > datetime.fromisoformat(r['start_utc'])
    if i:
        assert datetime.fromisoformat(r['start_utc']) >= datetime.fromisoformat(rows[i-1]['finish_utc'])
    assert r['process_elapsed_monotonic_seconds'] > float(r['curl_metrics']['time_total'])

all_records, advertisements, errors = [], [], []
for suffix in ('', '-2', '-3', '-4'):
    directory = ROOT/'evidence'/('gardener-2026-10-16-service-check'+suffix)
    for r in load(directory/'manifest.json')['records']:
        bp = directory/f'{r["id"]}.body'
        assert bp.exists() == r['body_present']
        hp = directory/f'{r["id"]}.headers'
        headers = hp.read_bytes()
        if r['body_present']:
            body = bp.read_bytes()
            assert len(body) == r['body_bytes'] == int(r['curl_metrics']['size_download'])
            assert sha(body) == r['body_sha256']
            assert re.search(rb'^HTTP/\S+ '+r['curl_metrics']['http_code'].encode()+rb'\b', headers, re.M)
            if r['curl_metrics']['http_code'] == '200':
                assert r['curl_metrics']['content_type'].split(';')[0] == 'application/x-git-upload-pack-advertisement'
                refs, caps = decode(body)
                expected = comparison['captures'][f'{directory.name}/{r["id"]}']['parsed']
                assert refs == expected['references'] and caps == expected['capabilities']
                advertisements.append((body, refs, caps, r))
            else:
                assert r['curl_metrics']['http_code'] == '500'
                assert body == b'Internal Server Error'
                errors.append(body)
        else:
            assert directory == HERE and r['id'] == 'r1-guix'
            assert headers == b'' and r['body_bytes'] is None and r['body_sha256'] is None
            assert r['curl_metrics']['size_download'] == '0'
            assert 'Operation timed out after 45112 milliseconds with 0 bytes received' in r['stderr']
        all_records.append(r)
assert len(all_records) == 21 and len(advertisements) == 7 and len(errors) == 13
for body, refs, caps, r in advertisements:
    assert (body, refs, caps) == advertisements[0][:3]
    assert all(r[key] == advertisements[0][3][key] for key in ('url', 'method', 'request_headers'))
assert advertisements[-1][1] == {'HEAD': 'ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb',
                                'refs/heads/master': 'ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb'}
assert sha(advertisements[-1][0]) == '5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e'
assert sha(errors[-1]) == 'e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62'
for pair, previous, current in zip(comparison['pairs'], advertisements, advertisements[1:]):
    assert pair['body_byte_equal'] and pair['references_equal'] and pair['capabilities_equal']
    a, b = previous[3], current[3]
    assert pair['request_start_spacing_seconds'] == (datetime.fromisoformat(b['start_utc'])-datetime.fromisoformat(a['start_utc'])).total_seconds()
    assert pair['between_processes_seconds'] == (datetime.fromisoformat(b['start_utc'])-datetime.fromisoformat(a['finish_utc'])).total_seconds()
window = (datetime.fromisoformat(rows[-1]['finish_utc'])-datetime.fromisoformat(rows[0]['start_utc'])).total_seconds()
assert window == comparison['observation_window_seconds'] == calc['observation_window_seconds'] == 46.640271
metrics = rows[-1]['curl_metrics']
assert Decimal(metrics['time_total'])-Decimal(metrics['time_pretransfer']) == Decimal(calc['elapsed_after_pretransfer_seconds']) == Decimal('44.820414')
assert metrics['time_starttransfer'] == '0.000000'
assert [float(metrics[k]) for k in ['time_namelookup','time_connect','time_appconnect','time_pretransfer']] == sorted(float(metrics[k]) for k in ['time_namelookup','time_connect','time_appconnect','time_pretransfer'])

sources = load(HERE/'sources.json')
for source in sources:
    assert source['http_status'] == '200' and source['curl_exit'] == 0
    assert sha((HERE/source['file']).read_bytes()) == source['sha256']
    assert datetime.fromisoformat(source['start_utc']) > datetime.fromisoformat(rows[-1]['finish_utc'])
assert load(HERE/'search-links.json')['results']

questions = (ROOT/'questions.md').read_text().splitlines()
assert len(questions) == len(before['question_lines_sha256'])
changed_questions = [i for i, line in enumerate(questions, 1)
                     if sha(line.encode()) != before['question_lines_sha256'][str(i)]]
assert changed_questions == [740, 744, 766]
for i in changed_questions:
    line = questions[i-1]
    assert line.startswith('- [ ]') and line.count('fourth bounded check') == 1
    start = line.index('(observed 2026-10-16 17:09 UTC;')
    end = line.index('(observed 2026-10-16 13:50 UTC;', start)
    assert sha((line[:start]+line[end:]).encode()) == before['question_lines_sha256'][str(i)]
open_lines = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
assert open_lines == before['open_question_lines'] and len(open_lines) == 16
for name in ('courtyard.md','quests.md','words/name-lookup-time.md'):
    assert sha((ROOT/name).read_bytes()) == before['tracked_sha256'][name]
assert not any(line.startswith('- ') for line in (ROOT/'courtyard.md').read_text().splitlines())

garden = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sorted((ROOT/'garden').rglob('*'))
          if p.is_file() and not p.is_symlink()}
assert garden == before['garden_sha256']
rooms = {p.name for p in (ROOT/'rooms').glob('*.md')}
gate = (ROOT/'gate.md').read_text()
map_section = gate.split('## Map\n',1)[1].split('\n## ',1)[0]
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^/)]+\.md)\)', map_section, re.M)
assert set(entries) == rooms and all(n == 1 for n in Counter(entries).values())
assert len(rooms) == 697

additions = {}
for name, heading, end in [
    ('rooms/what-the-gaps-can-say.md', '## The wait ended without a reply', '## Sources\n'),
    ('rooms/measuring-the-window.md', '## A deadline is not a recovery mark', 'Links:\n'),
]:
    text = (ROOT/name).read_text()
    a, b = text.index(heading), text.index(end, text.index(heading))
    additions[name] = text[a:b]
    assert sha((text[:a]+text[b:]).encode()) == before['tracked_sha256'][name], 'old room text changed'
    blocks = text.strip().split('\n\n')
    assert blocks[0] == '# '+Path(name).stem
    assert blocks[1].startswith('*') and blocks[1].endswith('*')
    assert not blocks[2].startswith(('#','*'))
for name in ('words/response-time.md','words/timeout.md'):
    text = (ROOT/name).read_text()
    blocks = text.strip().split('\n\n')
    assert blocks[0] == '# '+Path(name).stem and not blocks[1].startswith(('#','*'))
    assert text.strip().splitlines()[-1].startswith('Links:') and '[[' in text.strip().splitlines()[-1]
    additions[name] = text
additions[str((HERE/'README.md').relative_to(ROOT))] = (HERE/'README.md').read_text()

pending = {'verification.json'}
local_links_checked = 0
for name, text in additions.items():
    base = (ROOT/name).parent
    for dest in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
        if urlsplit(dest).scheme or dest.startswith('#'):
            continue
        target = (base/unquote(dest.split('#',1)[0])).resolve()
        assert target.is_relative_to(ROOT), (name,dest)
        assert target.exists() or (target.parent == HERE and target.name in pending), (name,dest)
        local_links_checked += 1
    for dest in re.findall(r'\[\[([^\]]+)\]\]', text):
        stem = dest.split('|')[0].split('#')[0]
        assert any((directory/(stem+'.md')).exists() for directory in (ROOT,ROOT/'words',ROOT/'rooms',ROOT/'works')), (name,stem)
        local_links_checked += 1

chronicle = (ROOT/'chronicle.md').read_bytes()
assert sha(chronicle[:before['chronicle_bytes']]) == before['chronicle_sha256']
appended = chronicle[before['chronicle_bytes']:].decode()
if PRE_CLOSE:
    assert not appended, 'chronicle already closed'
else:
    assert appended.count('\n') == 1
    assert re.fullmatch(r'- \d{4}-\d{2}-\d{2} \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', appended)
    assert 'timed-out guix request' in appended

report = {
    'verified_utc': datetime.now(timezone.utc).isoformat(),
    'verification_kind': 'offline same-session recheck, not independent review',
    'result': 'passed', 'attempted_service_requests': len(rows), 'unrun_second_round': True,
    'timed_out_request_kept_as_missing_response': True,
    'retained_operations_checked': len(all_records), 'retained_bodies_checked': len(advertisements)+len(errors),
    'independently_decoded_advertisements': len(advertisements),
    'matching_advertisements': True, 'source_retrievals_checked': len(sources),
    'observation_window_seconds': window, 'after_pretransfer_seconds': calc['elapsed_after_pretransfer_seconds'],
    'changed_question_lines_only': changed_questions, 'open_questions': len(open_lines),
    'courtyard_unchanged_and_empty': True, 'quests_unchanged': True,
    'rooms': len(rooms), 'map_lines': len(entries), 'map_missing_extra_duplicates': [],
    'old_room_text_preserved': True, 'word_and_room_shapes_pass': True,
    'local_links_checked': local_links_checked, 'garden_content_hashes_unchanged': True,
    'chronicle_exactly_one_line_appended': not PRE_CLOSE,
    'chronicle_line': appended.strip() if appended else None,
}
output = 'pre-close-verification.json' if PRE_CLOSE else 'verification.json'
(HERE/output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if PRE_CLOSE:
    print('CHRONICLE_TIME='+datetime.now().astimezone().strftime('%Y-%m-%d %H:%M'))
