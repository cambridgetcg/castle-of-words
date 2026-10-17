"""Offline, focused same-session verification; never requests a URL."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
import ast
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
PRE = '--pre-close' in sys.argv
checks = []

def check(ok, name):
    if not ok:
        raise AssertionError(name)
    checks.append(name)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def load(name):
    return json.loads((HERE / name).read_text())

def decode(data):
    """Separate minimal decoder for these actual SHA-1 v0 captures."""
    cursor = 0
    packets = []
    while cursor < len(data):
        prefix = data[cursor:cursor+4]
        check(re.fullmatch(rb'[0-9a-f]{4}', prefix) is not None, 'packet length is hex')
        length = int(prefix, 16)
        if length == 0:
            packets.append(None)
            cursor += 4
        else:
            check(4 <= length <= 65520 and cursor + length <= len(data), 'packet length within body')
            packets.append(data[cursor+4:cursor+length])
            cursor += length
    check(packets[0] == b'# service=git-upload-pack\n' and packets[1] is None and packets[-1] is None,
          'service envelope and flushes')
    refs, caps = {}, []
    for index, packet in enumerate(packets[2:-1]):
        assert packet is not None, 'unexpected flush inside references'
        check(packet.endswith(b'\n'), 'reference packet has newline')
        line = packet[:-1]
        if index == 0:
            line, raw_caps = line.split(b'\0', 1)
            caps = raw_caps.decode('ascii').split(' ')
        oid, name = line.decode('ascii').split(' ', 1)
        check(re.fullmatch(r'[0-9a-f]{40}', oid) is not None and name not in refs, 'unique SHA-1 reference')
        refs[name] = oid
    return {'references': refs, 'capabilities': caps, 'packet_count': len(packets)}

before, manifest, comparison = load('before.json'), load('manifest.json'), load('comparison.json')
records = manifest['records']
check([r['id'] for r in records] == [f'r{i}-{s}' for i in (1, 2) for s in ('orgmode', 'emacs', 'guix')],
      'exactly six planned sequential requests')
check(manifest['stopped_reason'] is None, 'no recorded stop trigger')
check(sha((ROOT / manifest['parser_path']).read_bytes()) == manifest['parser_sha256'], 'collector decoder source unchanged')
readme = (HERE / 'README.md').read_text()
previous_dir = ROOT / 'evidence/gardener-2026-10-16-service-check-5'
parsed = []
for rec, comp, calc in zip(records, comparison['comparisons'], load('timing-calculations.json')):
    rid, metrics, command = rec['id'], rec['curl_metrics'], rec['command']
    check(load(rid + '.json') == rec, rid + ': manifest agrees with capture')
    check(comp['id'] == rid == calc['id'], rid + ': comparison alignment')
    body, headers = (HERE / (rid + '.body')).read_bytes(), (HERE / (rid + '.headers')).read_bytes()
    check(rec['body_present'] and len(body) == rec['body_bytes'] == int(metrics['size_download'])
          and sha(body) == rec['body_sha256'], rid + ': actual body size/hash')
    expected_status = '200' if rid.endswith('orgmode') else '500'
    check(metrics['http_code'] == expected_status and headers.startswith(('HTTP/1.1 ' + expected_status).encode()),
          rid + ': HTTP status agrees with raw headers')
    check(rec['curl_exit'] == 0 and not rec['stderr'] and metrics['num_redirects'] == '0'
          and metrics['ssl_verify_result'] == '0' and metrics['proxy_used'] == '0', rid + ': completed profile')
    for option, value in [('--retry', '0'), ('--max-time', '45'), ('--connect-timeout', '10'),
                          ('--max-filesize', '1048576'), ('--user-agent', 'castle-gardener/1.0')]:
        check(command[command.index(option)+1] == value, rid + ': ' + option)
    check(command[1] == '--disable' and not set(command).intersection({'-k', '--insecure', '-L', '--location', '--user', '--cookie'}),
          rid + ': no redirect, credentials or insecure TLS')
    check('Accept-Encoding: identity' in command and 'Git-Protocol: version=0' in command, rid + ': comparable headers')
    name = rid.split('-', 1)[1]
    oldbody = (previous_dir / f'r2-{name}.body').read_bytes()
    oldrec = json.loads((previous_dir / f'r2-{name}.json').read_text())
    check(sha(oldbody) == oldrec['body_sha256'] and body == oldbody and comp['body_equal_to_previous'],
          rid + ': actual bytes match previous capture')
    if expected_status == '200':
        view = decode(body)
        check(view == comp['parsed'] and comp['parse_problem'] is None, rid + ': independently decoded view')
        parsed.append(view)
    else:
        check(body == b'Internal Server Error', rid + ': retained error bytes')
    start, finish = datetime.fromisoformat(rec['start_utc']), datetime.fromisoformat(rec['finish_utc'])
    check(start < finish and rec['process_elapsed_monotonic_seconds'] > 0, rid + ': time order')
    check(abs((finish - start).total_seconds() - rec['process_elapsed_monotonic_seconds']) < 0.01,
          rid + ': calendar/process durations consistent within 0.01 second')
    check(Decimal(calc['pretransfer_to_first_byte_seconds']) == Decimal(metrics['time_starttransfer']) - Decimal(metrics['time_pretransfer'])
          and Decimal(calc['first_byte_to_finish_seconds']) == Decimal(metrics['time_total']) - Decimal(metrics['time_starttransfer']),
          rid + ': decimal timing subtraction')
    check(all(value in readme for value in (start.strftime('%H:%M:%S.%f'), finish.strftime('%H:%M:%S.%f'), metrics['time_total'])),
          rid + ': receipt includes actual stamps and time')
check(parsed[0] == parsed[1], 'both decoded advertised views agree')
check(all(datetime.fromisoformat(a['finish_utc']) < datetime.fromisoformat(b['start_utc']) for a, b in zip(records, records[1:])),
      'no request intervals overlap')
span = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
check(span == comparison['window_seconds'] == 55.067392, 'collection span recomputed')
old_manifest = json.loads((previous_dir / 'manifest.json').read_text())
gap = (datetime.fromisoformat(records[0]['start_utc']) - datetime.fromisoformat(old_manifest['records'][-1]['finish_utc'])).total_seconds()
check(gap == comparison['previous_finish_to_start_seconds'], 'unobserved gap recomputed')
for source in load('sources.json'):
    data = (HERE / source['file']).read_bytes()
    check(sha(data) == source['sha256'] and len(data) == source['bytes'] and source['http_status'] == '200' and source['curl_exit'] == 0,
          'source integrity: ' + source['file'])
    check(datetime.fromisoformat(source['start_utc']) > datetime.fromisoformat(records[-1]['finish_utc']),
          'source retrieval after observations: ' + source['file'])

questions = (ROOT / 'questions.md').read_text().splitlines()
check(len(questions) == len(before['question_lines_sha256']), 'no question lines added or removed')
changed = [i for i, s in enumerate(questions, 1) if sha(s.encode()) != before['question_lines_sha256'][str(i)]]
check(changed == [740, 744, 766], 'only three eligible questions changed; reserved questions intact')
for line_number in changed:
    line = questions[line_number-1]
    old, count = re.subn(r'\(observed 2026-10-17 02:53–02:54 UTC; still open — \[morning bounded check\].*?\[\[response-time\]\]\) ', '', line)
    check(count == 1 and sha(old.encode()) == before['question_lines_sha256'][str(line_number)],
          f'question {line_number}: only the new observation note was added')
check([i for i, s in enumerate(questions, 1) if s.startswith('- [ ]')] == before['open_question_lines']
      and len(before['open_question_lines']) == 16, 'sixteen questions remain open; none planted or falsely closed')
for path in ('courtyard.md', 'quests.md', 'words/reference-advertisement.md'):
    check(sha((ROOT / path).read_bytes()) == before['tracked_sha256'][path], path + ': unchanged')
check(not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines()), 'empty courtyard; filed zero')

gate = (ROOT / 'gate.md').read_text()
map_section = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\((rooms/[^)]+\.md)\)', map_section, re.M)
rooms = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'rooms').glob('*.md'))
check(rooms == before['room_paths'] and len(rooms) == 697, 'no rooms added or removed')
check(set(entries) == set(rooms) and all(n == 1 for n in Counter(entries).values()), 'all 697 rooms listed once in Map')
for name in ('what-the-gaps-can-say', 'measuring-the-window'):
    text = (ROOT / 'rooms' / (name + '.md')).read_text()
    nonempty = [s for s in text.splitlines() if s.strip()]
    check(nonempty[0] == '# ' + name and nonempty[1].startswith('*') and nonempty[1].endswith('*')
          and not nonempty[2].startswith(('#', '*')), name + ': room shape retained')
    check('gardener-2026-10-17-service-check/README.md' in text and 'uncertain:' in text,
          name + ': receipt and uncertainty recorded')
word = (ROOT / 'words/response-time.md').read_text()
check(word.startswith('# response-time\n\nResponse time is ') and word.rstrip().splitlines()[-1].startswith('Links: '),
      'word keeps simple opening and final Links line')
for name in ('response-time', 'timeout', 'reference-advertisement', 'visibility-filter', 'http-status',
             'observation-window', 'measurement-target'):
    check((ROOT / 'words' / (name + '.md')).is_file(), 'linked word exists: ' + name)
current_garden = {}
for p in sorted((ROOT / 'garden').rglob('*')):
    if p.is_file() and not p.is_symlink():
        check(p.resolve().is_relative_to(ROOT), 'garden file stays on grounds')
        current_garden[str(p.relative_to(ROOT))] = sha(p.read_bytes())
check(current_garden == before['garden_sha256'], 'garden file set and hashes unchanged')

chronicle = (ROOT / 'chronicle.md').read_bytes()
check(sha(chronicle[:before['chronicle_bytes']]) == before['tracked_sha256']['chronicle.md'], 'all prior chronicle bytes preserved')
addition = chronicle[before['chronicle_bytes']:].decode()
if PRE:
    check(addition == '', 'chronicle not closed before verification')
else:
    check(re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', addition) is not None,
          'exactly one correctly shaped chronicle line appended')
for script in HERE.glob('*.py'):
    ast.parse(script.read_text(), filename=str(script))
    check(True, 'syntax: ' + script.name)
report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'mode': 'pre-close' if PRE else 'final',
          'result': 'PASS', 'checks_passed': len(checks), 'filed': 0, 'researched': 3, 'answered': 0,
          'planted': 0, 'open_questions': 16, 'rooms': len(rooms), 'map_entries': len(entries),
          'garden_unchanged': True, 'chronicle_line_added': not PRE, 'checks': checks}
filename = 'pre-close-verification.json' if PRE else 'verification.json'
with (HERE / filename).open('x') as f:
    json.dump(report, f, indent=2)
    f.write('\n')
print(json.dumps({k: v for k, v in report.items() if k != 'checks'}, indent=2))
print('Local close time:', datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z'))
