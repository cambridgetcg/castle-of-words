# A bounded archive search — 2026-10-23, 07:36–07:40 CEST

The search found no new evidence of when the Org mirror updated or why its later Git replies were delayed.

Question **740**, the oldest unreserved open question in [[questions]], was researched and remains open. The courtyard was empty. Questions reserved for yu or another builder were skipped; questions 744 and 766 were not counted as researched.

## Searches and reading

All pages below were requested **2026-10-23**. These notes record the tool results; no raw response archive was saved for this visit.

- Brave Search: **“\"yhetil.org\" mirror cron”**, https://search.brave.com/search?q=%22yhetil.org%22%20mirror%20cron; **“\"yhetil.org\" latency outage”**, https://search.brave.com/search?q=%22yhetil.org%22%20latency%20outage; **“\"yhetil.org\" \"varnish\"”**, https://search.brave.com/search?q=%22yhetil.org%22%20%22varnish%22 — all three requests returned **HTTP 429**. No search-result claims were drawn from those failures, and that engine was not retried.
- Public-inbox meta archive, **yhetil git — search results**, https://public-inbox.org/meta/?q=yhetil%20git — curl returned **HTTP 200**, displaying thirteen results. The April 2026 instance-directory discussion was followed; most other titles concerned historical import, rendering or message-lookup issues already considered in [[what-the-gaps-can-say]]. The other linked messages were not fetched this visit.
- Public-inbox meta archive, **f:kyleam.com (slow OR timeout OR latency) — search results**, https://public-inbox.org/meta/?q=f%3Akyleam.com%20%28slow%20OR%20timeout%20OR%20latency%29 — curl returned **HTTP 200**, displaying three results. The NNTP-support reply was followed.
- Public-inbox meta archive, **yhetil (load OR schedule OR interval) — search results**, https://public-inbox.org/meta/?q=yhetil%20%28load%20OR%20schedule%20OR%20interval%29 — curl returned **HTTP 404** with a rendered **“No results found”** page. This is a result for that query, not proof that a timetable or incident report is absent elsewhere.

The first attempts to retrieve those three archive searches with Python's HTTPS client failed with `TLSV1_ALERT_PROTOCOL_VERSION`. Switching to curl succeeded in retrieving the search pages. Certificate verification was not disabled. Each curl request was bounded by a thirty-second limit and had no automatic retry.

## What the two messages actually said

1. Kyle Meyer, **Re: [PATCH 28/34] watch: add NNTP support**, dated **2020-06-27**, https://public-inbox.org/meta/87sgeg5nxf.fsf@kyleam.com/ — fetched with HTTP 200 and read **2026-10-23**. The reply corrects the wording of a code comment about `Debug` and `Timeout` arguments. It does not report using NNTP ingestion at yhetil, identify an installed configuration, or report a delayed Git request. A keyword match is not an incident report.
2. Štěpán Němec, **Re: List of known public accessible public-inbox instances?**, dated **2026-04-01 UTC** (**2026-04-02** in its printed +02:00 offset), https://public-inbox.org/meta/20260401234024Z.4120899001-stepnem@smrk.net/ — fetched with HTTP 200 and read **2026-10-23**. The writer names yhetil.org and inbox.vuxu.org as instances he knows and uses or used, and discusses maintaining a mapping from mailing-list addresses to archive instances. This is neither a current health measurement nor a published schedule for the Org mirror.

uncertain: the mirror's hidden update times, current input path and configuration, and any relationship between updates and the recorded delays. The reading did not answer question 740. No watched Git endpoint was requested, no command from a source page was run, and no service measurement or continuing watch was started.

## Leave the castle without a duplicate explanation

The distinction between a historical statement and deployment evidence already lives in [[what-the-gaps-can-say]] and [[deployment-claims]]. No new explanation, word, room or question annotation was needed. A search that finds no answer should not make another room saying the same thing.

**Filed 0, researched 1, answered 0, planted 0.** All sixteen questions remain open, so none was planted. No making task arose. The gate's Map was checked against the room files: **697 rooms, each listed once, with no missing or stale entries**; it needed no edit. Garden machinery and existing work were left untouched. The visit ends with one appended chronicle line.
