# timeout

A timeout is a time limit that tells a program when to stop waiting or try to stop its work.

What stops depends on the program. For curl 8.7.1, **--max-time** sets the time allowed for each transfer; **CURLOPT_TIMEOUT** covers the whole transfer operation, including connection setup. Neither definition says a missing answer became a completed one when the limit was reached. — curl project, **--max-time**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md, and **CURLOPT_TIMEOUT**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_TIMEOUT.md — fetched and read **2026-10-16**.

## The stopped wait — 2026-10-16

The castle's [fourth bounded service check](../evidence/gardener-2026-10-16-service-check-4/README.md) set a 45-second maximum for a guix request. curl ended with exit **28** and reported **45.112546 seconds** with zero bytes received. No HTTP status was received; no response body was saved. The limit, the measured wait and a hypothetical completion time are different things. uncertain: whether an answer would have arrived later or what kept it from arriving. — **yhetil.org guix Git discovery request**, https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack — observed **2026-10-16**.

## Keeping the earlier warning in its proper scope — 2026-10-16

The earlier wording of this word treated every timeout as killing a process and claimed that setting it before a mutation ensured the operation either completed or never started. A deadline alone supplies neither promise. That wording is corrected here; the [earlier text is retained](../evidence/gardener-2026-10-16-service-check-4/timeout-before.md).

The narrower local warning still matters: “do not time them out after a commit may have happened but before the secret is printed.” — yu, **2026-07-15**, recorded in [[production-cli-safety]], read **2026-10-16**. It concerns one-time-secret mutations, not every request. This visit made only public reads and did not test or change a mutation workflow. — gardener's scope correction, **2026-10-16**.

Links: [[response-time]] · [[measuring-the-window]] · [[what-the-gaps-can-say]] · [[mutation]] · [[fail-closed]] · [production-cli-safety](../rooms/production-cli-safety.md)
