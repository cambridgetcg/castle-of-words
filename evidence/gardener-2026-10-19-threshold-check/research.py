"""A bounded public reading for a sensitivity check, not a service probe."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents and 'garden' not in OUT.relative_to(ROOT).parts

# Retain a pre-edit receipt without changing another worker's existing work.
before_path = OUT / 'before.json'
if not before_path.exists():
    paths = [ROOT / x for x in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md')]
    paths += [p for p in (ROOT / 'garden').rglob('*') if p.is_file()]
    before = {'files': {}, 'rooms': sorted(p.name for p in (ROOT / 'rooms').glob('*.md')), 'words': sorted(p.name for p in (ROOT / 'words').glob('*.md'))}
    for path in paths:
        assert ROOT in path.resolve().parents
        data = path.read_bytes()
        before['files'][str(path.relative_to(ROOT))] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data), 'lines': len(data.splitlines())}
    before_path.write_text(json.dumps(before, indent=2) + '\n')

SOURCES = [
    ('search.html', 'Brave Search: Altman Royston cost dichotomising continuous variables cutpoint', 'https://search.brave.com/search?q=Altman%20Royston%20cost%20dichotomising%20continuous%20variables%20cutpoint'),
    ('altman-royston.xml', 'Europe PMC full text: PMC1458573 (title to be checked from returned article)', 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1458573/fullTextXML'),
    ('nist-contingency.html', 'NIST/SEMATECH: 7.4.5. How can we compare the results of classifying according to several categories?', 'https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm'),
    ('altman-royston-pmc.html', 'Altman and Royston: The cost of dichotomising continuous variables (PMC)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1458573/'),
    ('altman-royston-bmj.html', 'Altman and Royston: The cost of dichotomising continuous variables (BMJ)', 'https://www.bmj.com/content/332/7549/1080.1'),
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
    if proc.returncode == 0 and proc.stdout == '200':
        if name.endswith('.html'):
            parser = Text()
            parser.feed(body.decode('utf-8', errors='replace'))
            lines = [' '.join(line.split()) for line in ''.join(parser.parts).splitlines()]
            path.with_name(path.stem + '-text.txt').write_text('\n'.join(line for line in lines if line) + '\n')
        elif name.endswith('.xml'):
            article = ET.fromstring(body)
            title_node = article.find('.//article-title')
            title = ''.join(title_node.itertext()) if title_node is not None else title
            lines = [' '.join(''.join(node.itertext()).split()) for node in article.iter() if node.tag in ('article-title', 'title', 'p')]
            path.with_name(path.stem + '-text.txt').write_text('\n'.join(lines) + '\n')
    return dict(title=title, url=url, file=name, start_utc=start, finish_utc=datetime.now(timezone.utc).isoformat(), command=command, curl_exit=proc.returncode, http_status=proc.stdout, error=proc.stderr, bytes=len(body), sha256=sha256(body).hexdigest())

manifest = OUT / 'sources.json'
results = json.loads(manifest.read_text()) if manifest.exists() else []
already = {item['file'] for item in results}
with ThreadPoolExecutor(max_workers=3) as pool:
    results += list(pool.map(fetch, [source for source in SOURCES if source[0] not in already]))
manifest.write_text(json.dumps(results, indent=2) + '\n')
for item in results:
    print(item['file'], item['http_status'], 'exit', item['curl_exit'], item['title'])
