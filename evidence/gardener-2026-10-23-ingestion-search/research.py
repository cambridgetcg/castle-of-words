"""Bounded reading for the oldest eligible question; no service probes."""
from pathlib import Path
from urllib.parse import quote
import runpy
import sys

ROOT = Path('/Users/yu/castle').resolve()
HERE = Path(__file__).resolve().parent
assert HERE.is_relative_to(ROOT / 'evidence')
helper = runpy.run_path(str(ROOT / 'evidence/gardener-2026-10-22-update-records/research.py'))
baseline = helper['baseline']
fetch_pairs = helper['fetch_pairs']
baseline.__globals__['HERE'] = HERE
fetch_pairs.__globals__['HERE'] = HERE

if sys.argv[1:] == ['start']:
    baseline()
    fetch_pairs([
        ('watch-search', 'https://search.brave.com/search?q=' + quote('"yhetil.org" "public-inbox-watch"')),
        ('archive-watch-search', 'https://public-inbox.org/meta/?q=' + quote('yhetil watch')),
        ('archive-update-search', 'https://public-inbox.org/meta/?q=' + quote('yhetil update')),
    ])
else:
    args = sys.argv[1:]
    assert args and len(args) % 2 == 0
    fetch_pairs(list(zip(args[::2], args[1::2])))
