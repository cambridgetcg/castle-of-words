"""Run the inspected finite collector once, retaining all earlier evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREVIOUS = ROOT / 'evidence/gardener-2026-10-17-service-check-2'
COLLECTOR = ROOT / 'evidence/gardener-2026-10-17-service-check/observe.py'
PARSER = ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert ROOT == Path('/Users/yu/castle')
    assert not (HERE / 'reuse.json').exists(), 'refuse repeated collection'
    assert not (HERE / 'before.json').exists(), 'refuse repeated collection'
    tracked = list((ROOT / 'rooms').glob('*.md')) + list((ROOT / 'words').glob('*.md'))
    tracked += [ROOT / p for p in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md')]
    assert all(p.resolve().is_relative_to(ROOT) for p in tracked)
    baseline = {
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'collector_path': str(COLLECTOR.relative_to(ROOT)),
        'collector_sha256': sha(COLLECTOR.read_bytes()),
        'parser_path': str(PARSER.relative_to(ROOT)),
        'parser_sha256': sha(PARSER.read_bytes()),
        'tracked_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in tracked},
        'plan_sha256': sha((HERE / 'README.md').read_bytes()),
    }
    with (HERE / 'reuse.json').open('x') as stream:
        json.dump(baseline, stream, indent=2)
        stream.write('\n')
    main_function = runpy.run_path(str(COLLECTOR))['main']
    main_function.__globals__['HERE'] = HERE
    main_function.__globals__['OLD'] = PREVIOUS
    main_function()


if __name__ == '__main__':
    main()
