"""Run the inspected finite collector once in this receipt's own directory."""
from pathlib import Path
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'evidence/gardener-2026-10-18-service-check/collect.py'

if __name__ == '__main__':
    assert ROOT == Path('/Users/yu/castle')
    assert not (HERE / 'before.json').exists(), 'no repeat collection'
    main = runpy.run_path(str(SOURCE))['main']
    main.__globals__['HERE'] = HERE
    main.__globals__['OLD'] = SOURCE.parent
    with (HERE / 'collector-source.json').open('x') as f:
        json.dump({'path': str(SOURCE.relative_to(ROOT)),
                   'sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest()}, f, indent=2)
        f.write('\n')
    main()
