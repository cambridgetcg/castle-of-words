"""Fetch a finite public reading; save a before-image before editing castle prose."""
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
    ('search.html', 'Brave Search: NIST homogeneous Poisson process number events time interval', 'https://search.brave.com/search?q=NIST%20homogeneous%20Poisson%20process%20number%20events%20time%20interval'),
    ('rfc2330.txt', 'Framework for IP Performance Metrics — RFC 2330', 'https://www.rfc-editor.org/rfc/rfc2330.txt'),
    ('git-pack.txt', 'Git v2.39.5: gitprotocol-pack — Pack protocol', 'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt'),
]

def fetch(item):
    name, title, url = item
    dest = OUT / name
    assert not dest.exists()
    cmd = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https', '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2500000', '--retry', '0', '--user-agent', 'castle-gardener/1.0', '--output', str(dest), '--write-out', '%{http_code}', url]
    started = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=45)
    data = dest.read_bytes() if dest.exists() else b''
    if p.returncode == 0 and p.stdout == '200' and name.endswith('.html'):
        parser = Text(); parser.feed(data.decode('utf-8', errors='replace'))
        lines = [' '.join(s.split()) for s in ''.join(parser.parts).splitlines()]
        dest.with_name(dest.stem + '-text.txt').write_text('\n'.join(s for s in lines if s) + '\n')
    return dict(file=name, title=title, url=url, command=cmd, start_utc=started, finish_utc=datetime.now(timezone.utc).isoformat(), curl_exit=p.returncode, http_status=p.stdout, error=p.stderr, sha256=sha256(data).hexdigest(), bytes=len(data))

if __name__ == '__main__':
    assert not (OUT/'before.json').exists() and not (OUT/'sources.json').exists()
    names = ['courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md', 'rooms/what-the-gaps-can-say.md', 'words/detection-exposure.md', 'words/observation-gap.md']
    snapshot = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'files': {}, 'rooms': sorted(p.name for p in (ROOT/'rooms').glob('*.md')), 'words': sorted(p.name for p in (ROOT/'words').glob('*.md'))}
    for name in names:
        p = ROOT/name
        assert ROOT in p.resolve().parents
        data = p.read_bytes()
        snapshot['files'][name] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data), 'text': data.decode()}
    # Hash machinery read-only, so the closing check can verify it was not changed.
    snapshot['garden_sha256'] = {}
    for p in sorted((ROOT/'garden').rglob('*')):
        if p.is_file():
            assert ROOT in p.resolve().parents
            snapshot['garden_sha256'][str(p.relative_to(ROOT))] = sha256(p.read_bytes()).hexdigest()
    snapshot['selected_question_lines'] = [740]
    snapshot['scope'] = 'Offline gap audit of the same fourteen saved visits; no service requests, new watcher, source-capture edits, or question closure. Three eligible questions: 740, 744, 766; take only oldest 740. Courtyard empty; sixteen open questions prohibit planting.'
    (OUT/'before.json').write_text(json.dumps(snapshot, indent=2) + '\n')
    with ThreadPoolExecutor(max_workers=3) as pool:
        result = list(pool.map(fetch, SOURCES))
    (OUT/'sources.json').write_text(json.dumps(result, indent=2) + '\n')
    for r in result: print(r['file'], r['http_status'], 'curl', r['curl_exit'], 'bytes', r['bytes'])
