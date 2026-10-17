"""Finite public search and source reading, after the service check."""
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
    queries = ['"yhetil.org" "2026" "outage"',
               'git protocol reference advertisement object-id refname capabilities']
    items = [(f'search-{i}.html', 'Brave Search: ' + q,
              'https://search.brave.com/search?q=' + quote(q))
             for i, q in enumerate(queries, 1)]
    items += [
        ('gitprotocol-pack-2.39.5.txt', 'Git v2.39.5 — gitprotocol-pack: Pack protocol',
         'https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt'),
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
