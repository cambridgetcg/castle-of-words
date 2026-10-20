"""Offline ad-hoc verification, not the project's canonical suite.

Malformed records below are synthetic fixtures, never remote observations.
Analysis/verifier writes are intercepted; only the ad-hoc receipt is saved.
"""
import contextlib
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import importlib.util
import io
import json
from pathlib import Path
import runpy
import sys
import unittest
from unittest.mock import patch

ROOT = Path('/Users/yu/castle')
OUT = ROOT / 'evidence/gardener-2026-10-20-http-date'
AUDIT, VERIFY = OUT/'audit.py', OUT/'verify.py'
READ_BYTES = Path.read_bytes
sources = {str(p.relative_to(ROOT)): sha256(READ_BYTES(p)).hexdigest() for p in (AUDIT, VERIFY)}
spec = importlib.util.spec_from_file_location('castle_http_date_audit_adhoc', AUDIT)
assert spec is not None and spec.loader is not None
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def fixture(header=None, timeout_header=b'', mismatch_body=False):
    """Build explicitly synthetic input entirely in memory."""
    prefix = 'evidence/gardener-2026-10-20-http-date/__adhoc_fixture__/'
    first, second = prefix+'r1-orgmode.json', prefix+'r2-orgmode.json'
    body = b'fixture only, not a remote reply\n'
    if header is None:
        header = b'HTTP/1.1 200 OK\r\nDate: Sat, 17 Oct 2026 02:53:05 GMT\r\nAge: 0\r\n\r\n'
    records = {
        first: dict(start_utc='2026-10-17T02:53:05.185254+00:00',
                    finish_utc='2026-10-17T02:53:05.902452+00:00', curl_exit=0,
                    curl_metrics={'time_total': '0.708186'}, body_present=True,
                    body_sha256=sha256(b'different fixture' if mismatch_body else body).hexdigest()),
        second: dict(start_utc='2026-10-17T02:54:00+00:00',
                     finish_utc='2026-10-17T02:54:45+00:00', curl_exit=28,
                     curl_metrics={'time_total': '45.000000'}, body_present=False),
    }
    files = {p: json.dumps(record).encode() for p, record in records.items()}
    files[str(Path(first).with_suffix('.headers'))] = header
    files[str(Path(first).with_suffix('.body'))] = body
    files[str(Path(second).with_suffix('.headers'))] = timeout_header
    prior = dict(rows=[{'capture': p} for p in records],
                 input_sha256={p: sha256(data).hexdigest() for p, data in files.items()})
    files[audit.INPUT] = json.dumps(prior).encode()
    assert not (ROOT/Path(second).with_suffix('.body')).exists()
    return files


def analyse(files=None):
    saved = {}
    def capture(name, value):
        saved[name] = value
    def fake_read(path):
        assert files is not None
        path = Path(path)
        key = str(path.relative_to(ROOT)) if path.is_absolute() else str(path)
        return files[key]
    with contextlib.ExitStack() as stack:
        stack.enter_context(patch.object(audit, 'save', side_effect=capture))
        stack.enter_context(patch.object(audit.subprocess, 'run', side_effect=AssertionError('Subprocess forbidden in offline analysis')))
        stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
        if files is not None:
            stack.enter_context(patch.object(audit, 'read', side_effect=fake_read))
        audit.analyse()
    return saved['analysis.json']


def verify(overrides=None):
    saved = {}
    overrides = overrides or {}
    def guarded_write(path, text, *args, **kwargs):
        assert path == OUT/'verification.json', path
        saved[str(path)] = json.loads(text)
        return len(text)
    def patched_read(path):
        return overrides[str(path)] if str(path) in overrides else READ_BYTES(path)
    with patch.object(Path, 'write_text', guarded_write), \
         patch.object(Path, 'read_bytes', patched_read), \
         patch.object(sys, 'argv', [str(VERIFY), '--closed']), \
         contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(str(VERIFY), run_name='__main__')
    return saved[str(OUT/'verification.json')]


class AdHocChecks(unittest.TestCase):
    def test_source_compiles(self):
        for path in (AUDIT, VERIFY):
            with self.subTest(path=path.name):
                compile(READ_BYTES(path), str(path), 'exec', dont_inherit=True)

    def test_real_analysis_reproduces_saved_evidence_without_writes(self):
        expected = json.loads(READ_BYTES(OUT/'analysis.json'))
        actual = analyse()
        for key in ('summary', 'rows', 'completed_at_or_above_1s', 'input_sha256'):
            self.assertEqual(actual[key], expected[key], key)

    def test_real_closed_verification_passes_without_writes(self):
        result = verify()
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['saved_attempts'], 28)
        self.assertEqual(result['completed_dates'], 27)
        self.assertEqual(result['headerless_timeouts'], 1)
        self.assertEqual(result['map_rooms'], 697)
        self.assertEqual(result['chronicle_lines_added'], 1)
        self.assertTrue(result['garden_unchanged'])

    def test_subsecond_date_and_missing_timeout_are_distinct(self):
        result = analyse(fixture())
        self.assertEqual(result['summary']['date_before_process_start'], 1)
        self.assertEqual(result['summary']['headerless_timeouts'], 1)
        self.assertEqual(Fraction(result['rows'][0]['date_minus_start_seconds']), Fraction(-185254, 1000000))
        self.assertIsNone(result['rows'][1]['date'])
        self.assertIsNone(result['rows'][1]['finish_minus_date_seconds'])

    def test_corrupted_input_hash_is_rejected(self):
        files = fixture()
        prior = json.loads(files[audit.INPUT])
        prior['input_sha256'][prior['rows'][0]['capture']] = '0'*64
        files[audit.INPUT] = json.dumps(prior).encode()
        with self.assertRaises(AssertionError):
            analyse(files)

    def test_duplicate_date_is_rejected(self):
        header = b'HTTP/1.1 200 OK\r\nDate: Sat, 17 Oct 2026 02:53:05 GMT\r\nDate: Sat, 17 Oct 2026 02:53:05 GMT\r\n\r\n'
        with self.assertRaises(AssertionError):
            analyse(fixture(header=header))

    def test_wrong_weekday_or_non_utc_date_is_rejected(self):
        for value in ('Sun, 17 Oct 2026 02:53:05 GMT', 'Sat, 17 Oct 2026 02:53:05 +0100'):
            with self.subTest(value=value), self.assertRaises(AssertionError):
                analyse(fixture(header=('HTTP/1.1 200 OK\r\nDate: '+value+'\r\n\r\n').encode()))

    def test_unexpected_timeout_headers_are_rejected(self):
        with self.assertRaises(AssertionError):
            analyse(fixture(timeout_header=b'HTTP/1.1 200 OK\r\n\r\n'))

    def test_body_checksum_mismatch_is_rejected(self):
        with self.assertRaises(AssertionError):
            analyse(fixture(mismatch_body=True))

    def test_changed_protected_question_file_is_rejected(self):
        path = ROOT/'questions.md'
        with self.assertRaises(AssertionError):
            verify({str(path): READ_BYTES(path)+b'\n'})

    def test_missing_room_map_entry_is_rejected(self):
        path = ROOT/'gate.md'
        mutated = b''.join(line for line in READ_BYTES(path).splitlines(keepends=True)
                           if not line.startswith(b'- [what-the-gaps-can-say]'))
        self.assertNotEqual(mutated, READ_BYTES(path))
        with self.assertRaises(AssertionError):
            verify({str(path): mutated})

    def test_extra_chronicle_line_is_rejected(self):
        path = ROOT/'chronicle.md'
        with self.assertRaises(AssertionError):
            verify({str(path): READ_BYTES(path)+b'- fixture extra line\n'})

    def test_missing_final_word_links_are_rejected(self):
        path = ROOT/'words/http-date.md'
        mutated = b''.join(line for line in READ_BYTES(path).splitlines(keepends=True)
                           if not line.startswith(b'Links: '))
        with self.assertRaises(AssertionError):
            verify({str(path): mutated})


result = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(AdHocChecks))
after = {str(p.relative_to(ROOT)): sha256(READ_BYTES(p)).hexdigest() for p in (AUDIT, VERIFY)}
assert sources == after, 'Tested source changed during verification'
receipt = dict(kind='ad-hoc verification; not a canonical test/lint/build suite',
    recorded_at_utc=datetime.now(timezone.utc).isoformat(),
    status='PASS' if result.wasSuccessful() else 'FAIL',
    test_methods_run=result.testsRun, failures=len(result.failures), errors=len(result.errors),
    tested_source_sha256=sources, offline=True,
    analysis_and_verifier_writes_intercepted=True,
    synthetic_cases='Malformed inputs and in-memory edits are fixtures only, not remote observations.',
    runner=__file__)
(OUT/'ad-hoc-verification.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2))
sys.exit(0 if result.wasSuccessful() else 1)
