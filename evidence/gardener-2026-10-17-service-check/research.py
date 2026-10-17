"""Public search/document retrieval after the finite service collection."""
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
assert (HERE / 'manifest.json').exists()
assert not (HERE / 'sources.json').exists(), 'do not repeat retrieval'
queries = ['site:curl.se time_starttransfer time_pretransfer server response', '"yhetil.org" "slow"']
base = 'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/'
items = [(f'search-{i}.html', 'Brave Search: ' + q, 'https://search.brave.com/search?q=' + quote(q)) for i, q in enumerate(queries, 1)]
items += [('write-out-8.7.1.md', 'curl 8.7.1: --write-out', base + 'cmdline-opts/write-out.md'),
          ('starttransfer-8.7.1.md', 'curl 8.7.1: CURLINFO_STARTTRANSFER_TIME_T', base + 'libcurl/opts/CURLINFO_STARTTRANSFER_TIME_T.md'),
          ('pretransfer-8.7.1.md', 'curl 8.7.1: CURLINFO_PRETRANSFER_TIME_T', base + 'libcurl/opts/CURLINFO_PRETRANSFER_TIME_T.md')]

def fetch(item):
    name, title, url = item
    dest = HERE / name
    assert not dest.exists()
    command = ['curl', '--disable', '--silent', '--show-error', '--proto', '=https',
               '--connect-timeout', '10', '--max-time', '40', '--max-filesize', '2097152',
               '--retry', '0', '--user-agent', 'castle-gardener/1.0',
               '--output', str(dest.relative_to(ROOT)), '--write-out', '%{http_code}', url]
    start = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=50)
    data = dest.read_bytes() if dest.exists() else b''
    return {'title': title, 'url': url, 'file': name, 'start_utc': start,
            'finish_utc': datetime.now(timezone.utc).isoformat(), 'curl_exit': proc.returncode,
            'http_status': proc.stdout, 'stderr': proc.stderr, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(), 'command': command}

with ThreadPoolExecutor(max_workers=5) as pool:
    sources = list(pool.map(fetch, items))
with (HERE / 'sources.json').open('x') as f:
    json.dump(sources, f, indent=2)
    f.write('\n')
links = {name: sorted(set(re.findall(r'href="(https?://[^"<>]+)"', (HERE / name).read_text(errors='replace')))) for name, _, _ in items[:2]}
with (HERE / 'search-links.json').open('x') as f:
    json.dump(links, f, indent=2)
    f.write('\n')
print(json.dumps([{k: row[k] for k in ('file', 'http_status', 'curl_exit', 'bytes')} for row in sources], indent=2))
print(json.dumps(links, indent=2))
