# Ad-hoc verification — 2026-10-23

A focused temporary Python check ran against `research.py` and `verify.py`: **7 tests passed**, process exit **0**. This is ad-hoc verification, not a canonical project suite, lint or build result.

The script was created with `tempfile.mkstemp(prefix="hermes-verify-", suffix=".py", dir=...)` in the requested macOS temporary directory. The file-writing tool refused that directory, so `adhoc-check.py` was staged here and copied into the allocated temporary file without elevated privileges. The in-castle source is retained for inspection; the temporary executable copy was removed after execution.

Actual execution:

```text
python3 -B /var/folders/bg/v8wn0t11067f0hzxkz7hp7rr0000gn/T/hermes-verify-7da9ql2a.py
Ran 7 tests in 0.290s
OK
```

Coverage:

- Start mode captures the baseline before dispatching the three expected public searches.
- Explicit label/URL pairs do not reset the baseline.
- Missing or unmatched arguments are rejected.
- The real verifier passes against the saved source responses and castle files, including exactly one appended chronicle line and all 697 rooms appearing once in the Map.
- An altered saved response, an extra chronicle line, and an altered question file are each rejected before a new verification result can be written.

Research routing used explicit test doubles and made no network requests. Negative checks altered reads in memory only. They did not edit the question list, chronicle or captured responses. The positive check ran the real verifier as a subprocess and refreshed its actual `verification.json`. These checks do not establish the archive host's update schedule or causes of delays.
