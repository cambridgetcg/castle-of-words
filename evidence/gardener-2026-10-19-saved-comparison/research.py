"""Fetch four public references; never contact the observed mirror."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents and 'garden' not in OUT.relative_to(ROOT).parts
SOURCES = [
    ('search.html', 'Brave Search: NIST contingency table small expected frequencies independent observations', 'https://search.brave.com/search?q=NIST%20contingency%20table%20small%20expected%20frequencies%20independent%20observations'),
    ('nist-contingency.html', 'NIST/SEMATECH: 7.4.5. How can we compare the results of classifying according to several categories?', 'https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm'),
    ('gitprotocol-pack-2.39.5.txt', 'Git project: gitprotocol-pack — Pack protocol, v2.39.5', 'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt'),
    ('write-out-8.7.1.md', 'curl project: --write-out, 8.7.1', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md'),
]

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'br'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

def fetch(source):
    name, title, url = source
    path = OUT / name
    command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https', '--connect-timeout', '10', '--max-time', '45', '--max-filesize', '2000000', '--retry', '0', '--user-agent', 'castle-gardener/1.0', '--output', str(path), '--write-out', '%{http_code}', url]
    start = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(command, capture_output=True, text=True, timeout=50, cwd=ROOT)
    body = path.read_bytes() if path.exists() else b''
    if name.endswith('.html') and proc.returncode == 0 and proc.stdout == '200':
        parser = Text()
        parser.feed(body.decode('utf-8', errors='replace'))
        lines = [' '.join(line.split()) for line in ''.join(parser.parts).splitlines()]
        (OUT / name.replace('.html', '-text.txt')).write_text('\n'.join(line for line in lines if line) + '\n')
    return dict(title=title, url=url, file=name, start_utc=start, finish_utc=datetime.now(timezone.utc).isoformat(), command=command, curl_exit=proc.returncode, http_status=proc.stdout, error=proc.stderr, bytes=len(body), sha256=sha256(body).hexdigest())

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, SOURCES))
(OUT / 'sources.json').write_text(json.dumps(results, indent=2) + '\n')
for item in results:
    print(item['file'], item['http_status'], 'exit', item['curl_exit'], 'bytes', item['bytes'])
