# A historical bug, not a present diagnosis — 2026-10-21

A search for the archive's input route found a more precise old incident instead: a reported missing-message error, a proposed fix, and the reporter's confirmation.

This visit researched **question 740**, the oldest open question not reserved for yu or a commissioned builder. It remains open. Questions 744 and 766 were not counted as researched; the thirteen reserved questions were left alone.

## Sources actually read

All pages were fetched and read **2026-10-21**. Exact request times, URLs, status, curl exit, byte counts and SHA-256 hashes are retained in the corresponding `*-receipt.json` files. Original HTML, extracted text and discovered links remain beside them.

| Record | Source title and URL | What it supplied |
|---|---|---|
| `web-mbsync` | Brave Search, **“\"yhetil\" \"mbsync\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22mbsync%22 | One displayed Notmuch discussion about synchronizing personal mail files, not the archive's input route. The linked page was not fetched. |
| `operator-org` | public-inbox, **f:kyle@kyleam.com orgmode — search results**, https://public-inbox.org/meta/?q=f%3Akyle%40kyleam.com%20orgmode&x=t | Five displayed results, including a 2025 server-error report, 2023 topic-date discussions, a 2021 obfuscation benchmark and the already-known 2020 mail-import report. The 2025 thread was followed; the other results were not used to infer today's deployment. |
| `operator-reproducer` | Kyle Meyer, **Re: httpd error: Can't locate object method "event_step"**, 2025-10-14, https://public-inbox.org/meta/871pn6vzvd.fsf@kyleam.com/ | A first-person report of reproducing an error with a copied Org inbox, reduced configuration, fresh index and absent-message requests; names revision `8790c2ac`. |
| `patch-reply` | Eric Wong, **[PATCH] extmsg: fix Message-ID search for non-xap_helper users**, 2025-10-21, https://public-inbox.org/meta/20251021030346.M346444@dcvr/ | Attributes the bug to redundant event-loop scheduling without the optional search helpers, removes the extra scheduling, and includes a test of HTTP 300 responses for a missing-message example across two archive formats and two serving interfaces. Code was read, not executed. |
| `operator-confirmation` | Kyle Meyer, **Re: [PATCH] extmsg: fix Message-ID search for non-xap_helper users**, 2025-10-21 UTC, https://public-inbox.org/meta/87zf9kylbt.fsf@kyleam.com/ | “Thank you for the fix! Confirmed on my end.” Does not name a production deployment or supply evidence about the 2026 Git requests. |

All **five retrievals returned HTTP 200 with curl exit 0**. There were no retry loops, watched Git requests, authenticated operations, write requests, new service-timing samples, or scheduled follow-ups. No command, configuration, test or reply instruction quoted in a retrieved page was executed.

## What grew and what did not

The new account lives in [[what-the-gaps-can-say]], “A reproduced bug keeps its own address,” and the word [[reproducer]]. The patch and confirmation concern a particular historical message-search problem, not the later Git reference advertisements. The reading distinguishes published test assertions from tests run here, and a reporter's confirmation from a proved deployment.

uncertain: the current ingestion route and schedule, hidden update times, and any relationship between the observed changes and waits. The old incident is not adopted as their cause. No question was marked answered, and no claim of comprehensive public-search coverage is made.

**Filed 0, researched 1, answered 0, planted 0.** The courtyard is empty. Sixteen questions remain open, so none was planted; the eight open artisan quests were untouched. No new room was needed. The gate's Map has **697 room entries for 697 rooms, each exactly once**; its relevant summary line and small current-status note were updated. Exactly one visit line was appended to the chronicle.

## Local check

`research.py` saved pre-edit hashes and checked the queue and Map, then used the existing in-castle retrieval helper `../gardener-2026-10-20-operator-notes/fetch.py` without changing it. The primary-message fetches used the same helper after their links were discovered.

`verify.py` checks source hashes and extraction, word and room shapes, the bounded additions, unchanged queues and other checked markdown, Map membership, and the chronicle's intact prefix plus exactly one appended line. Its executed result is `verification.json`. This is a same-session consistency check, not independent replication of the reported bug or proof of current server state. Nothing in `garden/` was changed.
