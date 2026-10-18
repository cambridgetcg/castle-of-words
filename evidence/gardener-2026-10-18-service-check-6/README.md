# A sixth bounded look — 2026-10-18

*The clock can stop on an answer that did not help.*

This receipt holds one finite gardener visit, not a continuing watch.

## Plan before collection

The courtyard is empty. Sixteen questions remain open; thirteen are commissioned or need yu. Research the three eligible questions in oldest-first order: 740 (changed Git views and slow replies), 744 (kinds of slowness and time of day), and 766 (fault-window duration). Do not close an unanswered question or plant beyond the cap.

Reuse the inspected finite collector from today's first check, changing only its output directory and comparison baseline to today's fifth check. Make at most six public GET requests: two sequential rounds of orgmode, emacs and guix Git-discovery paths. Each uses a fresh curl process with configuration disabled, certificate verification, identity encoding, protocol version 0, ten-second connection and forty-five-second operation limits, and a one-MiB body limit. No retries, followed redirects, credentials, cookies, objects fetched, extra rounds, lore probes or work on commissioned questions. Stop on transport failure, refusal, rate limit, redirect or detected challenge.

After service collection, search the public web for maintenance or latency information and fetch primary monitoring, Git and curl documentation. Examine the distinction between successful and failed request latency rather than pooling every completed transfer as useful success. Source retrieval does not overlap service measurements. Keep sources, actual captures, clocks, hashes and comparison results inside the castle. Preserve earlier prose and garden/; check the Map against every room and append exactly one chronicle line. No child or continuing process is started.

## What arrived

All six transfers completed with curl exit 0, empty stderr, zero followed redirects and certificate-verification result 0. Four nevertheless returned HTTP 500. Times below are **UTC on 2026-10-18**; seconds are curl's `time_total`.

| Capture | Process start | Process finish | HTTP | Bytes | Seconds |
|---|---|---|---|---|---|
| r1-orgmode | 14:19:55.275146 | 14:19:55.791108 | 200 | 370 | 0.507058 |
| r1-emacs | 14:19:55.794399 | 14:19:56.227454 | 500 | 21 | 0.408333 |
| r1-guix | 14:19:56.229551 | 14:19:56.776414 | 500 | 21 | 0.523171 |
| r2-orgmode | 14:19:56.778405 | 14:19:57.322733 | 200 | 370 | 0.519966 |
| r2-emacs | 14:19:57.324866 | 14:19:57.734767 | 500 | 21 | 0.386223 |
| r2-guix | 14:19:57.736844 | 14:19:58.249285 | 500 | 21 | 0.488936 |

Source: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**. [manifest.json](manifest.json) keeps exact commands, client version, UTC process endpoints, monotonic process durations and curl fields. Each request also has its own `.json`, `.body` and `.headers` capture. No retry, redirect, extra round or object download occurred.

Both orgmode bodies agree byte for byte. Compared with the preceding visit's final orgmode capture, `HEAD` and `refs/heads/master` changed from `c135a282dc27f2c2ddc385e9116feafee8aed74d` to `4044e661aa1de2b5e7470ccfbccae9ec6141ece6`. Names, capabilities and symbolic target agree. Replacing the old ID with the new one reproduces every changed byte. The new body's SHA-256 is `bceb5592499b5f17e96839a8b03358ec8be0b2bebce9e7740cd4cc0b5c1e9799`. This compares received maps, not hidden update counts, ancestry, freshness or completeness. The reused parser covers the observed v0 form, not every possible Git advertisement.

The four error bodies equal their preceding same-path captures: the 21 bytes `Internal Server Error`, without a newline. [comparison.json](comparison.json) keeps those comparisons separate from parsed advertisements and names the previous captures.

The observation window is **2.974139 seconds**, between the first process start and the last finish. The preceding check's last process finished **11,382.044328 seconds** before this collection began; the preceding orgmode process finished **11,382.870437 seconds** before the first new orgmode process began. Neither gap is a fault duration or an update interval.

## What the sources add

All four public retrievals returned HTTP 200. [sources.json](sources.json) records their titles, URLs, byte counts, hashes, commands and retrieval endpoints. Sources were fetched after service collection, and the relevant portions were read **2026-10-18**:

- **Brave Search: “\"yhetil.org\" latency maintenance errors”**, https://search.brave.com/search?q=%22yhetil.org%22%20latency%20maintenance%20errors — the [saved result page](search-text.txt) lists the mirror's landing page, not an explanation of these requests. No snippet was treated as primary evidence. This bounded search does not establish that no explanation exists elsewhere.
- Rob Ewaschuk, **Monitoring Distributed Systems**, Google's *Site Reliability Engineering*, “The Four Golden Signals: Latency” and “Errors,” https://sre.google/sre-book/monitoring-distributed-systems/ — [saved text](monitoring-text.txt), lines 149–158. The chapter recommends separating successful-request latency from failed-request latency without throwing away the error timings. It also distinguishes wrong content returned with HTTP 200 from genuine success. This is monitoring guidance, not a diagnosis of yhetil.
- Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved source](gitprotocol-pack-2.39.5.txt), lines 178–239. Used to interpret names, object IDs and capability fields, not to infer the server's unseen history.
- curl project, **--write-out**, **8.7.1**, `time_starttransfer` and `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved source](write-out-8.7.1.md), timing definitions read. `time_total` measures the full operation, not a fault lifetime.

The new word [[latency-by-outcome]] carries the monitoring distinction into [[what-the-gaps-can-say]] and [[measuring-the-window]]. The received groups here are two parsed advertisement-shaped 200 responses (**0.507058–0.519966 seconds**) and four 500 responses (**0.386223–0.523171 seconds**). These descriptive ranges are not service-wide distributions. Parsing the advertisement is not an end-to-end test of repository correctness. No old ledger labels or observation policy were changed.

- **740 stays open:** the advertised view changed beside quick samples, but the transition time and its relationship to earlier delays remain unknown.
- **744 stays open:** separating outcomes gives a better comparison rule, not an event kind, balanced sample or time-of-day preference.
- **766 stays open:** no fault onset or ending was observed; fast failures do not supply a recovery boundary.

uncertain: the hidden update history, error causes, and whether changes and delays share a cause. No question was closed. Nothing was planted because sixteen questions are already open; the courtyard and eight open quests remain untouched. The gate summary was updated without changing Map membership.

## Verification and scope

[collect.py](collect.py) reuses the inspected collector with a new output directory and comparison baseline; [collector-source.json](collector-source.json) identifies the source and its hash. [before.json](before.json) records the original prose and garden hashes and chronicle prefix size. [research.py](research.py) reuses the inspected finite retrieval helper.

[verify.py](verify.py) checks the retained bytes, parsed differences, timing arithmetic, table, source captures, preserved prose, links, Map coverage, question cap, garden contents and exactly one chronicle append. [verification.json](verification.json) records its execution result. This is a local self-check, not independent review or proof of a service cause. No machinery change or continuing process was added.
