"""Offline self-check of this finite visit. No network or machinery changes."""
from collections import Counter
from datetime import datetime
from pathlib import Path
import hashlib
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
PRE = '--pre-close' in sys.argv
sha = lambda data: hashlib.sha256(data).hexdigest()
dt = datetime.fromisoformat
load = lambda name: json.loads((HERE / name).read_text())
before, manifest, comparison = (load(n) for n in ('before.json', 'manifest.json', 'comparison.json'))
origin, sources = load('collector-source.json'), load('sources.json')
readme = (HERE / 'README.md').read_text()
assert sha(readme.split('\n## What arrived\n', 1)[0].encode()) == before['plan_sha256']
for record, pkey, hkey in ((origin, 'path', 'sha256'),
                           (before, 'parser_path', 'parser_sha256'),
                           (sources, 'helper_path', 'helper_sha256')):
    path = (ROOT / record[pkey]).resolve()
    assert path.is_relative_to(ROOT)
    assert sha(path.read_bytes()) == record[hkey]
parse = runpy.run_path(str(ROOT / before['parser_path']))['parse']
previous = ROOT / origin['baseline']
prior = json.loads((previous / 'manifest.json').read_text())['records']
records = manifest['records']
assert len(records) == manifest['planned_maximum_requests'] == 6
assert manifest['stop_reason'] is None
assert len(comparison['comparisons']) == len(records)
last_finish = None
counts = Counter()
for rec, comp in zip(records, comparison['comparisons']):
    rid, metrics, cmd = rec['id'], rec['curl_metrics'], rec['command']
    body = (HERE / (rid + '.body')).read_bytes()
    assert rec == load(rid + '.json')
    assert rec['body_present'] and len(body) == rec['body_bytes'] and sha(body) == rec['body_sha256']
    assert rec['curl_exit'] == 0 and rec['stderr'] == ''
    assert metrics['ssl_verify_result'] == metrics['num_redirects'] == '0'
    assert 0 < float(metrics['time_total']) < 1
    assert float(metrics['size_download']) == len(body)
    assert dt(rec['start_utc']) <= dt(rec['finish_utc'])
    assert rec['process_elapsed_monotonic_seconds'] >= float(metrics['time_total'])
    if last_finish:
        assert last_finish <= dt(rec['start_utc'])
    last_finish = dt(rec['finish_utc'])
    assert cmd[:2] == ['curl', '--disable'] and cmd[-1] == rec['url']
    for flag, value in (('--retry', '0'), ('--max-time', '45'),
                        ('--connect-timeout', '10'), ('--max-filesize', '1048576')):
        assert cmd[cmd.index(flag) + 1] == value
    assert 'Git-Protocol: version=0' in cmd and 'Accept-Encoding: identity' in cmd
    assert not {'--location', '--insecure', '--user', '--cookie'} & set(cmd)
    assert (HERE / (rid + '.headers')).is_file()
    assert rid == comp['id'] and comp['parse_problem'] is None
    oldpath = ROOT / comp['previous_complete_capture']
    oldbody = oldpath.with_suffix('.body').read_bytes()
    assert sha(oldbody) == json.loads(oldpath.read_text())['body_sha256']
    assert comp['body_equal_to_previous'] == (body == oldbody)
    if rid.endswith('orgmode'):
        assert metrics['http_code'] == '200' and len(body) == 370
        assert parse(body) == comp['parsed']
    else:
        assert metrics['http_code'] == '500' and body == b'Internal Server Error'
        assert comp['body_equal_to_previous'] and comp['parsed'] is None
    counts[metrics['http_code']] += 1
    row = '| ' + ' | '.join((rid, dt(rec['start_utc']).strftime('%H:%M:%S.%f'),
        dt(rec['finish_utc']).strftime('%H:%M:%S.%f'), metrics['http_code'],
        str(len(body)), metrics['time_total'])) + ' |'
    assert row in readme
assert counts == {'200': 2, '500': 4}
old, new = (previous / 'r2-orgmode.body').read_bytes(), (HERE / 'r1-orgmode.body').read_bytes()
a, b = parse(old), parse(new)
oid, nid = a['references']['HEAD'], b['references']['HEAD']
assert oid != nid and a['references'].keys() == b['references'].keys()
assert a['capabilities'] == b['capabilities']
assert b['references']['HEAD'] == b['references']['refs/heads/master']
assert old.count(oid.encode()) == 2 and old.replace(oid.encode(), nid.encode()) == new
assert new == (HERE / 'r2-orgmode.body').read_bytes()
assert oid in readme and nid in readme and sha(new) in readme
spans = {
    'observation_window_seconds': (dt(records[-1]['finish_utc']) - dt(records[0]['start_utc'])).total_seconds(),
    'previous_attempt_finish_to_start_seconds': (dt(records[0]['start_utc']) - dt(prior[-1]['finish_utc'])).total_seconds(),
    'previous_complete_orgmode_finish_to_start_seconds': (dt(records[0]['start_utc']) - dt(prior[3]['finish_utc'])).total_seconds(),
}
for key, value in spans.items():
    assert value == comparison[key] and f'{value:,.6f}' in readme
word = (ROOT / 'words/latency-by-outcome.md').read_text()
for status in ('200', '500'):
    values = [float(r['curl_metrics']['time_total']) for r in records if r['curl_metrics']['http_code'] == status]
    expected = f'{min(values):.6f}–{max(values):.6f}'
    assert expected in readme and expected in word
assert len(sources['sources']) == 4
assert last_finish is not None
for source in sources['sources']:
    data = (HERE / source['file']).read_bytes()
    assert source['http_status'] == '200' and source['curl_exit'] == 0
    assert len(data) == source['bytes'] and sha(data) == source['sha256']
    assert source['url'] in readme and dt(source['start_utc']) >= last_finish
assert 'track error latency, as opposed to just filtering out errors' in (HERE / 'monitoring-text.txt').read_text()


def check_links(text, base):
    for name in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
        assert any((ROOT / d / (name + '.md')).is_file() for d in ('rooms', 'words', '')), name
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^()]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        path = (base / target.split('#', 1)[0]).resolve()
        assert path.is_relative_to(ROOT), target
        if path == HERE / 'verification.json':
            continue
        assert path.is_file(), target


sections = {
    'rooms/what-the-gaps-can-say.md': ('## Keep the path beside the outcome — 2026-10-18, 17:30 UTC\n', '## Sources\n'),
    'rooms/measuring-the-window.md': ('## The gap still has no fault boundaries — 2026-10-18, 17:30 UTC\n', 'Links:\n'),
    'words/latency-by-outcome.md': ('## Keep the request beside the result — 2026-10-18\n', 'Links: '),
}
for rel, (start, end) in sections.items():
    path = ROOT / rel
    text = path.read_text()
    prefix, rest = text.split(start)
    added, suffix = rest.split(end, 1)
    assert sha((prefix + end + suffix).encode()) == before['content_hashes'][rel]
    assert text.startswith('# ' + path.stem + '\n')
    assert 'uncertain:' in added and '2026-10-18' in added
    if rel.startswith('rooms/'):
        assert text.splitlines()[2].startswith('*') and text.splitlines()[2].endswith('*')
    else:
        assert text.rstrip().splitlines()[-1].startswith('Links: ')
    check_links(added, path.parent)
allowed = set(sections) | {'gate.md', 'chronicle.md'}
for rel, expected in before['content_hashes'].items():
    if rel not in allowed:
        assert sha((ROOT / rel).read_bytes()) == expected, rel
current = {str(p.relative_to(ROOT)) for d in ('rooms', 'words') for p in (ROOT / d).glob('*.md')}
old_paths = {p for p in before['content_hashes'] if p.startswith(('rooms/', 'words/'))}
assert current == old_paths

gate = (ROOT / 'gate.md').read_text()
old_line = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — changed Git lists leave their history unseen; time useful replies and errors separately, without throwing the errors away (updated 2026-10-18)'
new_line = '- [what-the-gaps-can-say](rooms/what-the-gaps-can-say.md) — changed Git lists leave their history unseen; keep the request path and outcome beside each waiting time, including failures (updated 2026-10-18)'
assert gate.count(new_line) == 1
assert sha(gate.replace(new_line, old_line).encode()) == before['content_hashes']['gate.md']
entries = re.findall(r'^- \[[^\]]+\]\(rooms/([^()]+\.md)\)', gate.split('## Map\n', 1)[1].split('\n## ', 1)[0], re.M)
rooms = {p.name for p in (ROOT / 'rooms').glob('*.md')}
assert set(entries) == rooms and all(n == 1 for n in Counter(entries).values())
garden = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()}
assert garden == before['garden_hashes']
open_qs = [(n, line) for n, line in enumerate((ROOT / 'questions.md').read_text().splitlines(), 1) if line.startswith('- [ ]')]
eligible = [n for n, line in open_qs if not re.search(r'commission|waits for: yu|yu decides|another builder', line, re.I)]
assert len(open_qs) == 16 and eligible == [740, 744, 766]
assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8
assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())
check_links(readme, HERE)
chronicle = (ROOT / 'chronicle.md').read_bytes()
prefix, suffix = chronicle[:before['chronicle_bytes']], chronicle[before['chronicle_bytes']:].decode()
assert sha(prefix) == before['content_hashes']['chronicle.md']
if PRE:
    assert suffix == ''
else:
    assert re.fullmatch(r'- 2026-10-18 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', suffix)
result = {
    'result': 'PASS', 'phase': 'pre-close' if PRE else 'closed',
    'service_requests': len(records), 'public_searches': 1, 'primary_documents_read': 3,
    'advertisement_changed': oid != nid, 'new_orgmode_captures_equal': True,
    'id_replacement_explains_all_changed_bytes': True, 'all_requests_subsecond': True,
    'received_status_counts': dict(counts), 'spans_seconds': spans,
    'room_files_updated': 2, 'word_files_updated': 1, 'new_word_files': 0,
    'map_rooms': len(rooms), 'map_entries': len(entries), 'every_room_listed_once': True,
    'open_questions': len(open_qs), 'researched_still_open': eligible,
    'questions_closed': 0, 'filed': 0, 'planted': 0,
    'courtyard_questions_quests_unchanged': True, 'garden_unchanged': True,
    'earlier_prose_preserved': True, 'new_links_exist': True,
    'chronicle_lines_added': len(suffix.splitlines()),
    'limits': 'Local self-check, not independent review or proof of a service cause.'
}
with (HERE / ('pre-close-verification.json' if PRE else 'verification.json')).open('x') as f:
    json.dump(result, f, indent=2)
    f.write('\n')
print(json.dumps(result, indent=2))
