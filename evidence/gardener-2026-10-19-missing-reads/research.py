"""Finite public-document reading; no service measurements or external writes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents and 'garden' not in OUT.relative_to(ROOT).parts

# Capture pre-edit content hashes, never copying private material outside the grounds.
if not (OUT / 'before.json').exists():
    paths = [ROOT / x for x in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md')]
    paths += [p for p in (ROOT / 'garden').rglob('*') if p.is_file()]
    before = {'files': {}, 'rooms': sorted(p.name for p in (ROOT / 'rooms').glob('*.md')), 'words': sorted(p.name for p in (ROOT / 'words').glob('*.md'))}
    for p in paths:
        assert ROOT in p.resolve().parents
        b = p.read_bytes()
        before['files'][str(p.relative_to(ROOT))] = {'bytes': len(b), 'sha256': sha256(b).hexdigest(), 'lines': len(b.splitlines())}
    (OUT / 'before.json').write_text(json.dumps(before, indent=2) + '\n')

SOURCES = [
    ('search.html', 'Brave Search: complete case analysis missing data bias Sterne BMJ b2393', 'https://search.brave.com/search?q=complete%20case%20analysis%20missing%20data%20bias%20Sterne%20BMJ%20b2393'),
    ('nist-censoring.html', 'NIST/SEMATECH: 8.1.3.1. Censoring', 'https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm'),
    ('curl-max-time.md', 'curl 8.7.1: --max-time', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md'),
    ('missing-data-pmc.html', 'Missing data and multiple imputation in clinical epidemiological research', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5358992/'),
    ('git-pack.txt', 'Git v2.39.5: gitprotocol-pack — Pack protocol', 'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt'),
    ('curl-write-out.md', 'curl 8.7.1: --write-out', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md'),
]

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.hidden = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'br'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)

def fetch(item):
    name, title, url = item
    path = OUT / name
    command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https', '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2500000', '--retry', '0', '--user-agent', 'castle-gardener/1.0', '--output', str(path), '--write-out', '%{http_code}', url]
    start = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=45)
    data = path.read_bytes() if path.exists() else b''
    if proc.returncode == 0 and proc.stdout == '200' and name.endswith('.html'):
        parser = Text(); parser.feed(data.decode('utf-8', errors='replace'))
        lines = [' '.join(s.split()) for s in ''.join(parser.parts).splitlines()]
        path.with_name(path.stem + '-text.txt').write_text('\n'.join(s for s in lines if s) + '\n')
    return dict(title=title, url=url, file=name, start_utc=start, finish_utc=datetime.now(timezone.utc).isoformat(), command=command, curl_exit=proc.returncode, http_status=proc.stdout, error=proc.stderr, bytes=len(data), sha256=sha256(data).hexdigest())

if __name__ == '__main__':
    path = OUT / 'sources.json'
    results = json.loads(path.read_text()) if path.exists() else []
    done = {r['file'] for r in results}
    with ThreadPoolExecutor(max_workers=3) as pool:
        results.extend(pool.map(fetch, [x for x in SOURCES if x[0] not in done]))
    path.write_text(json.dumps(results, indent=2) + '\n')
    for r in results: print(r['file'], r['http_status'], 'exit', r['curl_exit'])
