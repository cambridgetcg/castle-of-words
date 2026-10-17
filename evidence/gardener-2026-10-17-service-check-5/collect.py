"""Reuse an inspected finite collector; keep prior receipts unchanged."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COLLECTOR = ROOT / 'evidence/gardener-2026-10-17-service-check/observe.py'
PARSER = ROOT / 'evidence/gardener-2026-10-16-service-check-5/observe.py'
PREVIOUS = ROOT / 'evidence/gardener-2026-10-17-service-check-4'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert ROOT == Path('/Users/yu/castle')
    assert not (HERE / 'reuse.json').exists()
    assert not (HERE / 'before.json').exists()
    paths = list((ROOT / 'rooms').glob('*.md')) + list((ROOT / 'words').glob('*.md'))
    paths += [ROOT / p for p in ('courtyard.md', 'questions.md', 'quests.md', 'gate.md', 'chronicle.md')]
    assert all(p.resolve().is_relative_to(ROOT) for p in paths)
    baseline = {
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'collector_path': str(COLLECTOR.relative_to(ROOT)),
        'collector_sha256': sha(COLLECTOR.read_bytes()),
        'parser_path': str(PARSER.relative_to(ROOT)),
        'parser_sha256': sha(PARSER.read_bytes()),
        'tracked_sha256': {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in paths},
        'plan_sha256': sha((HERE / 'README.md').read_bytes()),
    }
    with (HERE / 'reuse.json').open('x') as f:
        json.dump(baseline, f, indent=2)
        f.write('\n')
    collect = runpy.run_path(str(COLLECTOR))['main']
    collect.__globals__['HERE'] = HERE
    collect.__globals__['OLD'] = PREVIOUS
    collect()


if __name__ == '__main__':
    main()
