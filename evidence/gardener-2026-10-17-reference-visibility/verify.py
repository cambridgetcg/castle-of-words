"""Offline, same-session verification. Does not rerun Git or access the network."""
from collections import Counter
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')
PRE = '--pre-close' in sys.argv


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(name):
    return json.loads((HERE / name).read_text())


def decode(data):
    """Separate stream decoder of the actual raw upload-pack reference block."""
    stream = BytesIO(data)
    records = []
    while True:
        prefix = stream.read(4)
        assert len(prefix) == 4 and re.fullmatch(rb'[0-9a-fA-F]{4}', prefix)
        length = int(prefix, 16)
        if length == 0:
            assert stream.read() == b'', 'trailing data after final flush'
            break
        assert 4 <= length <= 65520
        payload = stream.read(length - 4)
        assert len(payload) == length - 4 and payload.endswith(b'\n')
        records.append(payload[:-1])
    references, capabilities = {}, []
    for number, record in enumerate(records):
        if number == 0:
            record, delimiter, capability = record.partition(b'\0')
            assert delimiter
            capabilities = capability.decode('ascii').split(' ')
        oid, sep, name = record.partition(b' ')
        assert sep and re.fullmatch(rb'[0-9a-f]{40}', oid) and name
        assert name.decode() not in references
        references[name.decode()] = oid.decode()
    return {'refs': references, 'capabilities': capabilities, 'packet_count': len(records)+1}


before, result = load('before.json'), load('visibility-result.json')
assert result['all_passed'] and len(result['checks']) == 8 and all(result['checks'].values())
assert result['network_requests'] == 0 and result['fixture_removed']
assert not (HERE / 'local-fixture').exists()
assert sha((HERE / 'check_visibility.py').read_bytes()) == result['script_sha256']
initial = load('initial-visibility-result.json')
assert initial['all_passed'] is False and initial['fixture_removed']
assert initial['error'] == 'AssertionError()'
assert result['git_version'] == 'git version 2.39.5 (Apple Git-154)'
assert datetime.fromisoformat(initial['finished_utc']) < datetime.fromisoformat(result['started_utc'])

captured = {}
for label, key in [('hidden-before', 'hidden_before'), ('hidden-after', 'hidden_after'), ('exposed-after', 'exposed_after')]:
    value = result['captures'][key]
    body = (HERE / (label+'.pkt')).read_bytes()
    stored = (HERE / (label+'-stored-refs.txt')).read_text()
    assert sha(body) == value['body_sha256'] and len(body) == value['body_bytes']
    assert decode(body) == value['advertised']
    assert stored == value['stored_refs']
    stored_map = {}
    for line in stored.splitlines():
        oid, ref = line.split(' ')
        assert ref not in stored_map and re.fullmatch('[0-9a-f]{40}', oid)
        stored_map[ref] = oid
    assert set(stored_map) == {'refs/heads/main', 'refs/heads/private'}
    captured[label] = (body, decode(body), stored_map)

b, a, e = (captured[label] for label in ('hidden-before', 'hidden-after', 'exposed-after'))
assert b[0] == a[0] and b[1] == a[1] and b[2] != a[2]
assert a[0] != e[0] and a[2] == e[2]
assert set(a[1]['refs']) == {'HEAD', 'refs/heads/main'}
assert set(e[1]['refs']) == {'HEAD', 'refs/heads/main', 'refs/heads/private'}
assert e[1]['refs']['refs/heads/private'] == e[2]['refs/heads/private']
assert all(c[1]['refs']['HEAD'] == c[2]['refs/heads/main'] for c in (b, a, e))
assert [len(c[0]) for c in (b, a, e)] == [348, 348, 412]
commands = load('commands.json')
assert all(c['command'][0] == 'git' and c['exit_code'] == 0 for c in commands)
assert not any(arg.startswith(('https://', 'http://', 'ssh://')) for c in commands for arg in c['command'])
upload_commands = [c for c in commands if 'upload-pack' in c['command']]
assert len(upload_commands) == 3
for c, label in zip(upload_commands, ('hidden-before', 'hidden-after', 'exposed-after')):
    assert bytes.fromhex(c['stdout_hex']) == captured[label][0]
assert all('uploadpack.hideRefs=refs/heads/private' in c['command'] for c in upload_commands[:2])
assert 'uploadpack.hideRefs=refs/heads/private' not in upload_commands[2]['command']

sources = load('sources.json')
for source in sources:
    data = (HERE / source['file']).read_bytes()
    assert source['http_status'] == '200' and source['curl_exit'] == 0
    assert sha(data) == source['sha256'] and len(data) == source['bytes']
extra_sources = {}
for name in ('git-upload-pack', 'transfer-data-leaks'):
    receipt = load(name+'-fetch.json')
    assert receipt['http_code'] == 200 and receipt['exitcode'] == 0
    assert receipt['url_effective'] == 'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/'+name+'.txt'
    extra_sources[name+'.txt'] = sha((HERE / (name+'.txt')).read_bytes())
assert 'https://git-scm.com/docs/git-config' in load('search-links.json')

questions = (ROOT / 'questions.md').read_text().splitlines()
assert len(questions) == len(before['question_lines_sha256'])
changed_questions = [i for i, text in enumerate(questions, 1)
                     if sha(text.encode()) != before['question_lines_sha256'][str(i)]]
assert changed_questions == [740]
assert 'researched 2026-10-17; still open' in questions[739]
open_questions = [i for i, text in enumerate(questions, 1) if text.startswith('- [ ]')]
assert open_questions == before['open_question_lines'] and len(open_questions) == 16
for name in ('courtyard.md', 'quests.md'):
    assert sha((ROOT / name).read_bytes()) == before['tracked_sha256'][name]
assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())

garden = {}
for path in sorted((ROOT / 'garden').rglob('*')):
    if path.is_file() and not path.is_symlink():
        assert path.resolve().is_relative_to(ROOT)
        garden[str(path.relative_to(ROOT))] = sha(path.read_bytes())
assert garden == before['garden_sha256']
rooms = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'rooms').glob('*.md'))
assert rooms == before['room_paths']
gate = (ROOT / 'gate.md').read_text()
map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
entries = re.findall(r'^- \[[^\]]+\]\((rooms/[^)]+\.md)\)', map_text, re.M)
assert Counter(entries) == Counter(rooms) and len(entries) == 697
assert 'checked 2026-10-17' in gate

word = (ROOT / 'words/reference-advertisement.md').read_text()
room = (ROOT / 'rooms/what-the-gaps-can-say.md').read_text()
word_before = load('word-before.json')
assert sha(word_before['content'].encode()) == word_before['sha256']
assert word.startswith(word_before['content'].split('Links:', 1)[0])
assert word.splitlines()[0] == '# reference-advertisement' and word.rstrip().splitlines()[-1].startswith('Links: ')
assert room.splitlines()[0] == '# what-the-gaps-can-say'
assert re.fullmatch(r'\*[^*]+\*', room.splitlines()[2])
assert 'This room gathers' in room.splitlines()[4]
section = room.split('## A still list can hide a moving name — 2026-10-17', 1)[1].split('\n## Sources', 1)[0]
assert 'Question 740 remains open' in section and 'uncertain:' in section
assert '**348-byte**' in section and '**412 bytes**' in section

# Check the actual new prose's local references, not unrelated historical links.
checked_links = 0
for path, text in [(ROOT/'words/reference-advertisement.md', word),
                   (ROOT/'rooms/what-the-gaps-can-say.md', section),
                   (HERE/'README.md', (HERE/'README.md').read_text())]:
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' in target or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        destination = (path.parent / target).resolve()
        assert destination.is_relative_to(ROOT), destination
        if destination == HERE/'verification.json':
            continue  # The final run writes this receipt after checking everything.
        assert destination.is_file(), destination
        checked_links += 1
    for target in re.findall(r'\[\[([^\]]+)\]\]', text):
        name = target.split('|', 1)[0].split('#', 1)[0]
        candidates = [ROOT/(name+'.md'), ROOT/'rooms'/(name+'.md'), ROOT/'words'/(name+'.md')]
        assert any(p.is_file() for p in candidates), name
        checked_links += 1

chronicle = (ROOT / 'chronicle.md').read_bytes()
n = before['chronicle_bytes']
assert sha(chronicle[:n]) == before['tracked_sha256']['chronicle.md']
addition = chronicle[n:].decode()
if PRE:
    assert addition == ''
else:
    assert len(addition.splitlines()) == 1 and addition.endswith('\n')
    assert re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n', addition)

report = {
    'verified_utc': datetime.now(timezone.utc).isoformat(), 'mode': 'pre-close' if PRE else 'final',
    'all_passed': True, 'independent_review': False, 'live_service_requests': 0,
    'real_git_fixture_checks': len(result['checks']), 'separate_decoder_agreed': True,
    'raw_block_sizes': [len(c[0]) for c in (b, a, e)], 'fixture_removed': True,
    'initial_failed_attempt_retained': True, 'changed_question_lines': changed_questions,
    'open_questions': len(open_questions), 'filed': 0, 'researched': 1, 'settled': 0, 'planted': 0,
    'rooms': len(rooms), 'map_entries': len(entries), 'map_duplicates_missing_extra': [],
    'courtyard_quests_garden_unchanged': True, 'checked_local_links': checked_links,
    'chronicle_appended_lines': len(addition.splitlines()), 'supplementary_source_sha256': extra_sources,
    'final_markdown_sha256': {name: sha((ROOT/name).read_bytes()) for name in
                            ('gate.md', 'questions.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md',
                             'words/reference-advertisement.md')},
}
output = HERE / ('pre-close-verification.json' if PRE else 'verification.json')
with output.open('x') as stream:
    json.dump(report, stream, indent=2)
    stream.write('\n')
print(json.dumps(report, indent=2))
