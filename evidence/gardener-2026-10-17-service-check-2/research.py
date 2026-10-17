"""A finite public search after measurement; no service probes here."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'a':
            href = dict(attrs).get('href') or ''
            if href.startswith(('https://', 'http://')):
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def fetch(item):
    name, title, url = item
    dest = HERE / name
    assert not dest.exists()
    command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https',
               '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2097152',
               '--retry', '0', '--user-agent', 'castle-gardener/1.0',
               '--output', str(dest.relative_to(ROOT)), '--write-out', '%{http_code}', url]
    start = datetime.now(timezone.utc).isoformat()
    try:
        proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=50)
        code, status, error = proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        code, status, error = 124, '', str(exc)
    body = dest.read_bytes() if dest.exists() else b''
    row = {'file': name, 'title': title, 'url': url, 'start_utc': start,
           'finish_utc': datetime.now(timezone.utc).isoformat(),
           'curl_exit': code, 'http_status': status, 'stderr': error,
           'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest(), 'command': command}
    if name.endswith('.html') and code == 0 and status == '200':
        parser = Text()
        parser.feed(body.decode('utf-8', errors='replace'))
        with (HERE / name.replace('.html', '-text.txt')).open('x') as f:
            f.write('\n'.join(parser.parts) + '\n')
        row['links'] = sorted(set(parser.links))
    return row


def main():
    assert ROOT == Path('/Users/yu/castle') and (HERE / 'manifest.json').exists()
    with (HERE / 'research-started.txt').open('x') as f:
        f.write(datetime.now(timezone.utc).isoformat() + '\n')
    queries = ['"yhetil.org" "slow"', '"yhetil.org" "maintenance"']
    items = [(f'search-{i}.html', 'Brave Search: ' + q,
              'https://search.brave.com/search?q=' + quote(q)) for i, q in enumerate(queries, 1)]
    base = 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/'
    items += [('write-out-8.7.1.md', 'curl 8.7.1: --write-out', base + 'cmdline-opts/write-out.md'),
              ('total-time-8.7.1.md', 'curl 8.7.1: CURLINFO_TOTAL_TIME_T',
               base + 'libcurl/opts/CURLINFO_TOTAL_TIME_T.md')]
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(fetch, items))
    with (HERE / 'sources.json').open('x') as f:
        json.dump(rows, f, indent=2)
        f.write('\n')
    print(json.dumps([{k: r[k] for k in ('file', 'curl_exit', 'http_status', 'bytes')} for r in rows], indent=2))
    print(json.dumps({r['file']: r.get('links', []) for r in rows[:2]}, indent=2))


if __name__ == '__main__':
    main()
