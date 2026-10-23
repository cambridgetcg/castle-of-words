"""Bounded public search for the oldest eligible castle question."""
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
        ('performance-search', 'https://search.brave.com/search?q=' + quote('"yhetil" "performance"')),
        ('slow-update-search', 'https://search.brave.com/search?q=' + quote('"yhetil" "orgmode" "slow"')),
    ])
else:
    args = sys.argv[1:]
    assert args and len(args) % 2 == 0
    fetch_pairs(list(zip(args[::2], args[1::2])))
