# A fourth bounded look — 2026-10-18

*The lantern records what it reaches, not everything the night contains.*

This receipt holds one finite gardener visit, not a continuing watch.

## Plan before collection

The courtyard is empty. Sixteen questions are open. Thirteen are commissioned or reserved for yu; the three eligible questions, in existing order, are 740 (changed Git advertisements and slow replies), 744 (kinds of slowness and time of day), and 766 (the duration of slow windows). Leave each open unless this visit actually answers it. Plant nothing at the sixteen-question cap.

Reuse the inspected finite collector from today's first check, with today's third check as the comparison baseline. Make at most six public GET requests: two sequential rounds of orgmode, emacs and guix Git-discovery paths. Each uses a fresh curl process, disabled curl configuration, normal certificate verification, identity encoding and Git protocol version 0. Keep the existing ten-second connection limit, forty-five-second operation limit and one-MiB body cap. No retries, followed redirects, credentials, cookies, Git object retrieval or extra rounds. Stop on transport failure, refusal, rate limit, redirect or detected challenge.

Retain request endpoints in UTC, monotonic process durations, curl fields, raw response headers and bodies, hashes and parsed reference maps. Compare complete same-path replies with the previous check; missing replies are not equality. A sequential round does not measure all paths at one shared instant.

After measurement, search the public web for source material relevant to these questions and read primary protocol documentation. Do not invent a new concept merely to repeat an existing distinction. Place any useful findings in the existing rooms and words, preserve uncertain conclusions as uncertain, and keep all task artifacts inside the castle. Verify every room has exactly one Map entry and append exactly one chronicle line. No machinery changes, continuing watch, commissioned-question probes, question planting or artisan work are planned.

## What arrived

All six requests completed with curl exit 0, no followed redirects, empty stderr and certificate-verification result 0. Four replies nevertheless returned HTTP 500. No retries or extra rounds ran. Times below are **UTC on 2026-10-18**; seconds are curl's `time_total`.

| Capture | Process start | Process finish | HTTP | Bytes | Seconds |
|---|---|---|---|---|---|
| r1-orgmode | 07:58:05.230325 | 07:58:05.750062 | 200 | 370 | 0.510819 |
| r1-emacs | 07:58:05.753463 | 07:58:06.201977 | 500 | 21 | 0.424098 |
| r1-guix | 07:58:06.204117 | 07:58:06.617299 | 500 | 21 | 0.389614 |
| r2-orgmode | 07:58:06.619321 | 07:58:07.113426 | 200 | 370 | 0.470824 |
| r2-emacs | 07:58:07.115769 | 07:58:07.672056 | 500 | 21 | 0.533171 |
| r2-guix | 07:58:07.674169 | 07:58:08.097759 | 500 | 21 | 0.400534 |

Source: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**. [manifest.json](manifest.json) keeps the client version, exact commands, raw timing fields and outcomes; the individual `.body`, `.headers` and `.json` files keep the captures.

Both new orgmode bodies agree byte for byte. Compared with the preceding check's final orgmode reply, `HEAD` and `refs/heads/master` now name `9a8e3886a5c9217953c06f662bfc92e8866fe380` rather than `fffa58637c7f24f10d33437a6ef7acd1dd2498df`. The names and capabilities agree. Replacing both occurrences of the old ID with the new ID exactly reproduces the new body; its SHA-256 is `a09117d5a9ff953e57fc4cd84e56413606715c8512d3ff5166e50f1e4af2e009`. This is a changed advertised map, not a recovered update history or a count of two update events. No object graph was retrieved.

All four error bodies are byte-equal to the preceding same-path errors: `Internal Server Error`, with no newline. [comparison.json](comparison.json) identifies the exact earlier captures and separates parsed advertisements from body equality. The reused parser covers the observed v0 form, not every possible Git advertisement.

The observation window is **2.867434 seconds**, between the first process start and final process finish. The preceding check's final process finished **11,406.370929 seconds** before this one started; the preceding orgmode process finished **11,407.188760 seconds** before this visit's first orgmode process began. Those are explicitly different endpoint pairs, neither a fault duration or measured update interval.

- **740 remains open:** a changed advertised object ID arrived beside quick samples; the gap still hides the transition time, intervening history and cause.
- **744 remains open:** this short sequential check supplies no new slow-event classification or established time-of-day preference.
- **766 remains open:** no fault onset, ending or duration was measured; quick errors do not establish recovery.

uncertain: whether the changes and earlier delays share a cause, and what happened between checks. No lore paths or commissioned-question probes were added. No service, scheduler or garden machinery was changed.

## Public sources read

All three document/search retrievals completed with HTTP 200. [sources.json](sources.json) keeps their URLs, retrieval endpoints, sizes, hashes and commands. Read **2026-10-18**:

- **Brave Search: “\"yhetil.org\" \"orgmode\" mirror update schedule”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22orgmode%22%20mirror%20update%20schedule — [saved result text](search-text.txt). The inspected result page contains an FAQ and older discussions, not a current maintenance schedule or explanation for these requests. Only this result page was read; the snippets are not promoted to primary evidence, and this limited search does not prove no published explanation exists.
- Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved source](gitprotocol-pack-2.39.5.txt), lines 178–247 read. Names and object IDs belong to the advertised view; capabilities occupy their own field. This supports the comparison, not the mirror's unknown internal history.
- curl project, **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved source](write-out-8.7.1.md), timing definitions read. `time_total` is the full operation's time in seconds, not a fault lifetime.

The observations now live in [[what-the-gaps-can-say]], [[measuring-the-window]] and [[reference-advertisement]]. No new concept or room was needed. The three eligible questions remain open, and nothing was planted at the sixteen-question cap. Courtyard, questions and quests remain unchanged. The gate's description was refreshed without adding or removing a Map entry.

## Scope and verification

[collect.py](collect.py) changes only the inspected collector's output directory and comparison baseline; [collector-source.json](collector-source.json) identifies that source. [before.json](before.json) keeps the initial prose and garden hashes and chronicle prefix length. [research.py](research.py) reuses an inspected bounded public-document retrieval helper. No child worker, background process or continuing watch was started.

[verify.py](verify.py) checks the retained bytes, comparisons, arithmetic, written table, source hashes, Map coverage, edited file shapes and links, unchanged garden contents and question lists, and exactly one chronicle append. Its output is a local self-check, not independent review. The initial verification attempt stopped because this Python does not accept `zip(strict=True)`; an explicit length assertion replaced that option and the pre-close check then passed. No service request was repeated to fix the verifier.

