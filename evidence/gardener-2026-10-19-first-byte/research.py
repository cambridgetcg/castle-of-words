"""One finite public reading, with all deliberate file access inside the castle."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess

ROOT = Path('/Users/yu/castle').resolve()
OUT = Path(__file__).resolve().parent
assert ROOT in OUT.parents

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.hidden = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'li', 'div', 'h1', 'h2', 'h3', 'br'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)

SOURCES = [
    ('search.html', 'Brave Search: curl time_starttransfer time_pretransfer first byte timing', 'https://search.brave.com/search?q=curl%20time_starttransfer%20time_pretransfer%20first%20byte%20timing'),
    ('write-out.md', 'curl --write-out, curl 8.7.1', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md'),
    ('max-time.md', 'curl --max-time, curl 8.7.1', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md'),
]

def fetch(item):
    name, title, url = item
    dest = OUT/name
    assert not dest.exists()
    cmd = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https', '--connect-timeout', '10', '--max-time', '35', '--max-filesize', '2500000', '--retry', '0', '--user-agent', 'castle-gardener/1.0', '--output', str(dest), '--write-out', '%{http_code}', url]
    start = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=40)
    data = dest.read_bytes() if dest.exists() else b''
    if p.returncode == 0 and p.stdout == '200' and name.endswith('.html'):
        parser = Text(); parser.feed(data.decode('utf-8', errors='replace'))
        lines = [' '.join(s.split()) for s in ''.join(parser.parts).splitlines()]
        (OUT/'search-text.txt').write_text('\n'.join(s for s in lines if s)+'\n')
    return dict(file=name, title=title, url=url, command=cmd, start_utc=start, finish_utc=datetime.now(timezone.utc).isoformat(), curl_exit=p.returncode, http_status=p.stdout, error=p.stderr, bytes=len(data), sha256=sha256(data).hexdigest())

if __name__ == '__main__':
    assert not (OUT/'before.json').exists()
    names = ['courtyard.md', 'questions.md', 'quests.md', 'chronicle.md', 'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/time-to-first-byte.md']
    before: dict = dict(recorded_at=datetime.now(timezone.utc).isoformat(), files={}, garden_sha256={}, rooms=sorted(p.name for p in (ROOT/'rooms').glob('*.md')))
    for name in names:
        p = ROOT/name
        assert ROOT in p.resolve().parents
        before['files'][name] = dict(text=p.read_text(), sha256=sha256(p.read_bytes()).hexdigest()) if p.exists() else None
    for p in sorted((ROOT/'garden').rglob('*')):
        if p.is_file():
            assert ROOT in p.resolve().parents
            before['garden_sha256'][str(p.relative_to(ROOT))] = sha256(p.read_bytes()).hexdigest()
    before['scope'] = 'Research question 740 only, the oldest eligible question. Courtyard empty; sixteen open questions, so plant zero. Use the already fixed fourteen October 17-18 visit directories from the request-order audit. Read the 28 saved orgmode request records and their bodies; rederive each first-view change from its earlier complete advertisement. Separate cumulative timing marks into start-to-pretransfer, pretransfer-to-first-byte, and first-byte-to-finish for completed requests only. Keep the inherited one-second descriptive cutoff; show every completed request at or above it. Keep timeout milestone absence separate. No new service probes, collector imports, changes to old captures, inferred server causes, fitted rates or question closures. Edit one existing room, one new word, one Map line and exactly one appended chronicle line.'
    (OUT/'before.json').write_text(json.dumps(before, indent=2)+'\n')
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, SOURCES))
    (OUT/'sources.json').write_text(json.dumps(results, indent=2)+'\n')
    for r in results: print(r['file'], 'HTTP', r['http_status'], 'curl', r['curl_exit'], 'bytes', r['bytes'])
