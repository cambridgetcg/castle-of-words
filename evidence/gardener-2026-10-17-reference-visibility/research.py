"""Bounded public-source retrieval and a before-state receipt; no service probes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def save(name, value):
    with (HERE / name).open('x') as f:
        json.dump(value, f, indent=2)
        f.write('\n')

def garden_hashes():
    result = {}
    for path in sorted((ROOT / 'garden').rglob('*')):
        if path.is_file() and not path.is_symlink():
            assert path.resolve().is_relative_to(ROOT)
            result[str(path.relative_to(ROOT))] = sha(path.read_bytes())
    return result

def main():
    assert not (HERE / 'before.json').exists(), 'refuse to repeat retrieval'
    tracked = ['courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md',
               'rooms/what-the-gaps-can-say.md']
    questions = (ROOT / 'questions.md').read_text().splitlines()
    chronicle = (ROOT / 'chronicle.md').read_bytes()
    save('before.json', {
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'tracked_sha256': {p: sha((ROOT / p).read_bytes()) for p in tracked},
        'chronicle_bytes': len(chronicle),
        'chronicle_lines': len(chronicle.splitlines()),
        'question_lines_sha256': {str(i): sha(line.encode()) for i, line in enumerate(questions, 1)},
        'open_question_lines': [i for i, line in enumerate(questions, 1) if line.startswith('- [ ]')],
        'room_paths': sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'rooms').glob('*.md')),
        'garden_sha256': garden_hashes(),
    })
    query = 'site:git-scm.com/docs transfer.hideRefs uploadpack hideRefs advertisement security'
    base = 'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/'
    sources = [
        ('search-brave.html', 'Brave Search: ' + query,
         'https://search.brave.com/search?q=' + quote(query)),
        ('transfer.txt', 'Git v2.39.5 configuration: transfer', base + 'config/transfer.txt'),
        ('uploadpack.txt', 'Git v2.39.5 configuration: uploadpack', base + 'config/uploadpack.txt'),
        ('gitprotocol-pack.txt', 'Git v2.39.5: gitprotocol-pack', base + 'gitprotocol-pack.txt'),
        ('gitprotocol-http.txt', 'Git v2.39.5: gitprotocol-http', base + 'gitprotocol-http.txt'),
        ('gitnamespaces.txt', 'Git v2.39.5: gitnamespaces', base + 'gitnamespaces.txt'),
    ]
    def fetch(item):
        name, title, url = item
        dest = HERE / name
        assert not dest.exists()
        command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https',
                   '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2097152',
                   '--retry', '0', '--user-agent', 'castle-gardener/1.0',
                   '--output', str(dest), '--write-out', '%{http_code}', url]
        started = datetime.now(timezone.utc).isoformat()
        done = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=50)
        data = dest.read_bytes() if dest.exists() else b''
        return {'title': title, 'url': url, 'file': name, 'started_utc': started,
                'finished_utc': datetime.now(timezone.utc).isoformat(), 'curl_exit': done.returncode,
                'http_status': done.stdout, 'stderr': done.stderr, 'bytes': len(data),
                'sha256': sha(data), 'command': command}
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, sources))
    save('sources.json', results)
    print(json.dumps([{k: r[k] for k in ('file', 'http_status', 'curl_exit', 'bytes')} for r in results], indent=2))
    text = (HERE / 'search-brave.html').read_text(errors='replace')
    links = sorted(set(re.findall(r'href="(https?://[^"<>]+)"', text)))
    save('search-links.json', links)
    print('Search links:', json.dumps(links[:30], indent=2))

if __name__ == '__main__':
    main()
