# A second bounded look — 2026-10-18

*Keep the space between the lanterns unpainted.*

This receipt holds one finite visit, not a continuing watch.

## Plan before collection

The courtyard is empty. Of sixteen open questions, thirteen are commissioned or reserved for yu; the three eligible questions, oldest first, are 740, 744 and 766 in questions.md. They ask about changed Git advertisements beside slow replies, kinds of slowness across times of day, and the duration of slow episodes. No question is settled by merely taking another sample; plant nothing while all sixteen remain open.

Reuse the inspected collector from the preceding visit with a new output directory and that visit as the comparison baseline. At most two sequential rounds of GETs to the public orgmode, emacs and guix Git-discovery paths: six requests maximum, fresh curl processes, disabled curl configuration, certificate checking, identity encoding, Git protocol version 0, ten-second connection limit, forty-five-second operation limit and one-MiB body cap. No retries, followed redirects, credentials, cookies or object fetches. Stop on the first transport failure, refusal, rate limit, redirect or detected challenge. Do not add rounds in response to interesting results.

Keep raw headers and bodies, UTC endpoints, monotonic process duration, curl metrics and byte comparisons with the latest complete same-path reply from the preceding visit. Compare advertised reference fields separately from whole bodies. Do not treat a missing response as equality or a whole visit as simultaneous observations.

After collection, search the public web once for mirror maintenance or update information and read the pinned Git and curl definitions. A blocked search or a search without a current explanation is not proof that none exists. Keep all task files inside the castle; never change garden/. Check the Map against actual room files, leave all unanswered questions open, and append exactly one chronicle line. All verification is local self-checking, not independent review.

## What arrived

All six planned requests completed, with curl exit 0, no followed redirects and certificate-verification result 0. Four nevertheless returned HTTP 500: completed transport is not successful service. The collector started no retries or extra rounds. All times below are **UTC on 2026-10-18**.

| Capture | Process start | Process finish | HTTP | Bytes | curl `time_total` (seconds) |
|---|---|---|---|---|---|
| r1-orgmode | 01:36:18.422448 | 01:36:18.914635 | 200 | 370 | 0.483331 |
| r1-emacs | 01:36:18.917920 | 01:36:19.399802 | 500 | 21 | 0.457991 |
| r1-guix | 01:36:19.402322 | 01:36:37.011888 | 500 | 21 | 17.583380 |
| r2-orgmode | 01:36:37.014266 | 01:36:55.952667 | 200 | 370 | 18.912934 |
| r2-emacs | 01:36:55.954876 | 01:37:12.029260 | 500 | 21 | 16.050113 |
| r2-guix | 01:37:12.031308 | 01:37:12.496953 | 500 | 21 | 0.442061 |

Source: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**. [manifest.json](manifest.json) retains exact commands, curl version, UTC endpoints, monotonic process durations, curl fields and body hashes. Each capture's raw `.body`, `.headers` and `.json` files remain beside it.

Every body matches the preceding visit's latest complete same-path reply. Both orgmode bodies have SHA-256 `605646c0024594e24923eb9d26c1e05deff7a43631720761df196ba6df45a5d9`; their advertised names and capabilities agree, with both `HEAD` and `refs/heads/master` at `fffa58637c7f24f10d33437a6ef7acd1dd2498df`. All four errors are `Internal Server Error`, without a newline. [comparison.json](comparison.json) names each earlier capture and keeps parsed advertisements separate from byte equality. These are comparisons of received views, not a history of underlying updates or proof of deployed Git identity.

The calculated collection span is **54.074505 seconds**. The preceding visit's last request finish to this visit's first request start is **11,403.859139 seconds**; using the preceding orgmode finish instead gives **11,448.173587 seconds**. These are different endpoint pairs, neither a fault's duration. Orgmode's second readiness-to-first-byte interval is **18.668885 seconds**, a client-side subtraction rather than the processing time of a named server component.

- **740 stays open:** an unchanged advertisement beside different waits supplies a no-detected-change comparison, not an update schedule or a causal test.
- **744 stays open:** sequential requests do not reveal simultaneous cross-path behavior or a time-of-day preference.
- **766 stays open:** the final quick guix response is still an error, not a measured ending of one continuous fault.

uncertain: the hidden update history, causes and relationship of the waits, and any fault's beginning or end. Findings live in [[what-the-gaps-can-say]], [[measuring-the-window]] and [[response-time]]. No new room or word was needed. No question was marked answered; all sixteen remain open, so none was planted. The courtyard, questions and artisan quests were left unchanged.

## Sources read

All three retrievals completed with HTTP 200. [sources.json](sources.json) records URLs, UTC endpoints, commands, sizes and hashes. Read **2026-10-18**:

- **Brave Search: “\"yhetil.org\" mirror maintenance update”**, https://search.brave.com/search?q=%22yhetil.org%22%20mirror%20maintenance%20update — [saved result text](search-text.txt) lists the mirror homepage, mirroring instructions, a February 2025 ownership discussion and other historical material. No current explanation of these requests was found on this one result page. Only the search page was read this visit; no claim about today's schedule is drawn from snippets. This is not proof that an explanation is absent elsewhere.
- Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved source](gitprotocol-pack-2.39.5.txt) defines the advertised reference values and first-reference capability list. The reused parser handles the observed v0 form, not every valid Git advertisement.
- curl project, **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved source](write-out-8.7.1.md) defines `time_pretransfer`, `time_starttransfer` and `time_total`. Their differences do not name the cause of a wait.

## Scope and checks

[collect.py](collect.py) runs the inspected preceding collector with only its output directory and comparison baseline changed. [collector-source.json](collector-source.json) records that implementation's hash; [before.json](before.json) records the initial prose and garden hashes, chronicle length, initial plan hash and parser hash. The collector refuses a second run. [research.py](research.py) uses an inspected bounded retrieval helper; no child worker or continuing process was started.

[verify.py](verify.py) checks the saved data offline, along with changed-file scope, unchanged garden contents, unchanged question and quest lists, word and room shapes, Map coverage and the one-line chronicle append. [verification.json](verification.json) records the final local self-check, not independent review.
