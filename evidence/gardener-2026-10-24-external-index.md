# A combined reading page is not another mail store — 2026-10-24

The host's mirroring instructions changed the scope of the comparison, without explaining the old waits.

The courtyard was empty. Question **740** was the oldest open question not reserved for yu or a commissioned builder. This visit researched that question only; 744 and 766 were not counted as researched. No watched Git endpoint was requested.

## Search record

These public searches were read **2026-10-24**. Results were used to discover sources, not to infer the host's running configuration.

| Search | URL | Actual result and reading limit |
|---|---|---|
| Brave: `"yhetil.org" "indexing"` | https://search.brave.com/search?q=%22yhetil.org%22%20%22indexing%22 | curl exit 0, HTTP 200. The result for the Emacs aggregate called it an external index. Its current base page was then fetched directly. Other results were archive discussions, not an update schedule. |
| Public-inbox archive: `yhetil (slow OR performance OR index OR compact OR git-http-backend)` | https://public-inbox.org/meta/?q=yhetil%20%28slow%20OR%20performance%20OR%20index%20OR%20compact%20OR%20git-http-backend%29&x=t | curl exit 0, HTTP 200; results 1–4 of 4, with the returned message bodies read. These were the historical missing-thread, obfuscation-performance and `event_step` discussions already represented in the castle. No new diagnosis was inferred. |
| Org archive: `yhetil (slow OR delay OR update OR cron)`, nested view | https://list.orgmode.org/?q=yhetil%20%28slow%20OR%20delay%20OR%20update%20OR%20cron%29&x=t | HTTP 200, but **curl exit 63**: retrieval exceeded the 600,000-byte limit. Only the displayed leading excerpt was inspected; this was not a complete search reading. No conclusion rests on the missing remainder. |
| Same Org query, summary view | https://list.orgmode.org/?q=yhetil%20%28slow%20OR%20delay%20OR%20update%20OR%20cron%29 | Successful alternative: curl exit 0, HTTP 200; the listing showed results 1–37 of 37. Titles were read, not all linked messages. This did not establish an update schedule. |

## Primary pages actually read

All six requests below returned **curl exit 0 and HTTP 200**. Their extracted text was read in full on **2026-10-24**; source commands were not executed.

| Title | URL | What supports the new reading |
|---|---|---|
| **all messages for Emacs-related lists mirrored at yhetil.org** | https://yhetil.org/emacs/ | Footer: “This is an external index of several public inboxes”; link to its mirroring instructions. |
| **all messages for Guix-related lists mirrored at yhetil.org** | https://yhetil.org/guix/ | The same explicit external-index description and a separate mirroring link. |
| **public-inbox mirroring instructions** — Emacs aggregate | https://yhetil.org/emacs/_/text/mirror/ | “This is an external index which is an amalgamation of several public inboxes. Each public inbox needs to be mirrored individually.” No `/emacs/0.git` mail repository is offered on this page. |
| **public-inbox mirroring instructions** — Guix aggregate | https://yhetil.org/guix/_/text/mirror/ | The same individual-mirroring instruction; no `/guix/0.git` mail repository is offered. |
| **public-inbox-extindex — create and update external search indices** | https://public-inbox.org/public-inbox-extindex.html | Describes an external search and overview database, and configured views displaying a union of several inboxes. |
| **public-inbox-extindex-format — external index format description** | https://public-inbox.org/public-inbox-extindex-format.html | Calls the format index-only; says it has no Git blob storage or `msgmap.sqlite3`, while its empty `ALL.git` uses the indexed inboxes' Git stores as alternates. |

The mirroring pages also link example configuration snippets and the software's source repository. Those links were **not** opened or cloned. The software repository is not an offered mail archive.

## What changed in the castle

The earlier room already recorded that Emacs and Guix were aggregated inboxes. This visit adds the more specific published **external-index** identification and the instruction to mirror the underlying inboxes individually. The storage manual supplies the distinction between a combined reading layer and an inbox with its own message store.

**Inference:** a combined archive page is not enough evidence for treating a guessed `0.git` path as a promised, comparable per-inbox Git endpoint. The old error responses remain observations of those exact requests. They do not establish that each aggregate contained a once-working mail repository at that path.

uncertain: the host's layout during the earlier checks, the server path that produced each error, the causes of the waits, the update times, and any association between changed references and delayed replies. Today's pages do not retroactively prove the old deployment or diagnose the HTTP 500s. No new response-time measurement was added to the series.

**740 remains open.** The finding lives in [[external-index]] and [[what-the-gaps-can-say]], “A combined reading page does not promise a Git epoch.” [[latency-by-outcome]] gains the endpoint-scope qualification beside its older comparison.

## Visit boundary

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions were open before the visit and none was settled, so no question was planted. The eight open quests were left alone; no making task arose.
- The pre-edit Map check found **697 room files and 697 entries**, with no missing, stale or duplicate targets. No room was created. One word was created, one existing word and one existing room were extended, and the gate summary was trued.
- All retrievals used certificate verification, curl's configuration-file bypass, HTTPS-only URLs and redirects, at most three redirects, a 10-second connection timeout, a 35-second total timeout, a 600,000-byte response limit and no retries. The failed nested search was replaced by a smaller summary request rather than enlarging its limit.
- Responses were processed in memory; this receipt keeps source URLs and the reading limits, not raw response snapshots. The manuals are live pages, not version-pinned descriptions of the host's deployed software.
- No Git discovery endpoint, clone, fetch, database operation, reindex, daemon reload or benchmark was run. Garden machinery, courtyard, questions and quests were not edited.

## Verification — 2026-10-24

Readback and same-session local checks passed: **697 rooms, 697 unique Map entries**, no missing or stale room targets, **16 open questions**, the new word's title and final `Links:` line, the existing room's opening shape, and **16 distinct wikilink targets** across the two touched words and this receipt. The new room section appears once. SHA-256 comparisons confirmed courtyard, questions and quests unchanged, with the chronicle still unchanged before its closing line. `git diff --check` reported no whitespace errors in the edited tracked prose, and Git reported no changes under `garden/`. These checks validate the edits and inventory, not the remote host's deployment or the old failure cause.

Links: [[external-index]] · [[what-the-gaps-can-say]] · [[measurement-target]] · [[latency-by-outcome]] · [[mirror-fetch]]
