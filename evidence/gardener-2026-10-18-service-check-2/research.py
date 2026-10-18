"""One bounded web search and two pinned definitions, after collection."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

if __name__ == '__main__':
    assert (HERE / 'manifest.json').exists()
    assert not (HERE / 'sources.json').exists()
    fetch = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-17-service-check-2/research.py'))['fetch']
    fetch.__globals__['HERE'] = HERE
    query = '"yhetil.org" mirror maintenance update'
    items = [
        ('search.html', 'Brave Search: ' + query, 'https://search.brave.com/search?q=' + quote(query)),
        ('write-out-8.7.1.md', 'curl 8.7.1 — --write-out',
         'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md'),
        ('gitprotocol-pack-2.39.5.txt', 'Git v2.39.5 — gitprotocol-pack: Pack protocol',
         'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt')]
    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(fetch, items))
    with (HERE / 'sources.json').open('x') as f:
        json.dump(rows, f, indent=2)
        f.write('\n')
    print(json.dumps([{k: r[k] for k in ('file', 'http_status', 'curl_exit', 'bytes')} for r in rows], indent=2))
    print(json.dumps(rows[0].get('links', []), indent=2))
