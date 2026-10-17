"""Offline same-session verification; no network and no changes to the castle text."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREVIOUS = ROOT / 'evidence/gardener-2026-10-17-service-check-2'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    assert path.resolve().is_relative_to(ROOT)
    return json.loads(path.read_text())


def main(final=False):
    assert ROOT == Path('/Users/yu/castle')
    baseline = load(HERE / 'before.json')
    reuse = load(HERE / 'reuse.json')
    for label in ('collector', 'parser'):
        assert sha((ROOT / reuse[label + '_path']).read_bytes()) == reuse[label + '_sha256']
    for file in HERE.glob('*.py'):
        ast.parse(file.read_text(), filename=str(file))
    parse = runpy.run_path(str(ROOT / reuse['parser_path']))['parse']
    manifest = load(HERE / 'manifest.json')
    comparisons = load(HERE / 'comparison.json')
    records = manifest['records']
    assert [r['id'] for r in records] == [f'r{n}-{name}' for n in (1, 2) for name in ('orgmode', 'emacs', 'guix')]
    assert manifest['stopped_reason'] is None
    assert manifest['retries'] == 0 and manifest['redirects_followed'] is False
    assert len(comparisons['comparisons']) == len(records)
    for i, record in enumerate(records):
        assert record == load(HERE / (record['id'] + '.json'))
        name = record['id'].split('-', 1)[1]
        assert record['method'] == 'GET'
        assert record['url'] == f'https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack'
        command = record['command']
        assert command[:2] == ['curl', '--disable']
        for flag, value in {'--proto': '=https', '--connect-timeout': '10', '--max-time': '45',
                            '--max-filesize': '1048576', '--retry': '0',
                            '--user-agent': 'castle-gardener/1.0'}.items():
            assert command[command.index(flag) + 1] == value
        assert 'Accept-Encoding: identity' in command and 'Git-Protocol: version=0' in command
        assert not set(command) & {'--location', '-L', '--insecure', '-k', '--cookie', '--user'}
        metrics = record['curl_metrics']
        assert record['curl_exit'] == 0 and record['stderr'] == ''
        assert metrics['http_code'] == ('200' if name == 'orgmode' else '500')
        assert metrics['num_redirects'] == metrics['proxy_used'] == metrics['ssl_verify_result'] == '0'
        assert Decimal('0') < Decimal(metrics['time_total']) < Decimal('1')
        assert datetime.fromisoformat(record['start_utc']) < datetime.fromisoformat(record['finish_utc'])
        assert record['process_elapsed_monotonic_seconds'] > 0
        if i:
            assert records[i - 1]['finish_utc'] < record['start_utc']
        body = (HERE / (record['id'] + '.body')).read_bytes()
        assert record['body_present'] and sha(body) == record['body_sha256']
        assert len(body) == record['body_bytes'] == int(metrics['size_download'])
        headers = HERE / (record['id'] + '.headers')
        assert headers.read_bytes().startswith(b'HTTP/1.1 ' + metrics['http_code'].encode())
        old_record = load(PREVIOUS / f'r2-{name}.json')
        old_body = (PREVIOUS / f'r2-{name}.body').read_bytes()
        assert sha(old_body) == old_record['body_sha256']
        comparison = comparisons['comparisons'][i]
        assert comparison['id'] == record['id'] and comparison['parse_problem'] is None
        assert comparison['body_equal_to_previous'] == (body == old_body)
        if name == 'orgmode':
            assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
            assert len(body) == 370
            assert comparison['parsed'] == parse(body)
        else:
            assert body == old_body == b'Internal Server Error'
            assert comparison['parsed'] is None
    old_body = (PREVIOUS / 'r2-orgmode.body').read_bytes()
    new_body = (HERE / 'r1-orgmode.body').read_bytes()
    old_view, new_view = parse(old_body), parse(new_body)
    assert new_body == (HERE / 'r2-orgmode.body').read_bytes()
    old_id = 'ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb'
    new_id = '5da905546619ed989e6f95159979c66ead2d4460'
    assert old_view['references'] == {key: old_id for key in ('HEAD', 'refs/heads/master')}
    assert new_view['references'] == {key: new_id for key in ('HEAD', 'refs/heads/master')}
    assert old_view['capabilities'] == new_view['capabilities']
    assert 'symref=HEAD:refs/heads/master' in new_view['capabilities']
    assert old_body.count(old_id.encode()) == 2
    assert old_body.replace(old_id.encode(), new_id.encode()) == new_body
    window = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
    old_record = load(PREVIOUS / 'r2-orgmode.json')
    gap = (datetime.fromisoformat(records[0]['start_utc']) - datetime.fromisoformat(old_record['finish_utc'])).total_seconds()
    assert window == comparisons['window_seconds'] == 2.600268
    assert gap == 11675.464852
    assert min(float(r['curl_metrics']['time_total']) for r in records) == comparisons['total_time_min'] == 0.322015
    assert max(float(r['curl_metrics']['time_total']) for r in records) == comparisons['total_time_max'] == 0.475978
    sources = load(HERE / 'sources.json') + [load(HERE / 'followup-search.json')]
    assert len(sources) == 5
    for source in sources:
        data = (HERE / source['file']).read_bytes()
        assert source['curl_exit'] == 0 and source['http_status'] == '200'
        assert len(data) == source['bytes'] and sha(data) == source['sha256']
        assert source['start_utc'] > records[-1]['finish_utc']
    questions = (ROOT / 'questions.md').read_text().splitlines()
    assert len(questions) == len(baseline['question_lines_sha256'])
    changed_question_lines = [i for i, line in enumerate(questions, 1)
                              if sha(line.encode()) != baseline['question_lines_sha256'][str(i)]]
    assert changed_question_lines == [740, 744, 766]
    open_lines = [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')]
    assert open_lines == baseline['open_question_lines'] and len(open_lines) == 16
    for i in changed_question_lines:
        assert 'observed 2026-10-17 09:24 UTC; still open' in questions[i - 1]
    garden = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sorted((ROOT / 'garden').rglob('*'))
              if p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(ROOT)}
    assert garden == baseline['garden_sha256']
    allowed = {'questions.md', 'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md',
               'rooms/measuring-the-window.md', 'words/reference-advertisement.md'}
    changed_files = []
    for name, digest in reuse['tracked_sha256'].items():
        if sha((ROOT / name).read_bytes()) != digest:
            assert name in allowed, name
            changed_files.append(name)
    assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())
    current_rooms = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'rooms').glob('*.md'))
    assert current_rooms == baseline['room_paths']
    words = {str(p.relative_to(ROOT)) for p in (ROOT / 'words').glob('*.md')}
    assert words == {name for name in reuse['tracked_sha256'] if name.startswith('words/')}
    gate = (ROOT / 'gate.md').read_text().split('## Map\n', 1)[1].split('\n## ', 1)[0]
    mapped = re.findall(r'^- \[[^\]]+\]\((rooms/[^)]+\.md)\)', gate, flags=re.M)
    assert set(mapped) == set(current_rooms) and all(n == 1 for n in Counter(mapped).values())
    for name in ('rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md'):
        lines = [line for line in (ROOT / name).read_text().splitlines() if line.strip()]
        assert lines[0] == '# ' + Path(name).stem
        assert lines[1].startswith('*') and lines[1].endswith('*')
        assert not lines[2].startswith(('#', '*', '-'))
    word = (ROOT / 'words/reference-advertisement.md').read_text().splitlines()
    assert word[0] == '# reference-advertisement' and word[-1].startswith('Links:')
    chronicle = (ROOT / 'chronicle.md').read_bytes()
    prefix = chronicle[:baseline['chronicle_bytes']]
    assert sha(prefix) == baseline['tracked_sha256']['chronicle.md']
    addition = chronicle[baseline['chronicle_bytes']:].decode()
    if final:
        assert len(addition.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', addition)
    else:
        assert addition == ''
    report = {
        'checked_utc': datetime.now(timezone.utc).isoformat(), 'phase': 'final' if final else 'pre-close',
        'result': 'pass', 'scope': 'offline same-session checks, not independent review',
        'service_requests': len(records), 'source_and_search_retrievals': len(sources),
        'old_reference_view': old_view, 'new_reference_view': new_view,
        'capabilities_unchanged': True, 'oid_substitution_explains_entire_body_difference': True,
        'current_orgmode_bodies_equal': True, 'all_error_bodies_match_previous': True,
        'collection_span_seconds': window, 'same_path_unobserved_gap_seconds': gap,
        'changed_question_lines': changed_question_lines, 'answered': 0, 'open_questions': len(open_lines),
        'rooms': len(current_rooms), 'map_entries': len(mapped), 'garden_unchanged': True,
        'unrelated_tracked_files_unchanged': True, 'changed_tracked_files': sorted(changed_files),
        'chronicle_lines_added': len(addition.splitlines()), 'chronicle_line': addition.rstrip('\n'),
    }
    target = HERE / ('verification.json' if final else 'pre-close-verification.json')
    with target.open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--final', action='store_true')
    main(parser.parse_args().final)
