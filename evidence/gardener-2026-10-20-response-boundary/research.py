"""Fetch bounded public references; keep all receipts inside the castle."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
from urllib.parse import quote

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents

# Do this before editing the prose. Never replace an existing before-image.
before = OUT / 'before.json'
if not before.exists():
    paths = ['courtyard.md', 'questions.md', 'quests.md', 'chronicle.md',
             'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/time-to-first-byte.md']
    paths += [str(p.relative_to(ROOT)) for p in (ROOT/'garden').rglob('*') if p.is_file()]
    originals = {}
    for relative in paths:
        p = (ROOT/relative).resolve()
        assert ROOT in p.parents
        data = p.read_bytes()
        originals[relative] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    before.write_text(json.dumps({'local_start': datetime.now().astimezone().isoformat(),
        'scope': 'Question 740 only, oldest unreserved; first-response versus first-content boundary. Same 28 saved orgmode attempts, no service probes. No planting while 16 questions remain open.',
        'files': originals}, indent=2) + '\n')

query = 'curl time_starttransfer includes HTTP response headers first byte body'
sources = [
    ('search.html', 'Brave Search: ' + query, 'https://search.brave.com/search?q=' + quote(query)),
    ('starttransfer.md', 'curl 8.7.1: CURLINFO_STARTTRANSFER_TIME', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_STARTTRANSFER_TIME.md'),
    ('transfer.c', 'curl 8.7.1: lib/transfer.c', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/transfer.c'),
    ('progress.c', 'curl 8.7.1: lib/progress.c', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/progress.c'),
    ('rfc9110.txt', 'HTTP Semantics (RFC 9110)', 'https://www.rfc-editor.org/rfc/rfc9110.txt'),
]

def fetch(item):
    name, title, url = item
    command = ['curl', '--disable', '--silent', '--show-error', '--location',
        '--proto', '=https', '--proto-redir', '=https', '--connect-timeout', '10',
        '--max-time', '35', '--max-filesize', '1500000', '--retry', '0',
        '--user-agent', 'castle-gardener/1.0', '--output', str(OUT/name),
        '--write-out', '%{http_code}\n%{url_effective}', url]
    stamp = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(command, capture_output=True, text=True, timeout=40, cwd=ROOT)
    data = (OUT/name).read_bytes() if (OUT/name).exists() else b''
    return dict(title=title, url=url, fetched_utc=stamp, local_read_date=datetime.now().astimezone().date().isoformat(),
        file=name, curl_exit=proc.returncode, status=proc.stdout, stderr=proc.stderr,
        bytes=len(data), sha256=sha256(data).hexdigest(), command=command)

sources.extend([
    ('http.c', 'curl 8.7.1: lib/http.c', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/http.c'),
    ('sendf.c', 'curl 8.7.1: lib/sendf.c', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/sendf.c'),
])
existing = json.loads((OUT/'sources.json').read_text()) if (OUT/'sources.json').exists() else []
by_url = {r['url']: r for r in existing}
pending = [s for s in sources if s[2] not in by_url]
with ThreadPoolExecutor(max_workers=5) as pool:
    by_url.update({r['url']: r for r in pool.map(fetch, pending)})
results = [by_url[s[2]] for s in sources]
(OUT/'sources.json').write_text(json.dumps(results, indent=2)+'\n')

class SearchText(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'): self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('style', 'script'): self.skip = max(0, self.skip-1)
    def handle_data(self, data):
        if not self.skip and data.strip(): self.parts.append(data.strip())
parser = SearchText()
parser.feed((OUT/'search.html').read_text(errors='replace'))
(OUT/'search-text.txt').write_text('\n'.join(parser.parts)+'\n')
print(json.dumps([{k: r[k] for k in ('title', 'curl_exit', 'status', 'bytes')} for r in results], indent=2))
