"""Ad-hoc checks, not a project suite: mocked dispatch and real receipts."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path('/Users/yu/castle')
HERE = ROOT / 'evidence/gardener-2026-10-23-ingestion-search'
RESEARCH = HERE / 'research.py'
VERIFY = HERE / 'verify.py'
HELPER = ROOT / 'evidence/gardener-2026-10-22-update-records/research.py'


class VisitHelperChecks(unittest.TestCase):
    def dispatch(self, args):
        calls = []

        def baseline():
            calls.append(('baseline', baseline.__globals__['HERE']))

        def fetch_pairs(pairs):
            calls.append(('fetch', pairs, fetch_pairs.__globals__['HERE']))

        def helper(path):
            self.assertEqual(Path(path), HELPER)
            return {'baseline': baseline, 'fetch_pairs': fetch_pairs}

        code = compile(RESEARCH.read_bytes(), str(RESEARCH), 'exec')
        with patch.object(runpy, 'run_path', side_effect=helper), \
             patch.object(sys, 'argv', [str(RESEARCH), *args]):
            exec(code, {'__name__': '__main__', '__file__': str(RESEARCH)})
        return calls

    def test_start_baseline_precedes_three_public_searches(self):
        calls = self.dispatch(['start'])
        self.assertEqual(calls[0], ('baseline', HERE))
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[1][0], 'fetch')
        self.assertEqual(calls[1][2], HERE)
        self.assertEqual(calls[1][1], [
            ('watch-search', 'https://search.brave.com/search?q=%22yhetil.org%22%20%22public-inbox-watch%22'),
            ('archive-watch-search', 'https://public-inbox.org/meta/?q=yhetil%20watch'),
            ('archive-update-search', 'https://public-inbox.org/meta/?q=yhetil%20update'),
        ])

    def test_explicit_pairs_do_not_reset_baseline(self):
        pairs = [('test-one', 'https://example.invalid/one'),
                 ('test-two', 'https://example.invalid/two')]
        calls = self.dispatch([item for pair in pairs for item in pair])
        self.assertEqual(calls, [('fetch', pairs, HERE)])

    def test_invalid_arguments_are_rejected(self):
        for args in ([], ['unpaired-label'], ['a', 'https://example.invalid', 'b']):
            with self.subTest(args=args), self.assertRaises(AssertionError):
                self.dispatch(args)

    def test_real_artifact_verification_passes(self):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        result = subprocess.run(
            [sys.executable, '-B', str(VERIFY)], cwd=ROOT, env=env,
            capture_output=True, text=True, timeout=45)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertTrue(data['passed'])
        self.assertEqual(data['phase'], 'closed')
        self.assertEqual(data['chronicle_lines_appended'], 1)
        self.assertEqual(data['changed_existing_grounds_files'], ['chronicle.md'])
        self.assertEqual(data['map_rooms_exactly_once'], 697)
        self.assertTrue(data['garden_unchanged'])
        self.assertEqual(len(data['retrievals']), 5)

    def rejects_altered_read(self, target, addition):
        original = Path.read_bytes
        code = compile(original(VERIFY), str(VERIFY), 'exec')
        seen = []

        def altered(path):
            raw = original(path)
            if path == target:
                seen.append(path)
                return raw + addition
            return raw

        with patch.object(Path, 'read_bytes', altered), \
             patch.object(Path, 'write_text', side_effect=RuntimeError('unexpected write')) as writes, \
             patch.object(sys, 'argv', [str(VERIFY)]), \
             contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(AssertionError):
                exec(code, {'__name__': '__main__', '__file__': str(VERIFY)})
            writes.assert_not_called()
        self.assertTrue(seen)

    def test_changed_saved_response_is_rejected(self):
        self.rejects_altered_read(HERE / 'duplicate-report.html', b'changed')

    def test_extra_chronicle_line_is_rejected(self):
        self.rejects_altered_read(ROOT / 'chronicle.md', b'- unexpected second line\n')

    def test_changed_question_file_is_rejected(self):
        self.rejects_altered_read(ROOT / 'questions.md', b'\nUnexpected question edit\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)
