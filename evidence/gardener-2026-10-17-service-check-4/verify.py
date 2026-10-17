"""Verify this finite visit offline; no requests and no repair of prior evidence."""
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
ALLOWED = {'questions.md', 'gate.md', 'chronicle.md',
           'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'}
NEW_WORD = 'words/via-header.md'
ELIGIBLE = {740, 744, 766}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def data(path):
    path = Path(path)
    assert path.resolve().is_relative_to(ROOT), f'out of grounds: {path}'
    return path.read_bytes()


def load(path):
    return json.loads(data(path))


def verify(final):
    assert ROOT == Path('/Users/yu/castle')
    before, reuse = load(HERE / 'before.json'), load(HERE / 'reuse.json')
    for file in HERE.glob('*.py'):
        ast.parse(data(file), filename=str(file))
    for label in ('collector', 'parser'):
        assert sha(data(ROOT / reuse[label + '_path'])) == reuse[label + '_sha256']
    plan = data(HERE / 'README.md').decode().split('\n## What execution returned', 1)[0]
    assert sha(plan.encode()) == reuse['plan_sha256'], 'original plan changed'

    manifest = load(HERE / 'manifest.json')
    records = manifest['records']
    expected_ids = [f'r{n}-{name}' for n in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
    assert [r['id'] for r in records] == expected_ids
    assert manifest['stopped_reason'] is None and manifest['retries'] == 0
    assert manifest['redirects_followed'] is False
    parse = runpy.run_path(str(ROOT / reuse['parser_path']))['parse']
    comparison = load(HERE / 'comparison.json')
    previous_finish = None
    assert len(records) == len(comparison['comparisons'])
    for row, comp in zip(records, comparison['comparisons']):
        assert row == load(HERE / (row['id'] + '.json'))
        assert row['curl_exit'] == 0 and row['method'] == 'GET'
        metrics, command = row['curl_metrics'], row['command']
        assert command[:2] == ['curl', '--disable']
        for key, value in {'--connect-timeout':'10', '--max-time':'45', '--max-filesize':'1048576', '--retry':'0'}.items():
            assert command[command.index(key) + 1] == value
        assert not any(s in command for s in ('--location', '-L', '--insecure', '-k', '--user', '--cookie'))
        assert 'Accept-Encoding: identity' in command and 'Git-Protocol: version=0' in command
        assert metrics['num_redirects'] == metrics['proxy_used'] == metrics['ssl_verify_result'] == '0'
        assert metrics['url_effective'] == row['url'] == command[-1]
        start, finish = (datetime.fromisoformat(row[k]) for k in ('start_utc', 'finish_utc'))
        assert start <= finish and (previous_finish is None or previous_finish <= start)
        previous_finish = finish
        assert 0 < float(metrics['time_total']) < 1
        body = data(HERE / (row['id'] + '.body'))
        assert len(body) == row['body_bytes'] == int(metrics['size_download'])
        assert sha(body) == row['body_sha256']
        old = ROOT / comp['previous_capture']
        old_record = load(old)
        old_body = data(old.with_suffix('.body'))
        assert sha(old_body) == old_record['body_sha256']
        assert comp['id'] == row['id'] and comp['body_equal_to_previous'] == (body == old_body)
        if row['id'].endswith('-orgmode'):
            assert metrics['http_code'] == '200'
            assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
            assert parse(body) == comp['parsed'] and comp['parse_problem'] is None
        else:
            assert metrics['http_code'] == '500' and body == b'Internal Server Error'
            assert body == old_body and comp['parsed'] is None
    span = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
    assert span == comparison['window_seconds'] == 2.477246
    assert min(float(r['curl_metrics']['time_total']) for r in records) == comparison['total_time_min']
    assert max(float(r['curl_metrics']['time_total']) for r in records) == comparison['total_time_max']
    inspection = load(HERE / 'inspection.json')
    assert runpy.run_path(str(HERE / 'inspect.py'))['inspect']() == inspection
    assert all(inspection[k] for k in ('same_reference_names', 'same_capabilities',
                                      'id_substitution_explains_all_body_changes', 'current_orgmode_bodies_equal'))
    assert inspection['old_id'] != inspection['new_id']
    assert inspection['same_path_gap_seconds'] == 11816.968365
    for row in inspection['header_checks']:
        assert row['client_proxy_used'] == '0'
        assert [part['matches_rfc9110_token'] for part in row['via']] == [False, True]
        assert row['via'][0]['forbidden_characters'] == ['/', '@']
    sources = load(HERE / 'sources.json')
    followup = load(HERE / 'followup-search.json')
    assert len(sources) == 4 and all(s['http_status'] == '200' for s in sources)
    assert followup['http_status'] == '429' and 'links' not in followup
    assert previous_finish is not None
    for row in sources + [followup]:
        body = data(HERE / row['file'])
        assert sha(body) == row['sha256'] and len(body) == row['bytes']
        assert row['curl_exit'] == 0
        assert datetime.fromisoformat(row['start_utc']) >= previous_finish

    tracked = reuse['tracked_sha256']
    changes = []
    for name, digest in tracked.items():
        if sha(data(ROOT / name)) != digest:
            changes.append(name)
            assert name in ALLOWED, f'unexpected edit: {name}'
    current = {str(p.relative_to(ROOT)) for folder in ('words', 'rooms') for p in (ROOT / folder).glob('*.md')}
    previous = {name for name in tracked if name.startswith(('words/', 'rooms/'))}
    assert current - previous == {NEW_WORD} and not previous - current
    garden = {str(p.relative_to(ROOT)): sha(data(p)) for p in sorted((ROOT / 'garden').rglob('*'))
              if p.is_file() and not p.is_symlink()}
    assert garden == before['garden_sha256'], 'garden changed'
    questions = data(ROOT / 'questions.md').decode().splitlines()
    assert len(questions) == len(before['question_lines_sha256'])
    changed_question_lines = {i for i, line in enumerate(questions, 1)
                             if sha(line.encode()) != before['question_lines_sha256'][str(i)]}
    assert changed_question_lines == ELIGIBLE
    opens = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
    assert opens == before['open_question_lines'] and len(opens) == 16
    assert all('still open' in questions[i-1] and 'service-check-4/README.md' in questions[i-1] for i in ELIGIBLE)
    assert not any(line.startswith('- ') for line in data(ROOT / 'courtyard.md').decode().splitlines())

    rooms = sorted(p.stem for p in (ROOT / 'rooms').glob('*.md'))
    gate = data(ROOT / 'gate.md').decode()
    section = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
    map_entries = re.findall(r'^- \[([^\]]+)\]\(rooms/([^\)]+)\.md\) — .+$', section, re.M)
    assert all(a == b for a, b in map_entries)
    mapped = [b for _, b in map_entries]
    assert Counter(mapped) == Counter(rooms), 'Map missing, extra or duplicate room'
    assert len(mapped) == len(rooms) == 697
    assert 'no extra round or new watch' in gate
    assert 'names along a reply\'s path supply neither per-helper times' in gate
    assert 'a malformed path note is not a diagnosis' in gate
    for name in ('rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'):
        lines = [s for s in data(ROOT / name).decode().splitlines() if s.strip()]
        assert lines[0] == '# ' + Path(name).stem
        assert lines[1].startswith('*') and lines[1].endswith('*')
        assert lines[2].startswith('This room gathers ')
    word = data(ROOT / NEW_WORD).decode()
    lines = [s for s in word.splitlines() if s.strip()]
    assert lines[0] == '# via-header' and lines[1].startswith('A Via header is ')
    assert lines[-1].startswith('Links: ') and 'uncertain:' in word
    for target in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', word):
        assert any((ROOT / f'{folder}/{target}.md').exists() for folder in ('words', 'rooms')), target

    chronicle = data(ROOT / 'chronicle.md')
    n = before['chronicle_bytes']
    assert sha(chronicle[:n]) == tracked['chronicle.md'], 'historical chronicle changed'
    added = chronicle[n:].decode()
    if final:
        assert len(added.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\.\n', added)
    else:
        assert added == ''
    return {'verified_utc': datetime.now(timezone.utc).isoformat(), 'mode': 'final' if final else 'pre-close',
            'status': 'pass', 'service_captures_verified': len(records), 'retrieval_receipts_verified': len(sources) + 1,
            'synthetic_token_cases_passed': inspection['synthetic_token_cases_passed'],
            'room_count': len(rooms), 'map_entries': len(mapped), 'open_questions': len(opens),
            'researched_question_lines': sorted(changed_question_lines), 'questions_answered': 0,
            'new_word_files': [NEW_WORD], 'changed_preexisting_files': sorted(changes),
            'garden_unchanged': True, 'chronicle_lines_appended': len(added.splitlines()),
            'chronicle_line': added.strip(), 'independent_review': False}


if __name__ == '__main__':
    final = '--final' in sys.argv[1:]
    name = 'verification.json' if final else 'pre-close-verification.json'
    assert not (HERE / name).exists(), 'refuse overwriting a verification result'
    result = verify(final)
    with (HERE / name).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))
