"""Finite public search and direct source reading, after service collection."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
HELPER = ROOT / 'evidence/gardener-2026-10-17-service-check-2/research.py'


def main():
    assert ROOT == Path('/Users/yu/castle')
    assert (HERE / 'manifest.json').exists()
    with (HERE / 'research-started.txt').open('x') as f:
        f.write(datetime.now(timezone.utc).isoformat() + '\n')
    fetch = runpy.run_path(str(HELPER))['fetch']
    fetch.__globals__['HERE'] = HERE
    queries = ['"yhetil.org" "2026" "500"',
               'RFC 9110 Via received protocol pseudonym response intermediary']
    items = [(f'search-{i}.html', 'Brave Search: ' + q,
              'https://search.brave.com/search?q=' + quote(q))
             for i, q in enumerate(queries, 1)]
    items += [
        ('rfc9110.txt', 'RFC 9110 — HTTP Semantics, Via and intermediaries',
         'https://www.rfc-editor.org/rfc/rfc9110.txt'),
        ('write-out-8.7.1.md', 'curl 8.7.1 — --write-out',
         'https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md'),
    ]
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(fetch, items))
    with (HERE / 'sources.json').open('x') as f:
        json.dump(rows, f, indent=2)
        f.write('\n')
    print(json.dumps([{k: r[k] for k in ('file', 'curl_exit', 'http_status', 'bytes')}
                      for r in rows], indent=2))
    print(json.dumps({r['file']: r.get('links', []) for r in rows[:2]}, indent=2))


if __name__ == '__main__':
    main()
