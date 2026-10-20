"""Read saved HTTP dates without making any new service requests.

Run --snapshot once before prose edits, --research to fetch public references,
and --analyse to recompute the local table. All file access stays in the castle.
"""
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from decimal import Decimal
from email.utils import parsedate_to_datetime, format_datetime
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
import json
import os
import re
import subprocess
import sys
from urllib.parse import quote

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
INPUT = 'evidence/gardener-2026-10-20-framing/analysis.json'
ROOM = 'rooms/what-the-gaps-can-say.md'
HEADING = '## The date on the envelope is not the update time — 2026-10-20'


def inside(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    resolved = path.resolve()
    assert ROOT in resolved.parents, path
    return resolved


def read(path):
    return inside(path).read_bytes()


def save(name, obj):
    path = inside(OUT / name)
    assert not path.exists() or name != 'before.json', 'Do not overwrite the baseline'
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')


def snapshot():
    protected = {}
    for directory in ['rooms', 'words', 'garden']:
        for base, dirs, files in os.walk(ROOT / directory, followlinks=False):
            dirs[:] = [d for d in dirs if not (Path(base) / d).is_symlink()]
            for name in files:
                path = Path(base) / name
                if path.is_symlink():
                    continue
                relative = str(path.relative_to(ROOT))
                if directory != 'garden' and path.suffix != '.md':
                    continue
                protected[relative] = sha256(read(path)).hexdigest()
    for relative in ['courtyard.md', 'questions.md', 'quests.md']:
        protected[relative] = sha256(read(relative)).hexdigest()
    gate = read('gate.md').decode()
    glance = next(s for s in gate.splitlines() if s.startswith('> rooms:'))
    map_line = next(s for s in gate.splitlines() if s.startswith('- [what-the-gaps-can-say]'))
    q = read('questions.md').decode().splitlines()
    open_lines = [(i, s) for i, s in enumerate(q, 1) if s.startswith('- [ ]')]
    eligible = [i for i, s in open_lines if not re.search(r'commission|yu decides|waits for: yu|needs yu|another builder', s, re.I)]
    chronicle = read('chronicle.md')
    save('before.json', dict(captured_at=datetime.now().astimezone().isoformat(),
        protected_sha256=protected, chronicle_bytes=len(chronicle),
        chronicle_sha256=sha256(chronicle).hexdigest(), gate_sha256=sha256(gate.encode()).hexdigest(),
        old_glance=glance, old_map_line=map_line,
        open_questions=len(open_lines), eligible_question_lines=eligible,
        researched_question_lines=[eligible[0]], courtyard_entries=sum(s.startswith('- ') for s in read('courtyard.md').decode().splitlines())))
    print('SNAPSHOT', len(protected), 'protected files;', len(open_lines), 'open questions; eligible', eligible)


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


def research():
    query = 'RFC 9110 Date header best available approximation message origination recipient clock'
    requests = [
        ('search', 'Brave Search: ' + query, 'https://search.brave.com/search?q=' + quote(query)),
        ('rfc9110', 'HTTP Semantics — RFC 9110', 'https://www.rfc-editor.org/rfc/rfc9110.txt'),
        ('rfc2330', 'Framework for IP Performance Metrics — RFC 2330', 'https://www.rfc-editor.org/rfc/rfc2330.txt'),
    ]

    def fetch(item):
        key, title, url = item
        command = ['curl', '--disable', '--silent', '--show-error', '--location',
            '--proto', '=https', '--proto-redir', '=https', '--connect-timeout', '10',
            '--max-time', '45', '--max-filesize', '2500000', '--retry', '0',
            '--write-out', '\nCASTLE_HTTP_STATUS=%{http_code}', url]
        started = datetime.now(timezone.utc).isoformat()
        p = subprocess.run(command, capture_output=True, timeout=55)
        body, separator, status = p.stdout.rpartition(b'\nCASTLE_HTTP_STATUS=')
        result = dict(title=title, url=url, read_at_utc=started, curl_exit=p.returncode,
            http_status=status.decode(errors='replace'), stderr=p.stderr.decode(errors='replace'),
            source_sha256=sha256(body).hexdigest(), source_bytes=len(body), command=command)
        assert separator and p.returncode == 0 and status == b'200', result
        text = body.decode('utf-8', errors='replace')
        if key == 'search':
            parser = Text()
            parser.feed(text)
            excerpt = '\n'.join(parser.parts)
        elif key == 'rfc9110':
            # Exact heading matching avoids the indented table of contents.
            sections = [('5.6.7.  Date/Time Formats', '6.  Message Abstraction'),
                        ('6.6.1.  Date', '6.6.2.  Trailer')]
            excerpts = []
            for begin, end in sections:
                a = text.index('\n' + begin + '\n')
                b = text.index('\n' + end + '\n', a)
                excerpts.append(text[a:b].strip())
            excerpt = '\n\n'.join(excerpts)
        else:
            # Keep the clock discussion together with its headings.
            matches = list(re.finditer(r'\n6\.1\.\s+Clock', text))
            if matches:
                a = matches[-1].start()
                b = text.find('\n7.', a)
                excerpt = text[a:b if b > a else a + 18000].strip()
            else:
                # Save full text if the expected headings differ, then inspect it.
                excerpt = text
        name = key + '-excerpts.txt'
        inside(OUT / name).write_text(excerpt + '\n')
        result['retained_excerpt'] = str((OUT / name).relative_to(ROOT))
        result['excerpt_sha256'] = sha256(read(OUT / name)).hexdigest()
        return result

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, requests))
    save('sources.json', results)
    print(json.dumps([{k: r[k] for k in ['title', 'http_status', 'curl_exit', 'retained_excerpt']} for r in results], indent=2))


def difference(a, b):
    delta = a - b
    microseconds = (delta.days * 86400 + delta.seconds) * 1000000 + delta.microseconds
    return format(Decimal(microseconds) / Decimal(1000000), '.6f')


def analyse():
    used = {}

    def kept(path):
        data = read(path)
        used[str(inside(path).relative_to(ROOT))] = sha256(data).hexdigest()
        return data

    prior = json.loads(kept(INPUT))
    for path, digest in prior['input_sha256'].items():
        assert sha256(kept(path)).hexdigest() == digest, path
    rows = []
    for entry in prior['rows']:
        path = Path(entry['capture'])
        record = json.loads(kept(path))
        header = kept(path.with_suffix('.headers'))
        row: dict[str, Any] = dict(capture=str(path), start_utc=record['start_utc'], finish_utc=record['finish_utc'],
            curl_exit=record['curl_exit'], curl_total_seconds=record['curl_metrics']['time_total'])
        if record['curl_exit']:
            assert record['curl_exit'] == 28 and header == b'' and not record['body_present']
            assert not inside(path.with_suffix('.body')).exists()
            row.update(date=None, date_utc=None, age=None,
                date_minus_start_seconds=None, finish_minus_date_seconds=None)
        else:
            assert header.startswith(b'HTTP/1.1 200 OK\r\n') and header.count(b'\r\n\r\n') == 1
            fields = defaultdict(list)
            for line in header.decode('iso-8859-1').split('\r\n')[1:]:
                if line:
                    key, value = line.split(':', 1)
                    fields[key.lower()].append(value.strip())
            assert len(fields['date']) == 1
            date = parsedate_to_datetime(fields['date'][0])
            offset = date.utcoffset()
            assert offset is not None and offset.total_seconds() == 0
            assert format_datetime(date, usegmt=True) == fields['date'][0]
            start = datetime.fromisoformat(record['start_utc'])
            finish = datetime.fromisoformat(record['finish_utc'])
            body = kept(path.with_suffix('.body'))
            assert sha256(body).hexdigest() == record['body_sha256']
            row.update(date=fields['date'][0], date_utc=date.isoformat(), age=fields.get('age'),
                date_minus_start_seconds=difference(date, start),
                finish_minus_date_seconds=difference(finish, date))
        rows.append(row)
    complete = [r for r in rows if r['date'] is not None]
    long_rows = [r for r in complete if Decimal(r['curl_total_seconds']) >= 1]
    summary = dict(attempts=len(rows), completed_with_single_imf_fixdate=len(complete),
        headerless_timeouts=len(rows)-len(complete),
        age_counts=dict(Counter(str(r['age']) for r in complete)),
        date_before_process_start=sum(Decimal(r['date_minus_start_seconds']) < 0 for r in complete),
        date_inside_process_interval=sum(Decimal(r['date_minus_start_seconds']) >= 0 and Decimal(r['finish_minus_date_seconds']) >= 0 for r in complete),
        date_after_process_finish=sum(Decimal(r['finish_minus_date_seconds']) < 0 for r in complete),
        finish_minus_date_min_seconds=min(Decimal(r['finish_minus_date_seconds']) for r in complete),
        finish_minus_date_max_seconds=max(Decimal(r['finish_minus_date_seconds']) for r in complete),
        inherited_hashes_verified=len(prior['input_sha256']))
    summary = {k: str(v) if isinstance(v, Decimal) else v for k, v in summary.items()}
    result = dict(read_date=datetime.now().astimezone().date().isoformat(),
        scope='Question 740 only; the same 28 saved orgmode attempts, with no new service traffic.',
        summary=summary, completed_at_or_above_1s=long_rows, rows=rows, input_sha256=used,
        limits='Differences compare sender-reported whole-second HTTP dates with local process calendar stamps. Clock alignment, the field writer, and the exact event marked are not established. These are not one-way delays, service times, Git selection times, or update timestamps. The local finish stamp is after curl exits, not a per-header arrival timestamp.')
    save('analysis.json', result)
    print(json.dumps(summary, indent=2))
    print('LONG COMPLETED REQUESTS')
    print(json.dumps(long_rows, indent=2))


if __name__ == '__main__':
    if '--snapshot' in sys.argv:
        snapshot()
    if '--research' in sys.argv:
        research()
    if '--analyse' in sys.argv:
        analyse()
