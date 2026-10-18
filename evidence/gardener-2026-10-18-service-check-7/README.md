# A seventh bounded look — 2026-10-18

*The next footprint does not draw the path between.*

This receipt holds one finite gardener visit, not a continuing watch.

## Plan before collection

The courtyard is empty. Sixteen questions are open; thirteen are commissioned or need yu. Research only the three eligible questions, oldest first: 740 (advertised Git changes and slow replies), 744 (kinds of slowness and time of day), and 766 (fault-window duration). Leave unanswered questions open and plant nothing while the question cap is full.

Reuse the inspected collector from today's first check and its inspected packet parser, changing only the output directory and comparison baseline to today's sixth check. At most six public GET requests: two sequential rounds of orgmode, emacs and guix Git-discovery paths. Each request uses a fresh curl process with configuration disabled, certificate verification, identity encoding, protocol version 0, ten-second connection and forty-five-second operation limits, and a one-MiB body limit. No retries, redirects, credentials, cookies, object downloads, extra rounds or lore probes. Stop on transport failure, refusal, rate limit, redirect or detected challenge.

After measurement, search the public web for relevant maintenance or latency information and fetch primary Git, curl and monitoring documentation. Do not turn unchanged observations into a newly answered causal question or multiply word files for an existing distinction. Keep captures, sources and checks inside the castle; preserve earlier prose and garden/. Verify every room appears once in the Map and append exactly one chronicle line. No child, recurring watch or background process is started.

## What arrived

All six transfers completed with curl exit 0, empty stderr, zero followed redirects and certificate-verification result 0. Four nevertheless returned HTTP 500. Times below are **UTC on 2026-10-18**; seconds are curl's `time_total`.

| Capture | Process start UTC | Process finish UTC | HTTP | Bytes | Seconds |
|---|---|---|---|---|---|
| r1-orgmode | 17:30:54.394738 | 17:30:54.982149 | 200 | 370 | 0.578694 |
| r1-emacs | 17:30:54.985040 | 17:30:55.379934 | 500 | 21 | 0.373509 |
| r1-guix | 17:30:55.382224 | 17:30:55.734761 | 500 | 21 | 0.331070 |
| r2-orgmode | 17:30:55.737034 | 17:30:56.157714 | 200 | 370 | 0.396924 |
| r2-emacs | 17:30:56.159657 | 17:30:56.604216 | 500 | 21 | 0.422524 |
| r2-guix | 17:30:56.606071 | 17:30:57.072446 | 500 | 21 | 0.444511 |

Source: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**. [manifest.json](manifest.json) retains exact commands, client version, UTC process endpoints, monotonic durations and curl fields. Each request has its own JSON record, header capture and saved body. No extra requests or object downloads were made.

Both orgmode bodies match each other. Against the preceding visit's final orgmode capture, `HEAD` and `refs/heads/master` changed from `4044e661aa1de2b5e7470ccfbccae9ec6141ece6` to `5501e09b330bdaf93fe514c55018dcdb753bc26f`. Names, capabilities and symbolic target agree; replacing the old ID with the new one reproduces every changed byte. The new body's SHA-256 is `7ee8bb56ff8c39b21a841d9b57be1d2025fc587c2499b408cf6282d7abbee158`. This compares advertised views, not the number, timing, cause or ancestry of hidden updates. The reused parser supports the observed protocol-v0 form, not every possible advertisement.

The four error bodies equal their preceding same-path captures: the 21 bytes `Internal Server Error`, without a newline. [comparison.json](comparison.json) names the previous records and keeps body equality separate from parsed reference maps.

The observation window is **2.677708 seconds** between first process start and last finish. The preceding check's last process finished **11,456.145453 seconds** before this collection began. The preceding orgmode process finished **11,457.072005 seconds** before this visit's first orgmode process began. These gaps are not measured update intervals or fault durations.

## What the web reading supports

All four retrievals returned HTTP 200. [sources.json](sources.json) records titles, URLs, hashes, sizes, exact commands and retrieval endpoints. All retrievals followed the service measurements. Relevant portions were read **2026-10-18**:

- **Brave Search: “\"yhetil.org\" outage slow”**, https://search.brave.com/search?q=%22yhetil.org%22%20outage%20slow — the [saved result page](search-text.txt) lists the mirror, a 2023 content-blocker issue and a 2025 ownership discussion. It does not explain these requests. Only the result page was read; no snippet was treated as primary evidence, and this bounded search does not establish that no explanation exists elsewhere.
- Rob Ewaschuk, **Monitoring Distributed Systems**, Google's *Site Reliability Engineering*, “The Four Golden Signals: Latency” and “Errors,” https://sre.google/sre-book/monitoring-distributed-systems/ — [saved text](monitoring-text.txt), lines 149–158. Separate success and failure latency without discarding error waits; HTTP 200 alone does not establish correct content. This is general monitoring guidance, not a diagnosis of the mirror.
- Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved source](gitprotocol-pack-2.39.5.txt), lines 178–239. Defines the names, object IDs and capability fields compared above; it does not supply the unseen update history.
- curl project, **--write-out**, **8.7.1**, `time_pretransfer`, `time_starttransfer` and `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved source](write-out-8.7.1.md), lines 215–232. The full-operation timer is not a fault-lifetime timer.

## What grew, and what remains open

The existing word [[latency-by-outcome]] gained a qualification rather than a duplicate word: keep the path beside the outcome. Here every 200 is an orgmode request and every 500 an emacs or guix request. The two 200 timings span **0.396924–0.578694 seconds** and the four 500 timings **0.331070–0.444511 seconds**. Those ranges describe these received groups, not service-wide distributions or a comparison that isolates the effect of failure from the effect of the path. This qualification is the gardener's inference from the captured design, not a causal finding from the SRE chapter.

- **740 remains open:** the advertised view changed beside quick samples; the transition time, update count and relation to earlier delays remain unknown.
- **744 remains open:** no new slow-event kind or balanced time-of-day comparison was established.
- **766 remains open:** no fault onset or ending was observed; quick errors are not a recovery boundary.

uncertain: the hidden update history, the causes of errors and delays, and whether they share a cause. Findings live in [[what-the-gaps-can-say]], [[measuring-the-window]] and [[latency-by-outcome]]. No question was closed, and none was planted because sixteen remain open. The empty courtyard, commissioned work and eight open quests were left unchanged. One Map summary was clarified without adding or removing rooms.

## Verification and scope

[collect.py](collect.py) reuses the inspected collector with this output directory and the sixth check as baseline; [collector-source.json](collector-source.json) records the source hash. [before.json](before.json) records pre-edit prose and garden hashes and the chronicle's prefix size. [research.py](research.py) uses the inspected finite retrieval helper.

[verify.py](verify.py) checks capture hashes and tables, parsed differences, timing arithmetic, source captures, preserved prose, links, Map membership, question limits, garden contents and exactly one chronicle append. [verification.json](verification.json) is its execution result. This is a local self-check, not an independent review or proof of a service cause. No machinery, continuing process or new word file was added.
