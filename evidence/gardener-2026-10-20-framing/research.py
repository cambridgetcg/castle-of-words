"""Bounded public-source retrieval for question 740; no mirror probes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
import json
import subprocess

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents

def safe(path):
    resolved = path.resolve()
    assert ROOT in resolved.parents, resolved
    return resolved

before = OUT / 'before.json'
if not before.exists():
    targets = ['courtyard.md', 'questions.md', 'quests.md', 'chronicle.md',
               'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/transfer-coding.md']
    targets += [str(p.relative_to(ROOT)) for p in (ROOT/'garden').rglob('*') if p.is_file()]
    originals = {}
    for relative in targets:
        data = safe(ROOT/relative).read_bytes()
        originals[relative] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    lines = (ROOT/'questions.md').read_text().splitlines()
    opened = [(i, line) for i, line in enumerate(lines, 1) if line.startswith('- [ ]')]
    reserved = ('commission', 'waits for: yu', 'yu decides', 'needs yu', 'being grown by')
    eligible = [i for i, line in opened if not any(s in line.lower() for s in reserved)]
    before.write_text(json.dumps({
        'local_start': datetime.now().astimezone().isoformat(),
        'scope': 'Question 740 only, oldest unreserved; compare message framing and saved content in the existing 28 orgmode attempts. No service probes or planting.',
        'open_questions': len(opened), 'eligible_question_lines': eligible,
        'files': originals,
    }, indent=2)+'\n')
    assert eligible[0] == 740

query = 'RFC 9112 chunked transfer coding connection property intermediaries decode'
sources = [
    ('search.html', 'Brave Search: '+query, 'https://search.brave.com/search?q='+quote(query)),
    ('rfc9112.txt', 'HTTP/1.1 (RFC 9112)', 'https://www.rfc-editor.org/rfc/rfc9112.txt'),
    ('transfer-decoding.md', 'curl 8.7.1: CURLOPT_HTTP_TRANSFER_DECODING', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_HTTP_TRANSFER_DECODING.md'),
]

def fetch(source):
    name, title, url = source
    command = ['curl', '--disable', '--silent', '--show-error', '--location',
        '--proto', '=https', '--proto-redir', '=https', '--connect-timeout', '10',
        '--max-time', '35', '--max-filesize', '1500000', '--retry', '0',
        '--user-agent', 'castle-gardener/1.0', '--output', str(OUT/name),
        '--write-out', '%{http_code}\n%{url_effective}', url]
    started = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=40)
    data = (OUT/name).read_bytes() if (OUT/name).exists() else b''
    return dict(title=title, url=url, file=name, fetched_utc=started,
        read_date=datetime.now().astimezone().date().isoformat(),
        curl_exit=p.returncode, result=p.stdout, stderr=p.stderr,
        bytes=len(data), sha256=sha256(data).hexdigest(), command=command)

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, sources))
(OUT/'sources.json').write_text(json.dumps(results, indent=2)+'\n')

class Plain(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip=0; self.parts=[]
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip = max(0, self.skip-1)
    def handle_data(self, data):
        if not self.skip and data.strip(): self.parts.append(data.strip())

if (OUT/'search.html').exists():
    parser=Plain(); parser.feed((OUT/'search.html').read_text(errors='replace'))
    (OUT/'search-text.txt').write_text('\n'.join(parser.parts)+'\n')
print(json.dumps([{k:r[k] for k in ('title','curl_exit','result','bytes')} for r in results], indent=2))
