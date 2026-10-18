"""Finite collection using the inspected collector and parser; no overwrites."""
from pathlib import Path
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / 'evidence/gardener-2026-10-18-service-check/collect.py'
BASELINE = ROOT / 'evidence/gardener-2026-10-18-service-check-6'

if __name__ == '__main__':
    assert ROOT == Path('/Users/yu/castle')
    assert not (HERE / 'before.json').exists(), 'refuse repeated collection'
    main = runpy.run_path(str(SOURCE))['main']
    main.__globals__['HERE'] = HERE
    main.__globals__['OLD'] = BASELINE
    with (HERE / 'collector-source.json').open('x') as f:
        json.dump({'path': str(SOURCE.relative_to(ROOT)),
                   'sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                   'baseline': str(BASELINE.relative_to(ROOT))}, f, indent=2)
        f.write('\n')
    main()
