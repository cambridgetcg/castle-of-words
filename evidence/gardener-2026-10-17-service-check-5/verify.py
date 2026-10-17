"""Offline checks for this visit; no fetches, repairs or monitoring."""
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
ELIGIBLE = {740, 744, 766}
ALLOWED = {'questions.md', 'gate.md', 'chronicle.md', 'words/observation-gap.md',
           'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'}


def data(path):
    path = Path(path)
    assert path.resolve().is_relative_to(ROOT), f'out of grounds: {path}'
    return path.read_bytes()


def sha(value):
    return hashlib.sha256(value).hexdigest()


def load(path):
    return json.loads(data(path))


def verify(final=False):
    assert ROOT == Path('/Users/yu/castle')
    before, reuse = load(HERE / 'before.json'), load(HERE / 'reuse.json')
    for file in HERE.glob('*.py'):
        ast.parse(data(file), filename=str(file))
    for label in ('collector', 'parser'):
        assert sha(data(ROOT / reuse[label + '_path'])) == reuse[label + '_sha256']
    readme = data(HERE / 'README.md').decode()
    plan = readme.split('\n## What execution returned', 1)[0]
    assert sha(plan.encode()) == reuse['plan_sha256'], 'plan changed after collection'
    manifest = load(HERE / 'manifest.json')
    records = manifest['records']
    expected_ids = [f'r{n}-{name}' for n in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
    assert [r['id'] for r in records] == expected_ids
    assert manifest['stopped_reason'] is None and manifest['retries'] == 0
    assert manifest['redirects_followed'] is False
    parse = runpy.run_path(str(ROOT / reuse['parser_path']))['parse']
    comparison = load(HERE / 'comparison.json')
    assert len(records) == len(comparison['comparisons'])
    previous_finish = None
    for row, comp in zip(records, comparison['comparisons']):
        assert row == load(HERE / (row['id'] + '.json'))
        assert row['curl_exit'] == 0 and row['method'] == 'GET' and not row['stderr']
        metrics, cmd = row['curl_metrics'], row['command']
        assert cmd[:2] == ['curl', '--disable']
        for key, value in {'--connect-timeout': '10', '--max-time': '45', '--max-filesize': '1048576', '--retry': '0'}.items():
            assert cmd[cmd.index(key) + 1] == value
        assert not any(k in cmd for k in ('--location', '-L', '--insecure', '-k', '--user', '--cookie'))
        assert 'Accept-Encoding: identity' in cmd and 'Git-Protocol: version=0' in cmd
        assert metrics['num_redirects'] == metrics['proxy_used'] == metrics['ssl_verify_result'] == '0'
        assert metrics['url_effective'] == row['url'] == cmd[-1]
        start, finish = (datetime.fromisoformat(row[k]) for k in ('start_utc', 'finish_utc'))
        assert start <= finish and (previous_finish is None or previous_finish <= start)
        previous_finish = finish
        assert 0 < float(metrics['time_total']) < 1
        assert abs((finish - start).total_seconds() - row['process_elapsed_monotonic_seconds']) < .01
        body = data(HERE / (row['id'] + '.body'))
        assert sha(body) == row['body_sha256']
        assert len(body) == row['body_bytes'] == int(metrics['size_download'])
        headers = data(HERE / (row['id'] + '.headers')).decode()
        assert headers.startswith('HTTP/1.1 ' + metrics['http_code'] + ' ')
        old = ROOT / comp['previous_capture']
        old_body = data(old.with_suffix('.body'))
        assert sha(old_body) == load(old)['body_sha256']
        assert comp['id'] == row['id']
        assert comp['body_equal_to_previous'] == (body == old_body)
        assert comp['parse_problem'] is None
        if row['id'].endswith('-orgmode'):
            assert metrics['http_code'] == '200'
            assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
            assert parse(body) == comp['parsed']
        else:
            assert metrics['http_code'] == '500'
            assert body == old_body == b'Internal Server Error' and comp['parsed'] is None
    span = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
    assert span == comparison['window_seconds'] == 3.322628
    assert min(float(r['curl_metrics']['time_total']) for r in records) == comparison['total_time_min'] == .351625
    assert max(float(r['curl_metrics']['time_total']) for r in records) == comparison['total_time_max'] == .851251
    inspection = load(HERE / 'inspection.json')
    assert inspection == runpy.run_path(str(HERE / 'inspect.py'))['inspect']()
    for key in ('same_reference_names', 'same_capabilities', 'id_substitution_explains_all_changed_bytes', 'current_orgmode_bodies_equal'):
        assert inspection[key]
    assert inspection['old_id'] != inspection['new_id']
    assert inspection['same_path_gap_seconds'] == 11838.569939
    assert all(row in readme for row in inspection['table_rows'])
    assert inspection['new_orgmode_sha256'] in readme
    sources = load(HERE / 'sources.json')
    assert len(sources) == 3
    assert previous_finish is not None
    for source in sources:
        body = data(HERE / source['file'])
        assert source['http_status'] == '200' and source['curl_exit'] == 0
        assert sha(body) == source['sha256'] and len(body) == source['bytes']
        assert source['url'] in readme
        assert datetime.fromisoformat(source['start_utc']) >= previous_finish
    assert 'The total time, in seconds, that the full operation lasted.' in data(HERE / 'write-out-8.7.1.md').decode()
    assert 'The stream MUST include capability declarations behind a NUL on the' in data(HERE / 'gitprotocol-pack-2.39.5.txt').decode()

    tracked = reuse['tracked_sha256']
    changes = sorted(name for name, digest in tracked.items() if sha(data(ROOT / name)) != digest)
    assert set(changes) <= ALLOWED, changes
    current = {str(p.relative_to(ROOT)) for folder in ('words', 'rooms') for p in (ROOT / folder).glob('*.md')}
    prior = {name for name in tracked if name.startswith(('words/', 'rooms/'))}
    assert current == prior, 'no new or deleted rooms/words expected'
    garden = {str(p.relative_to(ROOT)): sha(data(p)) for p in sorted((ROOT / 'garden').rglob('*')) if p.is_file() and not p.is_symlink()}
    assert garden == before['garden_sha256'], 'garden changed'
    questions = data(ROOT / 'questions.md').decode().splitlines()
    assert len(questions) == len(before['question_lines_sha256'])
    changed_lines = {i for i, line in enumerate(questions, 1) if sha(line.encode()) != before['question_lines_sha256'][str(i)]}
    assert changed_lines == ELIGIBLE
    opens = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
    assert opens == before['open_question_lines'] and len(opens) == 16
    assert all('15:58 UTC; still open' in questions[i - 1] and 'service-check-5/README.md' in questions[i - 1] for i in ELIGIBLE)
    assert not any(line.startswith('- ') for line in data(ROOT / 'courtyard.md').decode().splitlines())
    assert sum(line.startswith('- [ ]') for line in data(ROOT / 'quests.md').decode().splitlines()) == 8

    rooms = sorted(p.stem for p in (ROOT / 'rooms').glob('*.md'))
    gate = data(ROOT / 'gate.md').decode()
    section = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
    entries = re.findall(r'^- \[([^\]]+)\]\(rooms/([^\)]+)\.md\) — .+$', section, re.M)
    assert all(a == b for a, b in entries)
    mapped = [b for _, b in entries]
    assert Counter(mapped) == Counter(rooms), 'Map missing, extra or duplicate room'
    assert len(rooms) == 697
    assert 'do not reveal an update schedule' in gate
    assert 'request times, spans of checks and gaps between them measure different things' in gate
    for name in ('rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'):
        lines = [s for s in data(ROOT / name).decode().splitlines() if s.strip()]
        assert lines[0] == '# ' + Path(name).stem
        assert lines[1].startswith('*') and lines[1].endswith('*')
        assert lines[2].startswith('This room gathers ')
        assert '3.322628' in '\n'.join(lines)
    word = data(ROOT / 'words/observation-gap.md').decode()
    lines = [s for s in word.splitlines() if s.strip()]
    assert lines[0] == '# observation-gap'
    assert lines[1] == 'An observation gap is time between two checks when we did not record what happened.'
    assert lines[-1].startswith('Links: ') and 'uncertain:' in word
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', word):
        assert any((ROOT / f'{folder}/{target}.md').exists() for folder in ('words', 'rooms')), target
    for target in re.findall(r'\]\(([^)]+)\)', readme):
        if not target.startswith(('http:', 'https:')):
            if not final and target in ('pre-close-verification.json', 'verification.json'):
                continue
            if final and target == 'verification.json':
                continue
            assert (HERE / target).is_file(), target

    chronicle = data(ROOT / 'chronicle.md')
    n = before['chronicle_bytes']
    assert sha(chronicle[:n]) == tracked['chronicle.md'], 'old chronicle changed'
    added = chronicle[n:].decode()
    if final:
        assert len(added.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\.\n', added)
    else:
        assert added == ''
    return {'verified_utc': datetime.now(timezone.utc).isoformat(), 'status': 'pass',
            'mode': 'final' if final else 'pre-close', 'captures_verified': len(records),
            'web_retrievals_verified': len(sources), 'same_path_gap_seconds': inspection['same_path_gap_seconds'],
            'collection_span_seconds': span, 'room_count': len(rooms), 'map_entries': len(mapped),
            'open_questions': len(opens), 'researched_question_lines': sorted(changed_lines),
            'questions_answered': 0, 'questions_planted': 0, 'open_quests': 8,
            'new_words': 0, 'new_rooms': 0, 'changed_preexisting_files': changes,
            'garden_unchanged': True, 'chronicle_lines_appended': len(added.splitlines()),
            'chronicle_line': added.strip(), 'independent_review': False}


if __name__ == '__main__':
    final = '--final' in sys.argv[1:]
    name = 'verification.json' if final else 'pre-close-verification.json'
    assert not (HERE / name).exists(), 'refuse overwriting verification'
    result = verify(final)
    with (HERE / name).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))
