# A finite evening look — 2026-10-18

*The lantern we carry also casts a shadow.*

This receipt keeps one gardener visit and its limits, not a continuing watch.

## Plan before collection

The courtyard has no arrivals. Sixteen questions are open; thirteen are commissioned or need yu. Research the three eligible questions in their existing oldest-first order: 740 (changed Git advertisements and slow replies), 744 (observed kinds and time of day), then 766 (fault-window duration). Leave empirical questions open unless the evidence answers them; plant nothing while sixteen remain open.

Reuse the inspected finite collector and limited Git packet parser, with the seventh check today as the comparison baseline. At most six public GET requests: two sequential rounds of orgmode, emacs and guix discovery. Keep the same request settings, a ten-second connection limit, forty-five-second operation limit and one-MiB body cap. No credentials, cookies, redirects, retries, object downloads, extra rounds or lore probes. Stop on transport failure, refusal, rate limit, redirect or detected challenge.

After collection, search the public web and fetch RFC 7799 plus pinned Git and curl documentation. Investigate whether these deliberately generated requests are active measurements and what that classification does and does not say about disturbing the measured service. All files stay within the castle; do not change garden/, start a watcher, alter a schedule, or touch commissioned work. Keep the writing small, verify the Map against all rooms, and append exactly one chronicle line.

## Results

All six transfers completed, with curl exit 0, no followed redirect and successful certificate checks. Four replies were still HTTP 500. All times in this table are **UTC on 2026-10-18**; seconds are curl's full-operation `time_total`.

| Capture | Start UTC | Finish UTC | HTTP | Bytes | Seconds |
|---|---|---|---|---|---|
| r1-orgmode | 20:42:09.355184 | 20:42:09.769017 | 200 | 370 | 0.405859 |
| r1-emacs | 20:42:09.771146 | 20:42:10.200086 | 500 | 21 | 0.407925 |
| r1-guix | 20:42:10.202073 | 20:42:10.629507 | 500 | 21 | 0.407112 |
| r2-orgmode | 20:42:10.631554 | 20:42:11.073911 | 200 | 370 | 0.420832 |
| r2-emacs | 20:42:11.075974 | 20:42:11.440942 | 500 | 21 | 0.343136 |
| r2-guix | 20:42:11.443081 | 20:42:11.841741 | 500 | 21 | 0.375055 |

Source: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**. [manifest.json](manifest.json) retains exact commands, UTC intervals, monotonic process durations, curl version and metrics. Each request's JSON, headers and body remain here. No objects were downloaded and no additional round was made.

The two orgmode bodies agree. Compared with the previous visit's final complete capture, `HEAD` and `refs/heads/master` change from `5501e09b330bdaf93fe514c55018dcdb753bc26f` to `27b26db39953b726b5bd42c461679b8c3f387b80`. Names and capabilities, including the symbolic target, agree. Replacing the old ID with the new reproduces every changed byte. The new body's SHA-256 is `233f4847f5dc4fc5aacd7e81c84abbb0e2ae436948fc9fa2bb3010ca0a92e0c4`. The four error bodies match their previous same-path captures: `Internal Server Error`, 21 bytes without a newline. The limited parser checks the observed protocol-v0 form, not every possible Git reply, repository completeness or freshness. [comparison.json](comparison.json) separates byte equality from parsed views.

The collection spans **2.486557 seconds**. The previous collection's final process ended **11,472.282738 seconds** before this one began; the same-path orgmode gap is **11,473.197470 seconds**. These are measured gaps between process endpoints, not a hidden update schedule or continuous fault duration. All full-operation times span **0.343136–0.420832 seconds**.

## Sources read and understanding added

All four public retrievals returned HTTP 200 after service collection finished. [sources.json](sources.json) keeps their exact commands, retrieval times, sizes and hashes. Relevant portions were read **2026-10-18**:

- **Brave Search: “RFC 7799 active measurement traffic influence”**, https://search.brave.com/search?q=RFC%207799%20active%20measurement%20traffic%20influence — [saved result text](search-text.txt) located RFC 7799. Snippets were not used as primary evidence or as proof of a host condition.
- A. Morton, **Active and Passive Metrics and Methods (with Hybrid Types In-Between)**, RFC 7799, https://www.rfc-editor.org/rfc/rfc7799.txt — [saved text](rfc7799.txt), §§1, 3.4, 3.6 and 3.8. Generated measurement streams are distinguished from passive observation; added test traffic influences measured quantities and should have its effect quantified or minimized. Even exporting passive observations can add traffic. The May 2016 text is the cited definition, not a claim that a later draft has been adopted.
- Git project, **gitprotocol-pack — Pack protocol**, v2.39.5, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved source](gitprotocol-pack-2.39.5.txt), “Reference Discovery,” lines 178–239, defines the compared fields.
- curl project, **--write-out**, 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved source](write-out-8.7.1.md), timing fields, lines 203–232; the timer describes the operation, not a fault's lifetime.

The new word [[active-measurement]] applies the RFC's distinction to these deliberately generated requests. A read-only requested operation is not an absence of test traffic. The fixed cap limits our work without measuring its influence; this is not evidence that the probes caused errors or delays. Findings were added to [[what-the-gaps-can-say]] and [[measuring-the-window]], with dated sources and explicit unknowns.

- **740 remains open:** the advertised view changed beside quick replies, but its transition time, unseen history and relation to slowness were not established.
- **744 remains open:** the visit supplies no new slow-event kind or balanced comparison across times of day.
- **766 remains open:** neither fault onset nor recovery was observed; the collection span is not an event width.

uncertain: the size of any measurement-induced effect, the hidden update history, and the causes of errors and delays. No question was closed and none planted while sixteen remain open. The courtyard, questions, quests and commissioned work were left unchanged. No continuing process was started.

## Verification

[collect.py](collect.py) records its inspected source in [collector-source.json](collector-source.json); [before.json](before.json) holds the pre-edit content and garden hashes. [research.py](research.py) retrieves only the four declared sources. [verify.py](verify.py) checks capture hashes, the table and arithmetic, comparison results, preservation of existing prose, new links, word and room shapes, all Map entries, question limits, garden/ and exactly one appended chronicle line. [verification.json](verification.json) is the executed local self-check, not independent review or proof of a service cause.
