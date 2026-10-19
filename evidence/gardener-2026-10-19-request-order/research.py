"""Bounded public reading and a pre-edit snapshot; no mirror probes or external writes."""
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

def safe(path):
    assert ROOT in path.resolve().parents, path
    return path

if not (OUT / 'before.json').exists():
    files = [ROOT / x for x in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md')]
    files += [p for p in (ROOT / 'garden').rglob('*') if p.is_file()]
    before = {'files': {}, 'rooms': sorted(p.name for p in (ROOT/'rooms').glob('*.md')), 'words': sorted(p.name for p in (ROOT/'words').glob('*.md')), 'old_gate_lines': {}}
    for p in files:
        data = safe(p).read_bytes()
        before['files'][str(p.relative_to(ROOT))] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data), 'lines': len(data.splitlines())}
    for line in (ROOT/'gate.md').read_text().splitlines():
        if line.startswith('> rooms:') or line.startswith('- [what-the-gaps-can-say]'):
            before['old_gate_lines'][line.split(' — ', 1)[0] if line.startswith('- ') else '> rooms:'] = line
    (OUT/'before.json').write_text(json.dumps(before, indent=2)+'\n')

SOURCES = [
    ('search.html', 'Brave Search: NIST time series temporal order lag plot observations', 'https://search.brave.com/search?q=NIST%20time%20series%20temporal%20order%20lag%20plot%20observations'),
    ('rfc2330.txt', 'Framework for IP Performance Metrics — RFC 2330', 'https://www.rfc-editor.org/rfc/rfc2330.txt'),
    ('curl-write-out.md', 'curl 8.7.1: --write-out', 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md'),
    ('git-pack.txt', 'Git v2.39.5: gitprotocol-pack — Pack protocol', 'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt'),
]

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.hidden = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden-1)
        if tag in ('p', 'li', 'div', 'h1', 'h2', 'h3', 'br'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden: self.parts.append(data)

def fetch(item):
    name, title, url = item
    path = OUT/name
    command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https', '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2500000', '--retry', '0', '--user-agent', 'castle-gardener/1.0', '--output', str(path), '--write-out', '%{http_code}', url]
    started = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=45)
    data = path.read_bytes() if path.exists() else b''
    if p.returncode == 0 and p.stdout == '200' and name.endswith('.html'):
        text = Text(); text.feed(data.decode('utf-8', errors='replace'))
        lines = [' '.join(s.split()) for s in ''.join(text.parts).splitlines()]
        path.with_name(path.stem+'-text.txt').write_text('\n'.join(s for s in lines if s)+'\n')
    return dict(file=name, title=title, url=url, command=command, start_utc=started, finish_utc=datetime.now(timezone.utc).isoformat(), curl_exit=p.returncode, http_status=p.stdout, error=p.stderr, sha256=sha256(data).hexdigest(), bytes=len(data))

if __name__ == '__main__':
    assert not (OUT/'sources.json').exists(), 'Do not silently refetch a completed reading.'
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, SOURCES))
    (OUT/'sources.json').write_text(json.dumps(results, indent=2)+'\n')
    for r in results: print(r['file'], r['http_status'], 'curl', r['curl_exit'], 'bytes', r['bytes'])
