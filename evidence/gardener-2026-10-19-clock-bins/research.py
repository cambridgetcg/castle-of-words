"""Finite public reading and in-castle before-image; never runs a collector."""
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
        if tag in ('p', 'li', 'div', 'h1', 'h2', 'h3', 'br', 'tr'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)

SOURCES = [
    ('search.html', 'Brave Search: NIST contingency table counts categories sampling', 'https://search.brave.com/search?q=NIST%20contingency%20table%20counts%20categories%20sampling'),
    ('rfc3339.txt', 'Date and Time on the Internet: Timestamps — RFC 3339', 'https://www.rfc-editor.org/rfc/rfc3339.txt'),
    ('nist-contingency.html', '7.4.5. How can we compare the results of classifying according to several categories?', 'https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm'),
]

def fetch(item):
    name, title, url = item
    dest = OUT/name
    assert not dest.exists()
    cmd = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https', '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2500000', '--retry', '0', '--user-agent', 'castle-gardener/1.0', '--output', str(dest), '--write-out', '%{http_code}', url]
    start = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=45)
    data = dest.read_bytes() if dest.exists() else b''
    if p.returncode == 0 and p.stdout == '200' and name.endswith('.html'):
        parser = Text(); parser.feed(data.decode('utf-8', errors='replace'))
        lines = [' '.join(s.split()) for s in ''.join(parser.parts).splitlines()]
        dest.with_name(dest.stem+'-text.txt').write_text('\n'.join(s for s in lines if s)+'\n')
    return dict(file=name, title=title, url=url, command=cmd, start_utc=start, finish_utc=datetime.now(timezone.utc).isoformat(), curl_exit=p.returncode, http_status=p.stdout, error=p.stderr, sha256=sha256(data).hexdigest(), bytes=len(data))

if __name__ == '__main__':
    assert not (OUT/'before.json').exists()
    names = ['courtyard.md', 'questions.md', 'quests.md', 'chronicle.md', 'gate.md', 'rooms/what-the-gaps-can-say.md', 'words/time-bin.md']
    before: dict = dict(recorded_at=datetime.now(timezone.utc).isoformat(), files={}, garden_sha256={}, rooms=sorted(p.name for p in (ROOT/'rooms').glob('*.md')))
    for name in names:
        p = ROOT/name
        assert ROOT in p.resolve().parents
        before['files'][name] = dict(text=p.read_text(), sha256=sha256(p.read_bytes()).hexdigest()) if p.exists() else None
    for p in sorted((ROOT/'garden').rglob('*')):
        if p.is_file():
            assert ROOT in p.resolve().parents
            before['garden_sha256'][str(p.relative_to(ROOT))] = sha256(p.read_bytes()).hexdigest()
    before['scope'] = 'Research oldest eligible questions 740 then 744; 766 not researched. Use the same fourteen saved visits, not new service traffic. Fix UTC bins [00,06), [06,12), [12,18), [18,24) before calculation, label each request by its own start, retain timeout as failed wait, never call bins host working hours. Tabulate first-view change labels and each round\'s client waits separately; count completed-view gaps that cross bin boundaries. No inferred event kinds, event starts, rates, significance tests or question closures. Empty courtyard and sixteen open questions: file zero, plant zero. Edit one room, one new word, one Map line; append one chronicle line.'
    (OUT/'before.json').write_text(json.dumps(before, indent=2)+'\n')
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, SOURCES))
    (OUT/'sources.json').write_text(json.dumps(results, indent=2)+'\n')
    for r in results: print(r['file'], 'HTTP', r['http_status'], 'curl', r['curl_exit'], 'bytes', r['bytes'])
