"""Offline verification of this finite visit; never makes a network request."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import ast
import hashlib
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ALLOWED = {'questions.md', 'gate.md', 'chronicle.md', 'words/timeout.md',
           'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'}
ELIGIBLE = {740, 744, 766}


def data(path):
    path = Path(path)
    assert path.resolve().is_relative_to(ROOT), path
    return path.read_bytes()


def sha(value):
    return hashlib.sha256(value).hexdigest()


def load(path):
    return json.loads(data(path))


def verify(final=False):
    before, reuse = load(HERE / 'before.json'), load(HERE / 'reuse.json')
    for file in HERE.glob('*.py'):
        ast.parse(data(file), filename=str(file))
    for label in ('collector', 'parser'):
        assert sha(data(ROOT / reuse[label + '_path'])) == reuse[label + '_sha256']
    readme = data(HERE / 'README.md').decode()
    plan = readme.split('\n## What execution returned', 1)[0]
    assert sha(plan.encode()) == reuse['plan_sha256'], 'pre-collection plan changed'
    manifest = load(HERE / 'manifest.json')
    records = manifest['records']
    ids = ['r1-orgmode', 'r1-emacs', 'r1-guix', 'r2-orgmode']
    assert [r['id'] for r in records] == ids
    assert manifest['stopped_reason'] == 'r2-orgmode: curl=28, HTTP=0, challenge=False'
    assert manifest['retries'] == 0 and manifest['redirects_followed'] is False
    assert not any((HERE / (rid + ext)).exists() for rid in ('r2-emacs', 'r2-guix')
                   for ext in ('.json', '.body', '.headers'))
    parse = runpy.run_path(str(ROOT / reuse['parser_path']))['parse']
    comparison = load(HERE / 'comparison.json')
    inspection = load(HERE / 'inspection.json')
    assert inspection == runpy.run_path(str(HERE / 'inspect.py'))['inspect']()
    assert len(comparison['comparisons']) == len(inspection['body_comparisons']) == len(records)
    previous_finish = None
    for row, comp, optional in zip(records, comparison['comparisons'], inspection['body_comparisons']):
        rid, metrics, cmd = row['id'], row['curl_metrics'], row['command']
        assert row == load(HERE / (rid + '.json'))
        assert row['method'] == 'GET' and cmd[:2] == ['curl', '--disable']
        for key, value in {'--connect-timeout': '10', '--max-time': '45', '--max-filesize': '1048576', '--retry': '0'}.items():
            assert cmd[cmd.index(key) + 1] == value
        assert not any(k in cmd for k in ('--location', '-L', '--insecure', '-k', '--user', '--cookie'))
        assert 'Accept-Encoding: identity' in cmd and 'Git-Protocol: version=0' in cmd
        assert metrics['num_redirects'] == metrics['proxy_used'] == metrics['ssl_verify_result'] == '0'
        assert metrics['url_effective'] == row['url'] == cmd[-1]
        start, finish = (datetime.fromisoformat(row[k]) for k in ('start_utc', 'finish_utc'))
        assert start <= finish and (previous_finish is None or previous_finish <= start)
        previous_finish = finish
        assert abs((finish - start).total_seconds() - row['process_elapsed_monotonic_seconds']) < .01
        old = ROOT / comp['previous_capture']
        old_body = data(old.with_suffix('.body'))
        assert sha(old_body) == load(old)['body_sha256']
        path = HERE / (rid + '.body')
        body = data(path) if path.exists() else None
        assert row['body_present'] == (body is not None)
        assert row['body_sha256'] == (sha(body) if body is not None else None)
        assert row['body_bytes'] == (len(body) if body is not None else None)
        assert rid == comp['id'] == optional['id']
        assert comp['body_equal_to_previous'] == (body == old_body)  # raw collector behavior
        assert optional['body_equal_to_previous'] == (None if body is None else body == old_body)
        headers = data(HERE / (rid + '.headers'))
        assert comp['parse_problem'] is None
        if rid == 'r2-orgmode':
            assert row['curl_exit'] == 28 and 'timed out' in row['stderr']
            assert metrics['http_code'] == '000' and metrics['size_download'] == '0'
            assert metrics['time_starttransfer'] == '0.000000'
            assert body is None and headers == b'' and comp['parsed'] is None
        else:
            assert row['curl_exit'] == 0 and not row['stderr']
            assert body is not None
            assert len(body) == int(metrics['size_download'])
            assert headers.startswith(('HTTP/1.1 ' + metrics['http_code'] + ' ').encode())
            if rid == 'r1-orgmode':
                assert metrics['http_code'] == '200'
                assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
                assert parse(body) == comp['parsed']
            else:
                assert metrics['http_code'] == '500' and body == old_body == b'Internal Server Error'
                assert comp['parsed'] is None
    assert inspection['old_id'] != inspection['new_id']
    assert all(inspection[k] for k in ('same_reference_names', 'same_capabilities', 'id_substitution_explains_all_changed_bytes'))
    assert inspection['collection_span_seconds'] == comparison['window_seconds'] == 129.561243
    assert inspection['same_path_gap_seconds'] == 11509.914646
    assert inspection['timed_out_operation_seconds'] == [45.145394]
    assert all(row in readme for row in inspection['table_rows'])
    assert inspection['new_orgmode_sha256'] in readme
    sources = load(HERE / 'sources.json') + load(HERE / 'followup-sources.json')
    assert len(sources) == 6
    assert previous_finish is not None
    for source in sources:
        body = data(HERE / source['file'])
        expected_status = '429' if source['file'] == 'search-2.html' else '200'
        assert source['http_status'] == expected_status and source['curl_exit'] == 0
        assert sha(body) == source['sha256'] and len(body) == source['bytes']
        assert source['url'] in readme
        assert datetime.fromisoformat(source['start_utc']) >= previous_finish
    assert not (HERE / 'search-2-text.txt').exists(), 'rate-limit page is not search evidence'
    assert 'The total time, in seconds, that the full operation lasted.' in data(HERE / 'write-out-8.7.1.md').decode()
    assert 'no server response code has been received.' in data(HERE / 'response-code-8.7.1.md').decode()
    assert 'Set maximum time in seconds that you allow each transfer to take.' in data(HERE / 'max-time-8.7.1.md').decode()
    assert 'The stream MUST include capability declarations behind a NUL on the' in data(HERE / 'gitprotocol-pack-2.39.5.txt').decode()

    tracked = reuse['tracked_sha256']
    changes = sorted(name for name, digest in tracked.items() if sha(data(ROOT / name)) != digest)
    assert set(changes) <= ALLOWED, changes
    current = {str(p.relative_to(ROOT)) for folder in ('words', 'rooms') for p in (ROOT / folder).glob('*.md')}
    prior = {name for name in tracked if name.startswith(('words/', 'rooms/'))}
    assert current == prior, 'unexpected new or deleted room/word'
    garden = {str(p.relative_to(ROOT)): sha(data(p)) for p in sorted((ROOT / 'garden').rglob('*')) if p.is_file() and not p.is_symlink()}
    assert garden == before['garden_sha256'], 'garden changed'
    questions = data(ROOT / 'questions.md').decode().splitlines()
    assert len(questions) == len(before['question_lines_sha256'])
    changed_lines = {i for i, line in enumerate(questions, 1) if sha(line.encode()) != before['question_lines_sha256'][str(i)]}
    assert changed_lines == ELIGIBLE
    opens = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
    assert opens == before['open_question_lines'] and len(opens) == 16
    assert all('19:10–19:12 UTC; still open' in questions[i - 1] and 'service-check-6/README.md' in questions[i - 1] for i in ELIGIBLE)
    assert not any(line.startswith('- ') for line in data(ROOT / 'courtyard.md').decode().splitlines())
    quests = sum(line.startswith('- [ ]') for line in data(ROOT / 'quests.md').decode().splitlines())
    assert sha(data(ROOT / 'quests.md')) == tracked['quests.md']
    rooms = sorted(p.stem for p in (ROOT / 'rooms').glob('*.md'))
    gate = data(ROOT / 'gate.md').decode()
    section = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
    entries = re.findall(r'^- \[([^\]]+)\]\(rooms/([^\)]+)\.md\) — .+$', section, re.M)
    assert all(a == b for a, b in entries)
    assert Counter(b for _, b in entries) == Counter(rooms), 'Map missing, extra or duplicate room'
    assert 'a changed Git list, slow errors and a timeout' in gate
    for name in ('rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'):
        text = data(ROOT / name).decode()
        lines = [s for s in text.splitlines() if s.strip()]
        assert lines[0] == '# ' + Path(name).stem
        assert lines[1].startswith('*') and lines[1].endswith('*')
        assert lines[2].startswith('This room gathers ')
        assert '129.561243' in text and 'uncertain:' in text
        assert 'service-check-6/README.md' in text and '2026-10-17' in text
    word = data(ROOT / 'words/timeout.md').decode()
    lines = [s for s in word.splitlines() if s.strip()]
    assert lines[0] == '# timeout'
    assert lines[1] == 'A timeout is a time limit that tells a program when to stop waiting or try to stop its work.'
    assert lines[-1].startswith('Links: ') and 'unavailable' in word
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', word):
        assert any((ROOT / f'{folder}/{target}.md').exists() for folder in ('words', 'rooms')), target
    for target in re.findall(r'\]\(([^)]+)\)', readme):
        if target.startswith(('http:', 'https:')):
            continue
        if target == 'verification.json' or (not final and target == 'pre-close-verification.json'):
            continue
        path = (HERE / target).resolve()
        assert path.is_relative_to(ROOT) and path.is_file(), target

    chronicle = data(ROOT / 'chronicle.md')
    n = before['chronicle_bytes']
    assert sha(chronicle[:n]) == tracked['chronicle.md'], 'earlier chronicle changed'
    added = chronicle[n:].decode()
    if final:
        assert len(added.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\.\n', added)
    else:
        assert added == ''
    return {'verified_utc': datetime.now(timezone.utc).isoformat(), 'status': 'pass',
            'mode': 'final' if final else 'pre-close', 'service_requests': len(records),
            'completed_service_replies': sum(r['curl_exit'] == 0 for r in records),
            'timeouts': sum(r['curl_exit'] == 28 for r in records), 'stop_rule_observed': True,
            'missing_body_comparison': inspection['body_comparisons'][-1]['body_equal_to_previous'],
            'web_retrieval_statuses': dict(Counter(s['http_status'] for s in sources)),
            'room_count': len(rooms), 'map_entries': len(entries), 'open_questions': len(opens),
            'researched_question_lines': sorted(changed_lines), 'questions_answered': 0,
            'questions_planted': 0, 'open_quests': quests, 'new_words': 0, 'new_rooms': 0,
            'changed_preexisting_files': changes, 'garden_unchanged': True,
            'chronicle_lines_appended': len(added.splitlines()), 'chronicle_line': added.strip(),
            'independent_review': False}


if __name__ == '__main__':
    final = '--final' in sys.argv[1:]
    name = 'verification.json' if final else 'pre-close-verification.json'
    assert not (HERE / name).exists(), 'refuse overwriting verification'
    result = verify(final)
    with (HERE / name).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))
