"""Offline self-verification of this visit. This script makes no network calls."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
import hashlib
import json
import re
import runpy
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / 'evidence/gardener-2026-10-17-service-check-6'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify(closed):
    assert ROOT == Path('/Users/yu/castle')
    before = json.loads((HERE / 'before.json').read_text())
    manifest = json.loads((HERE / 'manifest.json').read_text())
    records = manifest['records']
    assert len(records) == 6 and manifest['stop_reason'] is None
    assert [r['id'] for r in records] == [f'r{i}-{n}' for i in (1, 2) for n in ('orgmode', 'emacs', 'guix')]
    for i, r in enumerate(records):
        assert json.loads((HERE / (r['id'] + '.json')).read_text()) == r
        body = (HERE / (r['id'] + '.body')).read_bytes()
        assert len(body) == r['body_bytes'] and sha(body) == r['body_sha256']
        m, cmd = r['curl_metrics'], r['command']
        assert r['curl_exit'] == 0 and not r['stderr']
        assert m['http_code'] == ('200' if r['id'].endswith('orgmode') else '500')
        assert m['num_redirects'] == '0' and m['ssl_verify_result'] == '0'
        assert m['url_effective'] == r['url']
        assert cmd[0:2] == ['curl', '--disable']
        assert cmd[cmd.index('--retry') + 1] == '0'
        assert cmd[cmd.index('--max-time') + 1] == '45'
        assert not any(x in cmd for x in ('-k', '--insecure', '-L', '--location', '-X', '--request', '--cookie', '--user'))
        assert Decimal(m['time_total']) >= Decimal(m['time_starttransfer']) >= Decimal(m['time_pretransfer'])
        assert datetime.fromisoformat(r['finish_utc']) > datetime.fromisoformat(r['start_utc'])
        if i:
            assert records[i - 1]['finish_utc'] <= r['start_utc']
    parser = ROOT / before['parser_path']
    assert sha(parser.read_bytes()) == before['parser_sha256']
    parse = runpy.run_path(str(parser))['parse']
    old_body = (OLD / 'r1-orgmode.body').read_bytes()
    new_body = (HERE / 'r1-orgmode.body').read_bytes()
    old_parsed, new_parsed = parse(old_body), parse(new_body)
    old_id, new_id = old_parsed['references']['HEAD'], new_parsed['references']['HEAD']
    assert old_id != new_id
    assert new_body == (HERE / 'r2-orgmode.body').read_bytes()
    assert old_parsed['capabilities'] == new_parsed['capabilities']
    assert old_parsed['references'].keys() == new_parsed['references'].keys()
    assert old_body.replace(old_id.encode(), new_id.encode()) == new_body
    for name in ('emacs', 'guix'):
        assert (OLD / ('r1-' + name + '.body')).read_bytes() == b'Internal Server Error'
        for i in (1, 2):
            assert (HERE / (f'r{i}-' + name + '.body')).read_bytes() == b'Internal Server Error'
    comparison = json.loads((HERE / 'comparison.json').read_text())
    inspection = json.loads((HERE / 'inspection.json').read_text())
    for r, c, timing in zip(records, comparison['comparisons'], inspection['pretransfer_to_first_byte_seconds']):
        prior = ROOT / c['previous_complete_capture']
        assert c['body_equal_to_previous'] == ((HERE / (r['id'] + '.body')).read_bytes() == prior.with_suffix('.body').read_bytes())
        assert c['parsed'] == (new_parsed if r['id'].endswith('orgmode') else None)
        m = r['curl_metrics']
        assert Decimal(timing['seconds']) == Decimal(m['time_starttransfer']) - Decimal(m['time_pretransfer'])
    span = (datetime.fromisoformat(records[-1]['finish_utc']) - datetime.fromisoformat(records[0]['start_utc'])).total_seconds()
    assert span == comparison['observation_window_seconds'] == 87.064224
    assert inspection['new_orgmode_sha256'] == sha(new_body)
    sources = json.loads((HERE / 'sources.json').read_text())
    assert len(sources) == 3
    for s in sources:
        data = (HERE / s['file']).read_bytes()
        assert s['http_status'] == '200' and s['curl_exit'] == 0
        assert len(data) == s['bytes'] and sha(data) == s['sha256']
        assert s['start_utc'] > records[-1]['finish_utc']
    for rel in ('courtyard.md', 'questions.md', 'quests.md'):
        assert sha((ROOT / rel).read_bytes()) == before['content_hashes'][rel]
    questions = (ROOT / 'questions.md').read_text().splitlines()
    assert sum(line.startswith('- [ ]') for line in questions) == 16
    assert not any(line.startswith('- ') for line in (ROOT / 'courtyard.md').read_text().splitlines())
    for i in (740, 744, 766):
        assert questions[i - 1].startswith('- [ ]') and 'commissioned' not in questions[i - 1]
    garden_now = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in (ROOT / 'garden').rglob('*') if p.is_file() and not p.is_symlink()}
    assert garden_now == before['garden_hashes']
    expected = {'gate.md', 'rooms/what-the-gaps-can-say.md', 'rooms/measuring-the-window.md', 'words/response-time.md'}
    changed = {p for p, h in before['content_hashes'].items() if sha((ROOT / p).read_bytes()) != h}
    assert changed == expected | ({'chronicle.md'} if closed else set())
    for rel in sorted(expected - {'gate.md'}):
        lines = (ROOT / rel).read_text().strip().splitlines()
        assert lines[0] == '# ' + Path(rel).stem
        if rel.startswith('rooms/'):
            assert lines[2].startswith('*') and lines[2].endswith('*') and lines[4]
        else:
            assert lines[-1].startswith('Links:') and '[[' in lines[-1]
        assert '2026-10-18' in '\n'.join(lines)
    gate = (ROOT / 'gate.md').read_text()
    map_text = gate.split('## Map\n', 1)[1].split('\n## ', 1)[0]
    map_links = re.findall(r'\]\(rooms/([^/)]+)\.md\)', map_text)
    rooms = {p.stem for p in (ROOT / 'rooms').glob('*.md')}
    assert len(rooms) == len(map_links) == 697
    assert set(map_links) == rooms and all(n == 1 for n in Counter(map_links).values())
    assert all(len(re.findall(r'\]\(rooms/', line)) <= 1 for line in map_text.splitlines())
    chronicle = (ROOT / 'chronicle.md').read_bytes()
    prefix = chronicle[:before['chronicle_bytes']]
    assert sha(prefix) == before['content_hashes']['chronicle.md']
    added = chronicle[before['chronicle_bytes']:].decode()
    if closed:
        assert len(added.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-18 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — .+\n', added)
    else:
        assert not added
    diff_check = subprocess.run(['git', 'diff', '--check'], cwd=ROOT, capture_output=True, text=True)
    assert diff_check.returncode == 0, diff_check.stdout + diff_check.stderr
    report = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'closed': closed,
              'requests': len(records), 'parsed_orgmode_captures': 2, 'matching_error_bodies': 4,
              'sources_fetched': len(sources), 'observation_window_seconds': span,
              'rooms': len(rooms), 'map_entries': len(map_links), 'open_questions': 16,
              'filed': 0, 'researched': 3, 'settled': 0, 'planted': 0,
              'garden_unchanged': True, 'questions_and_courtyard_unchanged': True,
              'changed_content_files': sorted(changed), 'chronicle_lines_added': len(added.splitlines()),
              'verification_kind': 'offline self-check, not independent review'}
    name = 'verification.json' if closed else 'pre-close-verification.json'
    with (HERE / name).open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    verify('--closed' in sys.argv)
