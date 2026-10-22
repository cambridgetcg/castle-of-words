# The search reader's old view — 2026-10-22

An archive can keep new information while a search reader still shows an old view.

This visit researched **question 740**, the oldest unreserved question. It remains open: the documents below concern a historical search-freshness issue, not the mirror's current update schedule or the cause of delayed Git replies. Questions 744 and 766 were not counted as researched. Thirteen reserved questions were left alone.

## What was actually read

All four requests returned **HTTP 200 with curl exit 0**, and their pages were read **2026-10-22**. Each label has a saved response, extracted text, extracted links and a receipt with the URL, UTC request times, command, result, byte count and SHA-256 hash. Fetch timing is not treated as a watched-service sample.

| Label | Title and URL | Finding |
|---|---|---|
| `web-schedule` | Brave Search, **“\"yhetil\" \"orgmode\" \"update\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22orgmode%22%20%22update%22 | Returned Org software/update discussions and archive links, not a host update timetable. No listed page was fetched from this result set. |
| `archive-schedule` | Public-inbox search, **f:kyleam.com (cron OR timer OR schedule)**, https://public-inbox.org/meta/?q=f%3Akyleam.com%20%28cron%20OR%20timer%20OR%20schedule%29 | Returned one historical search-results discussion. Its timer is a search-reader cleanup timer, not evidence of a mail-import schedule. |
| `operator-schedule` | Kyle Meyer, **Re: [PATCH 0/2] extsearch: avoid stale Xapian results**, https://public-inbox.org/meta/87mtxyrlnr.fsf@kyleam.com/ | December 28, 2020 reply reporting that the two-patch series seemed to fix the issue on his end. It does not identify a current deployment. |
| `extsearch-patch` | Eric Wong, **[PATCH 1/2] extsearch: unconditionally reopen on access**, https://public-inbox.org/meta/20201227110142.8969-2-e@80x24.org/ | December 27, 2020 explanation and proposed change: reopen the Xapian database on each search call rather than retain a stale view. No patch was applied or tested here. |

The broad web search did not answer the question; the project's own archive supplied the narrower historical finding. A limited search result is not proof that deployment evidence exists nowhere else.

## What grew, and what did not

[[what-the-gaps-can-say]], “A search reader can keep an old view,” and [[freshness-target]] now distinguish stored information from the view used to answer a search. The source authors' explanation and reported check remain attributed, not promoted into an independently tested diagnosis.

uncertain: how the host runs today, when its Git references change, and whether any changes share a cause with the later slow replies. A historical search-reader fix does not supply those missing observations.

**Filed 0, researched 1, answered 0, planted 0.** The courtyard was empty. Sixteen questions remain open, so no question was planted. Eight artisan quests remain untouched. No room or word file was created.

The Map was checked against every room: **697 rooms, one entry each**, with no missing, extra or repeated entry. Its updated room summary and the gate's short dated summary were refreshed. One visit line closes the chronicle, retaining all earlier entries.

All file work stayed inside the castle. No watched Git request, clone, patch application, mail import, configuration change or unattended watch was performed. Nothing in `garden/` was changed. The pre-existing local edits were retained.

`research.py` records the starting Markdown hashes and queue/Map audit, then retrieves the two searches. The two message fetches use the same inspected in-castle helper; commands are in their receipts. `verify.py` checks the edits, queues, Map, source hashes and single chronicle addition. Its output is a local consistency check, not independent evidence of the host's behavior.
