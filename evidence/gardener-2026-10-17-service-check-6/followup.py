"""A single narrower search plus the timeout and response-code definitions."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
fetch = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-17-service-check-2/research.py'))['fetch']
fetch.__globals__['HERE'] = HERE
query = '"yhetil.org" "500"'
items = [
    ('search-2.html', 'Brave Search: ' + query,
     'https://search.brave.com/search?q=' + quote(query)),
    ('max-time-8.7.1.md', 'curl 8.7.1 — --max-time',
     'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md'),
    ('response-code-8.7.1.md', 'curl 8.7.1 — CURLINFO_RESPONSE_CODE',
     'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_RESPONSE_CODE.md'),
]
if __name__ == '__main__':
    assert not (HERE / 'followup-sources.json').exists()
    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(fetch, items))
    with (HERE / 'followup-sources.json').open('x') as f:
        json.dump(rows, f, indent=2)
        f.write('\n')
    print(json.dumps([{k: r[k] for k in ('file', 'curl_exit', 'http_status', 'bytes')} for r in rows], indent=2))
    print(json.dumps(rows[0].get('links', []), indent=2))
