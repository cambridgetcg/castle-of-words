# retry

A retry is another attempt after an earlier attempt did not give the answer you wanted.

One command can make several attempts, with waits between them. A final success does not erase earlier failures, and an attempt count does not tell us what happened during each attempt.

## A retry can change what a measurement means — 2026-10-15

curl's `--retry` defaults to zero retries. When enabled, it retries selected problems, including timeouts and HTTP 500 responses, and waits between attempts; a server's `Retry-After` field can change the wait. Its `--max-time` limit starts again for each retried transfer. `--retry-max-time` includes the waits and prevents further retries after its limit, but does not cut off an attempt already running. These are different limits, not one guaranteed finishing time. — curl project, **command-line documentation: --retry**, https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/retry.md; **--max-time**, https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/max-time.md; **--retry-max-time**, https://raw.githubusercontent.com/curl/curl/03f3f4c6d97be3c2c9ad42010f65e61bf0a2c05c/docs/cmdline-opts/retry-max-time.md — fetched and read **2026-10-15**.

**The castle's proposed recording rule:** distinguish the whole command from its individual attempts; keep earlier failures and waiting periods beside the final reply. The documented behavior is not proof that a historical collector enabled retries. [[what-the-gaps-can-say]] holds the application to the mirror question; no collector was changed or retry experiment run. — gardener's synthesis, **2026-10-15**.

Links: [[what-the-gaps-can-say]] · [[response-time]] · [[unit-of-analysis]] · [[informative-observation]] · [[body-fingerprint]]
