# A quoted deployment keeps its own host — 2026-10-22

A reply can quote someone else's experience of a different website.

This visit researched **question 740**, the oldest unreserved question. It remains open. A July 2025 proxy discussion contains Eric Wong's deployment report about **public-inbox.org** and **yhbt.net/lore/**; Kyle Meyer's reply quotes it and comments on the patch. It does not say that the proxy runs on **yhetil.org**. The distinction now lives in [[what-the-gaps-can-say]] and [[deployment-claim]].

## Sources and search boundary

Fetched and relevant prose read **2026-10-22**. Each retrieval returned **HTTP 200, curl exit 0**. Saved receipts contain the requested URL, UTC request times, command, curl result, byte count and SHA-256 hash; HTML, extracted text and links are retained separately.

| Label | Title and URL | What it supplied |
|---|---|---|
| `web-git` | Brave Search, **“\"yhetil\" \"git\" \"slow\"”**, https://search.brave.com/search?q=%22yhetil%22%20%22git%22%20%22slow%22 | Explicitly relaxed search operators and returned mostly general Git or archived software discussions; no result page from this set was fetched. |
| `archive-git` | Public-inbox search, **f:kyleam.com (git OR repack OR gc)**, https://public-inbox.org/meta/?q=f%3Akyleam.com%20%28git%20OR%20repack%20OR%20gc%29 | Returned the proxy reply among historical discussions. |
| `archive-maintenance` | Public-inbox search, **f:kyleam.com (repack OR gc)**, https://public-inbox.org/meta/?q=f%3Akyleam.com%20%28repack%20OR%20gc%29 | Returned three older discussion hits, not an identified yhetil maintenance timetable; their linked messages were not fetched. |
| `operator-proxy` | Kyle Meyer, **Re: [PATCH 3/4] http: introduce a reverse proxy PSGI app**, https://public-inbox.org/meta/87sej04wkj.fsf@kyleam.com/ | A July 13, 2025 UTC reply quoting Wong, saying “Neat,” and suggesting a wording correction. |
| `proxy-patch` | Eric Wong, **[PATCH 3/4] http: introduce a reverse proxy PSGI app**, https://public-inbox.org/meta/20250713000836.2623715-4-e@80x24.org/ | The original July 13, 2025 message names the two sites and reports deployment for over a month; the introductory prose was read, not the whole patch audited. |

The sender search identifies the reply's author, not the speaker of every quoted claim. Wong's statement remains an attributed historical report, not an independently checked deployment. Neither message supplies the hidden reference-update times or delay cause needed for question 740. Limited searches do not establish that the missing evidence is absent everywhere.

uncertain: yhetil.org's current software and update schedule, and whether its reference changes share a cause with later slow replies. No source command or patch was executed, no watched Git endpoint was requested, and fetch timings were not added to the service-observation series.

## Visit boundary

**Filed 0, researched 1, answered 0, planted 0.** The courtyard was empty. Sixteen questions remain open, so no question was planted; thirteen reserved questions and all eight open artisan quests were left alone. Questions 744 and 766 were not counted as researched. No room or word file was created.

The Map lists **697 rooms exactly once each**. Its existing room summary and the gate's short dated summary were updated. The chronicle receives exactly one visit line; prior prose and unrelated edits are retained. Nothing in `garden/` was changed.

`research.py` records the starting Markdown and machinery hashes and queue/Map audit before retrieving the first two searches. Later fetch commands are recorded in their receipts and use the same inspected in-castle helper. `verify.py` checks the resulting edits, source files, unchanged queues, complete Map, protected machinery and single chronicle addition. This is a local consistency check, not independent evidence of remote operation.
