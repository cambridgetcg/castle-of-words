"""Offline focused verification, not an independent review or project test suite."""
import ast
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREVIOUS = HERE.parent / 'gardener-2026-10-17-service-check'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    assert path.resolve().is_relative_to(ROOT)
    return json.loads(path.read_text())


def instant(value):
    return datetime.fromisoformat(value)


def seconds(end, start):
    delta = instant(end) - instant(start)
    return Decimal(delta.days * 86400 + delta.seconds) + Decimal(delta.microseconds) / 1000000


def decode(data):
    packets = []
    pos = 0
    while pos < len(data):
        token = data[pos:pos+4]
        assert re.fullmatch(rb'[0-9a-fA-F]{4}', token)
        size = int(token, 16)
        assert size == 0 or 4 <= size <= 65520
        assert pos + max(size, 4) <= len(data)
        packets.append(data[pos+4:pos+size] if size else None)
        pos += max(size, 4)
    assert packets[:2] == [b'# service=git-upload-pack\n', None]
    assert packets[-1] is None and len(packets) == 5
    first, last = packets[2:4]
    assert first is not None and last is not None
    first_ref, capabilities = first.rstrip(b'\n').split(b'\0')
    refs = {}
    for value in (first_ref, last.rstrip(b'\n')):
        oid, name = value.decode('ascii').split(' ')
        assert re.fullmatch(r'[a-f0-9]{40}', oid) and name not in refs
        refs[name] = oid
    return {'references': refs, 'capabilities': capabilities.decode('ascii').split(), 'packet_count': len(packets)}


def main():
    assert ROOT == Path('/Users/yu/castle')
    before, reuse = load(HERE/'before.json'), load(HERE/'reuse.json')
    for label in ('collector', 'parser'):
        assert sha((ROOT/reuse[label+'_path']).read_bytes()) == reuse[label+'_sha256']
    for path in HERE.glob('*.py'):
        ast.parse(path.read_text(), filename=str(path))
    manifest, comparison = load(HERE/'manifest.json'), load(HERE/'comparison.json')
    rows = manifest['records']
    assert len(rows) == 6 and manifest['stopped_reason'] is None
    assert manifest['retries'] == 0 and manifest['redirects_followed'] is False
    assert 'curl 8.7.1' in manifest['curl_version']
    prior_finish = None
    for i, row in enumerate(rows):
        name = ('orgmode', 'emacs', 'guix')[i % 3]
        assert row['id'] == f'r{1+i//3}-{name}'
        assert row == load(HERE/(row['id']+'.json'))
        assert row['curl_exit'] == 0 and row['method'] == 'GET'
        metrics = row['curl_metrics']
        assert metrics['http_code'] == ('200' if name == 'orgmode' else '500')
        assert all(metrics[k] == '0' for k in ('num_redirects','proxy_used','ssl_verify_result'))
        assert Decimal('0') < Decimal(metrics['time_total']) < 1
        assert instant(row['start_utc']) < instant(row['finish_utc'])
        if prior_finish:
            assert instant(prior_finish) <= instant(row['start_utc'])
        prior_finish = row['finish_utc']
        cmd = row['command']
        assert cmd[:2] == ['curl','--disable']
        for key, val in {'--proto':'=https','--connect-timeout':'10','--max-time':'45',
                         '--max-filesize':'1048576','--retry':'0','--user-agent':'castle-gardener/1.0'}.items():
            assert cmd[cmd.index(key)+1] == val
        assert 'Accept-Encoding: identity' in cmd and 'Git-Protocol: version=0' in cmd
        assert not set(cmd) & {'--insecure','-k','--location','-L','--cookie','--user','--netrc'}
        assert cmd[-1] == row['url'] == f'https://yhetil.org/{name}/0.git/info/refs?service=git-upload-pack'
        body = (HERE/(row['id']+'.body')).read_bytes()
        headers = (HERE/(row['id']+'.headers')).read_bytes()
        assert headers.startswith(('HTTP/1.1 '+metrics['http_code']).encode())
        assert sha(body) == row['body_sha256'] and len(body) == row['body_bytes']
        old = load(PREVIOUS/f'r2-{name}.json')
        oldbody = (PREVIOUS/f'r2-{name}.body').read_bytes()
        assert sha(oldbody) == old['body_sha256'] and body == oldbody
        result = comparison['comparisons'][i]
        assert result['body_equal_to_previous'] and result['parse_problem'] is None
        if name == 'orgmode':
            assert metrics['content_type'] == 'application/x-git-upload-pack-advertisement'
            assert decode(body) == decode(oldbody) == result['parsed']
        else:
            assert body == b'Internal Server Error' and result['parsed'] is None
    previous = load(PREVIOUS/'manifest.json')['records']
    span = seconds(rows[-1]['finish_utc'], rows[0]['start_utc'])
    gap = seconds(rows[0]['start_utc'], previous[-1]['finish_utc'])
    assert span == Decimal(str(comparison['window_seconds'])) == Decimal('2.509528')
    assert gap == Decimal(str(comparison['previous_finish_to_start_seconds'])) == Decimal('11752.725375')
    same_path_gaps = {}
    for name, expected in [('orgmode','11778.734563'),('guix','11753.506345')]:
        new = next(r for r in rows if r['id'] == 'r1-'+name)
        old = next(r for r in previous if r['id'] == 'r2-'+name)
        value = seconds(new['start_utc'],old['finish_utc'])
        assert value == Decimal(expected)
        same_path_gaps[name] = str(value)
    sources = load(HERE/'sources.json') + [load(HERE/'followup-source.json'),load(HERE/'followup-reply-source.json')]
    assert len(sources) == 6
    for source in sources:
        body = (HERE/source['file']).read_bytes()
        assert len(body) == source['bytes'] and sha(body) == source['sha256']
        assert source['http_status'] == '200' and source['curl_exit'] == 0
        assert instant(source['start_utc']) > instant(rows[-1]['finish_utc'])
    questions = (ROOT/'questions.md').read_text().splitlines()
    assert len(questions) == len(before['question_lines_sha256'])
    changed = [i for i,t in enumerate(questions,1) if sha(t.encode()) != before['question_lines_sha256'][str(i)]]
    assert changed == [740,744,766]
    for i in changed:
        text = questions[i-1]
        assert text.startswith('- [ ]') and text.count('(observed 2026-10-17 06:09 UTC;') == 1
        restored = re.sub(r'\(observed 2026-10-17 06:09 UTC;.*?\]\]\) ', '', text, count=1)
        assert sha(restored.encode()) == before['question_lines_sha256'][str(i)]
    opens = [i for i,t in enumerate(questions,1) if t.startswith('- [ ]')]
    assert opens == before['open_question_lines'] and len(opens) == 16
    for path in ('courtyard.md','quests.md','words/reference-advertisement.md'):
        assert sha((ROOT/path).read_bytes()) == before['tracked_sha256'][path]
    assert not any(t.startswith('- ') for t in (ROOT/'courtyard.md').read_text().splitlines())
    garden = {}
    for path in sorted((ROOT/'garden').rglob('*')):
        if path.is_file() and not path.is_symlink():
            assert path.resolve().is_relative_to(ROOT)
            garden[str(path.relative_to(ROOT))] = sha(path.read_bytes())
    assert garden == before['garden_sha256']
    rooms = sorted(str(p.relative_to(ROOT)) for p in (ROOT/'rooms').glob('*.md'))
    assert rooms == before['room_paths']
    assert sorted(str(p.relative_to(ROOT)) for p in (ROOT/'words').glob('*.md')) == reuse['word_paths']
    gate = (ROOT/'gate.md').read_text()
    map_text = gate.split('## Map\n',1)[1].split('\n## ',1)[0]
    links = re.findall(r'^- \[[^\]]+\]\((rooms/[^)]+\.md)\)',map_text,re.M)
    assert sorted(links) == rooms and len(links) == len(set(links))
    added_chunks = []
    for path, start, end in [
        ('rooms/what-the-gaps-can-say.md','## Later quick replies leave the gap dark','## Sources\n'),
        ('rooms/measuring-the-window.md','## The next short wait does not date the ending','Links:\n')]:
        text = (ROOT/path).read_text()
        assert text.startswith('# '+Path(path).stem+'\n\n*')
        assert text.splitlines()[2].endswith('*') and text.splitlines()[4]
        a,b = text.index(start),text.index(end,text.index(start))
        added_chunks.append((ROOT/path,text[a:b]))
        assert sha((text[:a]+text[b:]).encode()) == before['tracked_sha256'][path]
    word = (ROOT/'words/observation-window.md').read_text()
    assert word.startswith('# observation-window\n\nAn observation window is')
    assert word.rstrip().splitlines()[-1].startswith('Links: ')
    a,b = word.index('## A short window does not fill a long gap'),word.index('Links: ')
    restored_word = (word[:a]+word[b:]).replace(' · [[response-time]] · [[http-status]]','')
    assert sha(restored_word.encode()) == reuse['word_before_sha256']
    added_chunks.append((ROOT/'words/observation-window.md',word[a:b]))
    added_chunks.append((HERE/'README.md',(HERE/'README.md').read_text()))
    for path, text in added_chunks:
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
            if re.match(r'https?://',link) or link.startswith('#'):
                continue
            target = (path.parent/link.split('#',1)[0]).resolve()
            assert target.is_relative_to(ROOT)
            if '--pre-close' in sys.argv and target == HERE/'verification.json':
                continue
            assert target.exists(), (path,link)
    chronicle = (ROOT/'chronicle.md').read_bytes()
    assert sha(chronicle[:before['chronicle_bytes']]) == before['tracked_sha256']['chronicle.md']
    suffix = chronicle[before['chronicle_bytes']:].decode()
    if '--pre-close' in sys.argv:
        assert suffix == ''
    else:
        assert len(suffix.splitlines()) == 1
        assert re.fullmatch(r'- 2026-10-17 \d{2}:\d{2} · visit: filed 0, researched 3, planted 0 — [^\n]+\n',suffix)
    print(json.dumps({'status':'PASS','scope':'focused offline same-session verification',
        'checked_utc':datetime.now(timezone.utc).isoformat(),'service_captures':len(rows),
        'source_retrievals':len(sources),'collection_seconds':str(span),
        'previous_collection_gap_seconds':str(gap),'same_path_gaps_seconds':same_path_gaps,
        'changed_question_lines':changed,'open_questions':len(opens),'rooms':len(rooms),
        'map_entries':len(links),'garden_unchanged':True,'reserved_questions_unchanged':True,
        'chronicle_lines_added':len(suffix.splitlines()),'network_requests_during_verification':0},indent=2))


if __name__ == '__main__':
    main()
