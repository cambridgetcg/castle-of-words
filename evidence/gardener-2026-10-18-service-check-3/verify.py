"""Offline verification of this visit. No network calls or source-file edits."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
import hashlib
import json
import re
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRE_CLOSE = '--pre-close' in sys.argv


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    assert path.resolve().is_relative_to(ROOT), path
    return path.read_bytes()


def load(path):
    return json.loads(read(path))


def main():
    assert ROOT == Path('/Users/yu/castle')
    before = load(HERE / 'before.json')
    expected = {'gate.md', 'rooms/what-the-gaps-can-say.md',
                'rooms/measuring-the-window.md', 'words/response-time.md'}
    if not PRE_CLOSE:
        expected.add('chronicle.md')
    changed = {p for p, h in before['content_hashes'].items() if sha(read(ROOT / p)) != h}
    assert changed == expected, (changed, expected)
    now_words_rooms = {str(p.relative_to(ROOT)) for d in ('words', 'rooms')
                       for p in (ROOT / d).glob('*.md')}
    new = now_words_rooms - set(before['content_hashes'])
    assert new == {'words/server-timing.md'}, new
    garden = {str(p.relative_to(ROOT)): sha(read(p))
              for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()}
    assert garden == before['garden_hashes'], 'garden changed'
    for p in ('courtyard.md', 'questions.md', 'quests.md'):
        assert sha(read(ROOT / p)) == before['content_hashes'][p]
    questions = (ROOT / 'questions.md').read_text().splitlines()
    opened = [(i, s) for i, s in enumerate(questions, 1) if s.startswith('- [ ]')]
    eligible = [i for i, s in opened if not re.search(
        r'commissioned|waits for: (?:yu|commission)|yu decides|being grown', s)]
    assert len(opened) == 16 and eligible == [740, 744, 766]
    assert not any(s.startswith('- ') for s in (ROOT / 'courtyard.md').read_text().splitlines())
    assert sum(s.startswith('- [ ]') for s in (ROOT / 'quests.md').read_text().splitlines()) == 8

    gate = (ROOT / 'gate.md').read_text()
    section = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
    entries = re.findall(r'\]\(rooms/([^()]+\.md)\)', section)
    rooms = {p.name for p in (ROOT / 'rooms').glob('*.md')}
    assert set(entries) == rooms and all(n == 1 for n in Counter(entries).values())
    assert all(len(re.findall(r'\]\(rooms/[^()]+\.md\)', line)) <= 1
               for line in section.splitlines())

    manifest = load(HERE / 'manifest.json')
    rows = manifest['records']
    assert len(rows) == manifest['planned_maximum_requests'] == 6
    assert manifest['stop_reason'] is None
    assert [r['id'] for r in rows] == [f'r{i}-{p}' for i in (1, 2)
                                      for p in ('orgmode', 'emacs', 'guix')]
    comparison = load(HERE / 'comparison.json')
    parse = runpy.run_path(str(ROOT / before['parser_path']))['parse']
    assert sha(read(ROOT / before['parser_path'])) == before['parser_sha256']
    collector = load(HERE / 'collector-source.json')
    assert sha(read(ROOT / collector['path'])) == collector['sha256']
    totals = []
    for r, c in zip(rows, comparison['comparisons']):
        assert r['id'] == c['id']
        assert r == load(HERE / (r['id'] + '.json'))
        body = read(HERE / (r['id'] + '.body'))
        assert r['curl_exit'] == 0 and r['body_present']
        assert len(body) == r['body_bytes'] and sha(body) == r['body_sha256']
        m, cmd = r['curl_metrics'], r['command']
        assert m['url_effective'] == r['url']
        assert m['num_redirects'] == m['ssl_verify_result'] == '0'
        assert Decimal(m['size_download']) == len(body)
        assert cmd[cmd.index('--retry') + 1] == '0'
        assert cmd[cmd.index('--max-time') + 1] == '45'
        assert '--location' not in cmd and '--insecure' not in cmd and '-k' not in cmd
        assert '--disable' in cmd and 'Git-Protocol: version=0' in cmd
        headers = read(HERE / (r['id'] + '.headers')).decode()
        assert not re.search(r'^server-timing\s*:', headers, re.I | re.M)
        assert re.search(r'^HTTP/\S+ ' + m['http_code'] + r'\b', headers, re.M)
        old_meta = ROOT / c['previous_complete_capture']
        old = load(old_meta)
        old_body = read(old_meta.with_suffix('.body'))
        assert sha(old_body) == old['body_sha256']
        assert body == old_body and c['body_equal_to_previous'] is True
        if r['id'].endswith('-orgmode'):
            assert m['http_code'] == '200' and len(body) == 370
            assert parse(body) == c['parsed'] == parse(old_body)
            assert c['parsed']['references'] == {
                'HEAD': 'fffa58637c7f24f10d33437a6ef7acd1dd2498df',
                'refs/heads/master': 'fffa58637c7f24f10d33437a6ef7acd1dd2498df'}
        else:
            assert m['http_code'] == '500' and body == b'Internal Server Error'
        assert c['parse_problem'] is None
        total = Decimal(m['time_total'])
        assert 0 < total < 1
        assert Decimal(m['time_pretransfer']) <= Decimal(m['time_starttransfer']) <= total
        assert datetime.fromisoformat(r['start_utc']) < datetime.fromisoformat(r['finish_utc'])
        totals.append(total)
    for left, right in zip(rows, rows[1:]):
        assert left['finish_utc'] < right['start_utc'], 'requests overlapped'
    start = datetime.fromisoformat(rows[0]['start_utc'])
    span = (datetime.fromisoformat(rows[-1]['finish_utc']) - start).total_seconds()
    old_rows = load(ROOT / collector['baseline'] / 'manifest.json')['records']
    old_org = next(r for r in reversed(old_rows) if r['id'].endswith('-orgmode') and r['curl_exit'] == 0)
    gap = (start - datetime.fromisoformat(old_org['finish_utc'])).total_seconds()
    last_gap = (start - datetime.fromisoformat(old_rows[-1]['finish_utc'])).total_seconds()
    assert span == comparison['observation_window_seconds'] == 2.535096
    assert gap == comparison['previous_complete_orgmode_finish_to_start_seconds'] == 11460.371633
    assert last_gap == comparison['previous_attempt_finish_to_start_seconds'] == 11443.827347

    sources = load(HERE / 'sources.json')
    assert sha(read(ROOT / sources['helper_path'])) == sources['helper_sha256']
    for s in sources['sources'] + [load(HERE / 'pinned-source.json')]:
        data = read(HERE / s['file'])
        assert s['curl_exit'] == 0 and s['http_status'] == '200'
        assert sha(data) == s['sha256'] and len(data) == s['bytes']
    assert read(HERE / 'server-timing-text.txt') == read(HERE / 'server-timing-20260407-text.txt')
    receipt = (HERE / 'README.md').read_text()
    initial_plan = receipt.split('\n## What arrived\n', 1)[0]
    assert sha(initial_plan.encode()) == before['plan_sha256'], 'plan altered'
    for r in rows:
        assert r['curl_metrics']['time_total'] in receipt
    assert str(span) in receipt and f'{gap:,.6f}' in receipt

    for name in ('server-timing', 'response-time'):
        text = (ROOT / 'words' / (name + '.md')).read_text()
        assert text.startswith('# ' + name + '\n\n')
        assert text.rstrip().splitlines()[-1].startswith('Links: ')
    sections = [(ROOT / 'words/server-timing.md', (ROOT / 'words/server-timing.md').read_text()),
                (HERE / 'README.md', receipt)]
    for name, marker in [('what-the-gaps-can-say', '## A report from inside is not an explanation'),
                         ('measuring-the-window', '## A reported duration still needs its boundaries')]:
        path = ROOT / 'rooms' / (name + '.md')
        text = path.read_text()
        lines = text.splitlines()
        assert lines[0] == '# ' + name and lines[2].startswith('*') and lines[2].endswith('*')
        assert lines[4] and not lines[4].startswith(('#', '*'))
        sections.append((path, text.split(marker, 1)[1].split('\n## ', 1)[0].split('\nLinks:', 1)[0]))
    for path, text in sections:
        for name in re.findall(r'\[\[([^\]|#]+)', text):
            assert any((ROOT / p).exists() for p in (name + '.md', 'words/' + name + '.md',
                                                   'rooms/' + name + '.md')), (path, name)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', '#')):
                continue
            if target == 'verification.json' and path == HERE / 'README.md':
                continue  # This run creates the report only after every check passes.
            assert (path.parent / target.split('#')[0]).exists(), (path, target)

    chronicle = read(ROOT / 'chronicle.md')
    prefix = chronicle[:before['chronicle_bytes']]
    assert sha(prefix) == before['content_hashes']['chronicle.md']
    added = chronicle[before['chronicle_bytes']:].decode()
    if PRE_CLOSE:
        assert added == ''
    else:
        assert re.fullmatch(r'- 2026-10-18 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n', added)
    result = {'verified_utc': datetime.now(timezone.utc).isoformat(),
              'stage': 'before chronicle' if PRE_CLOSE else 'final', 'passed': True,
              'requests': len(rows), 'http_status_counts': dict(Counter(r['curl_metrics']['http_code'] for r in rows)),
              'min_seconds': str(min(totals)), 'max_seconds': str(max(totals)),
              'server_timing_fields_in_saved_headers': 0, 'all_bodies_match_previous': True,
              'window_seconds': span, 'same_path_gap_seconds': gap,
              'rooms': len(rooms), 'map_entries': len(entries), 'open_questions': len(opened),
              'researched_question_lines': eligible, 'new_word_files': sorted(new),
              'changed_existing_prose': sorted(changed), 'garden_unchanged': True,
              'chronicle_lines_added': len(added.splitlines()), 'chronicle_line': added.rstrip(),
              'review_kind': 'local self-check, not independent review'}
    output = HERE / ('pre-close-verification.json' if PRE_CLOSE else 'verification.json')
    with output.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
