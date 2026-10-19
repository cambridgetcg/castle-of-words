# Additional ad-hoc verification

After the visit's own checks, a focused temporary harness exercised the three changed Python files: `analyze.py`, `research.py` and `verify.py`.

The harness path was created with `tempfile.mkstemp`, using the `hermes-verify-` prefix in the requested macOS temporary directory. The file-writing tool refused that directory, so the harness was staged as a text file inside the castle and moved to the generated path without sudo. It ran with Python's `-B` flag.

## Actual result

The unittest runner reported **11 tests passed**, **0 failures**, in **0.065 seconds**, with process exit **0**. This is **targeted ad-hoc verification**, not a canonical project suite, independent review or proof of the service's unseen history.

Checks covered:

- Compilation of all three changed Python files.
- Fresh analysis of the actual saved records, with output writes intercepted; the resulting rows, summaries and input hashes matched the saved analysis.
- Rejection of out-of-order timing marks and a body-hash mismatch, introduced in memory only.
- A fresh closed-visit check of the Map, unchanged machinery, sources and exactly one chronicle addition, again with output writes intercepted.
- Detection of simulated machinery tampering without editing a machinery file.
- HTML script/style exclusion.
- Fetch metadata and text extraction for an explicitly mocked successful response.
- HTTP-error and transport-error handling using explicitly mocked failures.
- Refusal to overwrite an existing capture.

The mocked responses were test fixtures, not fetched research evidence. No new service or documentation request was sent during these checks. Temporary fixture directories used `TemporaryDirectory` cleanup; the harness and its staging file were removed after execution. The original observations, Python source files and chronicle were not changed by this additional verification.
