"""One public search plus primary protocol texts, after the service measurement."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
HELPER = ROOT / 'evidence/gardener-2026-10-17-service-check-2/research.py'

if __name__ == '__main__':
    assert ROOT == Path('/Users/yu/castle')
    assert (HERE / 'manifest.json').exists()
    assert not (HERE / 'sources.json').exists()
    fetch = runpy.run_path(str(HELPER))['fetch']
    fetch.__globals__['HERE'] = HERE
    query = '"yhetil.org" "orgmode" mirror update schedule'
    items = [
        ('search.html', 'Brave Search: ' + query,
         'https://search.brave.com/search?q=' + quote(query)),
        ('gitprotocol-pack-2.39.5.txt', 'Git v2.39.5 — gitprotocol-pack: Pack protocol',
         'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt'),
        ('write-out-8.7.1.md', 'curl 8.7.1 — --write-out',
         'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md')]
    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(fetch, items))
    with (HERE / 'sources.json').open('x') as f:
        json.dump({'helper_path': str(HELPER.relative_to(ROOT)),
                   'helper_sha256': hashlib.sha256(HELPER.read_bytes()).hexdigest(),
                   'sources': rows}, f, indent=2)
        f.write('\n')
    print(json.dumps([{k: r[k] for k in ('file', 'http_status', 'curl_exit', 'bytes')} for r in rows], indent=2))
    print(json.dumps(rows[0].get('links', []), indent=2))
