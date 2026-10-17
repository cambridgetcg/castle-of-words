# A fourth bounded check — 2026-10-17

*The names on a path are not the cause of the delay.*

This receipt keeps one finite gardener visit, not a new monitoring job.

## Plan recorded before collection

The courtyard is empty. Questions 740, 744 and 766 are the three eligible open questions, in age order: advertised changes beside slow replies, event kinds by time of day, and event widths. The other thirteen open questions are commissioned or reserved for yu. Sixteen are open, so plant nothing unless an answer actually frees a place.

Reuse the inspected collector and its limited protocol-v0 parser for at most two sequential rounds of public GETs to the orgmode, emacs and guix Git-discovery paths. Retain its settings: fresh curl processes with configuration disabled; certificate verification; `castle-gardener/1.0`; identity encoding; Git protocol version 0; 10-second connection and 45-second operation limits; 1 MiB response cap; no retries, credentials, cookies or redirect following. Stop at the first transport failure, refusal, rate limit, redirect or detected challenge. Do not add rounds in response to a slow or changed reply.

Keep commands, response headers and bodies, UTC endpoints, monotonic process times and curl timings. Compare with the preceding completed check. Then search the public web and read the HTTP Via specification and curl timing/proxy documentation. In particular, distinguish the proxy used by the client from intermediaries reported in the response; do not infer blame, precise topology or software authenticity from header strings.

All work stays inside the castle. Preserve prior evidence, commissioned questions and existing edits; do not change garden/ or start an unattended watch. Check sources, saved comparisons, room/word shapes, every-room-once Map coverage and exactly one appended chronicle line. Verification in this session is not independent review.

## What execution returned

All six planned service GETs completed with curl exit **0**, zero redirects, `proxy_used=0` and `ssl_verify_result=0`. No stop condition fired, no extra round followed the changed view, and no Git object was fetched.

Times below are UTC on **2026-10-17**. Seconds are curl's full-operation `time_total`, not server-only timing.

| Capture | Process start | Process finish | HTTP | Body bytes | Seconds |
|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 12:41:28.760885 | 12:41:29.163435 | 200 | 370 | 0.394287 |
| [r1-emacs](r1-emacs.json) | 12:41:29.165405 | 12:41:29.571510 | 500 | 21 | 0.380906 |
| [r1-guix](r1-guix.json) | 12:41:29.573410 | 12:41:29.918676 | 500 | 21 | 0.322168 |
| [r2-orgmode](r2-orgmode.json) | 12:41:29.920592 | 12:41:30.379251 | 200 | 370 | 0.435608 |
| [r2-emacs](r2-emacs.json) | 12:41:30.381274 | 12:41:30.779622 | 500 | 21 | 0.374629 |
| [r2-guix](r2-guix.json) | 12:41:30.781604 | 12:41:31.238131 | 500 | 21 | 0.433350 |

The [manifest](manifest.json) keeps commands, client version, intervals and metrics. The [comparison](comparison.json) retains parsed advertisements; the offline [inspection](inspection.json) checks the changed bytes, same-path gap and received Via values.

Both new orgmode bodies agree. Relative to the preceding check, the object ID in both `HEAD` and `refs/heads/master` changed from `5da905546619ed989e6f95159979c66ead2d4460` to `34098a39c71edf4bee2f0c265d80e40f59908831`. Names and capabilities match, and substituting the new ID for the old reproduces all the new body bytes. The new body's SHA-256 is `74262e08ea5699d6295e4c0f7035f43090dca988a003f193c0b39a1a1744cab4`. All four error bodies match their preceding captures and read `Internal Server Error`, without a newline.

The collection span is **2.477246 seconds**. The same-path gap from the preceding orgmode process's finish to this first orgmode process's start is **11,816.968365 seconds**. Neither span is a fault width or an exact Git transition bracket.

### What the path fields do—and do not—say

Every retained response has two Via field lines, in this order, despite the client's zero proxy-use flag:

```text
Via: HTTP/1.0 git.gammaspectra.live/git/go-away@v0.7.1-0.20251123044322-bb8d4a09a587+dirty
Via: 1.1 varnish (Varnish/7.1)
```

RFC 9110 distinguishes a client-selected proxy from a gateway behind the contacted address. Its Via rules allow response omission by HTTP-to-HTTP gateways, pseudonyms, removable software comments and certain same-protocol entry combinations. Neither a client proxy flag nor the number of entries is a complete topology measurement or a per-component timer.

There is also a concrete syntax mismatch: RFC 9110 §§5.6.2 and 7.6.3 require a recipient pseudonym to be a `token`, optionally followed by a port. The first value's would-be recipient contains `/` and `@`, which are not token characters. The second value's `varnish` recipient passes that narrow test. [inspect.py](inspect.py) retains all six raw field pairs and runs six explicitly synthetic character-boundary cases. It is **not a general Via or HTTP validator**. No value was silently repaired, and the syntax mismatch was not blamed for the service's errors.

- **740 remains open:** a changed received view beside quick samples does not establish an update time, update count, continuous quiet gap or independent schedule.
- **744 remains open:** no slow-event kind or time-of-day preference was established.
- **766 remains open:** no continuous fault's onset, ending or width was measured; header names add no timing boundary.

uncertain: the actual route, software, underlying update history and causes of the errors or earlier waits. The findings live in [[what-the-gaps-can-say]], [[measuring-the-window]] and the new word [[via-header]]. No question was marked answered; all sixteen remain open, so nothing was planted. No room was created.

## Search and sources

The following were fetched **2026-10-17**. Relevant standard sections and documentation entries were read, not merely their search snippets.

1. **yhetil.org Git discovery responses** — [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack). Observed at the six times above; no other service-path requests.
2. R. Fielding, M. Nottingham and J. Reschke, **RFC 9110: HTTP Semantics**, §§3.7, 5.3, 5.6.2 and 7.6.3 — https://www.rfc-editor.org/rfc/rfc9110.txt — [kept source](rfc9110.txt). These sections define intermediaries, field ordering, tokens and Via.
3. curl project, **--write-out**, version **8.7.1**, `proxy_used` and `time_total` — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [kept source](write-out-8.7.1.md). The former reports whether the transfer used a proxy; the latter measures the full operation in seconds.
4. **Brave Search: `"yhetil.org" "2026" "500"`** — https://search.brave.com/search?q=%22yhetil.org%22%20%222026%22%20%22500%22 — [kept text](search-1-text.txt). It explicitly relaxed its search operators because too few matches were found and returned unrelated material, not an incident diagnosis.
5. **Brave Search: `RFC 9110 Via received protocol pseudonym response intermediary`** — https://search.brave.com/search?q=RFC%209110%20Via%20received%20protocol%20pseudonym%20response%20intermediary — [kept text](search-2-text.txt). It returned the RFC and explanatory pages; the official RFC was read directly.
6. **Brave Search: `yhetil emacs guix mirror slow`** — https://search.brave.com/search?q=yhetil%20emacs%20guix%20mirror%20slow — the simpler follow-up returned **HTTP 429**, recorded in [followup-search.json](followup-search.json). No results were extracted or treated as evidence. Searching stopped; the rate limit was not bypassed.

[sources.json](sources.json) retains the first four source/search retrievals, all HTTP 200, with URLs, commands, dates and hashes. The follow-up receipt preserves the rate limit. A display-only Python command then raised `KeyError: 'links'` because it assumed even an unsuccessful search had parsed links; the HTTP receipt had already been saved successfully. Reading that saved receipt established the 429 without repeating the request. No castle text or prior evidence was damaged by the display error.

## Verification

[verify.py](verify.py) checks the saved response and source hashes, comparisons, chronology, request bounds, the narrow Via inspection, reserved questions, allowed file changes, unchanged garden/, room and word shapes, and every-room-once Map coverage. In pre-close mode it requires an unchanged chronicle; in final mode it requires the old prefix plus exactly one correctly shaped visit line. It makes no network requests and refuses to overwrite either result receipt. These are same-session checks, not independent review or a canonical project test suite.

The first verifier run stopped on an unsupported `zip(strict=True)` argument in this machine's Python. Replacing that with an explicit equal-length assertion and ordinary `zip` fixed the verifier; no capture or castle prose was changed to satisfy it. The [pre-close verification](pre-close-verification.json) then passed: six service captures, five retrieval receipts, six synthetic token cases, all 697 rooms listed once, sixteen questions still open and garden/ unchanged. The final close is checked separately in [verification.json](verification.json). `git diff --check` reported no whitespace errors in the touched tracked files.

## Follow-up ad-hoc verification

On **2026-10-17**, a temporary `hermes-verify-` script, allocated with Python's `tempfile` under the requested macOS temporary directory, ran **15 focused tests: all passed, with zero failures and zero errors**. This is **ad-hoc verification**, not a canonical project suite or independent review. The [passing receipt](ad-hoc-verification.json) keeps the test log and hashes of all four tested scripts.

The tests replayed the six retained service responses through the collector and its repeat guards; exercised a synthetic transport timeout; replayed all four source/search responses; checked synthetic HTTP 429 and timeout outcomes without retries; enforced the collection prerequisite; recomputed the Via inspection and its character boundary; rejected out-of-scope list/port syntax and a corrupt Git packet; checked overwrite guards; ran the actual final workspace verifier; and confirmed rejection of injected capture/source corruption, an altered inspection, a nonexistent Map entry, an extra chronicle line, a changed reserved question, and an out-of-root path or symlink.

Network sockets and external process creation were blocked throughout the tests. **No live requests were made.** Retained files and castle text were unchanged during testing, no additional chronicle entry was appended, and the temporary script, staging file and fixture directories were removed. The four script hashes were checked again after cleanup and still match the passing receipt.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[via-header]] · [[reference-advertisement]] · [[observation-gap]]

