"""Reuse the inspected finite collector; never alter previous evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREVIOUS = ROOT / 'evidence/gardener-2026-10-17-service-check'
COLLECTOR = PREVIOUS / 'observe.py'
PARSER = ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert ROOT == Path('/Users/yu/castle')
    assert not (HERE / 'reuse.json').exists(), 'collection already started; do not repeat'
    assert not (HERE / 'before.json').exists(), 'collection already started; do not repeat'
    baseline = {
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'collector_path': str(COLLECTOR.relative_to(ROOT)),
        'collector_sha256': sha(COLLECTOR.read_bytes()),
        'parser_path': str(PARSER.relative_to(ROOT)),
        'parser_sha256': sha(PARSER.read_bytes()),
        'word_before_sha256': sha((ROOT / 'words/observation-window.md').read_bytes()),
        'word_paths': sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'words').glob('*.md')),
        'plan_sha256': sha((HERE / 'README.md').read_bytes()),
    }
    with (HERE / 'reuse.json').open('x') as f:
        json.dump(baseline, f, indent=2)
        f.write('\n')
    loaded = runpy.run_path(str(COLLECTOR))
    main_function = loaded['main']
    main_function.__globals__['HERE'] = HERE
    main_function.__globals__['OLD'] = PREVIOUS
    main_function()


if __name__ == '__main__':
    main()
