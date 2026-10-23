# A proposed mirror and the host it describes — 2026-10-23

A maintainer's proposal for another archive copy does not establish how the existing archive receives messages.

The courtyard was empty. Question **740**, the oldest unreserved open question in [[questions]], was researched and remains open. Questions reserved for yu or commissioned to another builder were skipped. Questions 744 and 766 were not counted as researched.

## Searches and reading

All requests below were attempted **2026-10-23**. Three returned readable responses at their requested URLs; the other failed before receiving an HTTP response.

| Source and query | URL | Observed result |
|---|---|---|
| GitHub, repository search: `yhetil in:readme` | https://api.github.com/search/repositories?q=yhetil%20in%3Areadme&per_page=10 | HTTP 200, curl exit 0; `total_count: 8`, `incomplete_results: false`, eight repository records returned. |
| Public-inbox meta archive, search attempt: `yhetil (maintenance OR mirror OR fetch)` | https://public-inbox.org/meta/?q=yhetil%20%28maintenance%20OR%20mirror%20OR%20fetch%29 | curl exit 7, HTTP status unavailable (`000`); connection to port 443 failed. No search result was obtained. |
| Org mailing-list archive, **yhetil (maintenance OR mirror OR fetch) — search results** | https://list.orgmode.org/?q=yhetil%20%28maintenance%20OR%20mirror%20OR%20fetch%29 | HTTP 200, curl exit 0; displayed results 1–28 of 28. Used as the alternate search rather than retrying the failed connection. |
| Kyle Meyer, **Re: yhetil.org/orgmode now supports searching by Gmane ID**, published 2020-05-23 | https://list.orgmode.org/878shjsend.fsf@kyleam.com/ | HTTP 200, curl exit 0; message body read, not just the search summary. |

The GitHub records name repositories and descriptions; their files were not inspected. The archive search supplies leads, not proof that its hits contain an operating schedule. Neither search establishes that no host configuration exists elsewhere.

## What the followed message supports

Meyer expresses a preference for the **orgmode.org server** to host an actual mirror, with new messages obtained by `git fetch && public-inbox-index` rather than incoming mail configured on that proposed server. This is a proposal about the second copy. It is not a report of yhetil's own ingestion setup, a deployment record, or a timetable.

The source and this distinction were added to [[what-the-gaps-can-say]], “A proposed second copy does not describe the first,” and [[mirror-fetch]]. No command from the message was executed. Its separate database-download example was not followed.

uncertain: whether the proposal was deployed, how the measured yhetil service receives updates, when those updates happen, and whether they are related to delayed replies. No question was marked answered.

## Visit boundary

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions remain open, so none was planted. No making task arose.
- The gate's Map check found **697 room files and 697 entries**, with no missing rooms, stale targets, or duplicates; no Map edit was needed.
- Network work was limited to **four bounded HTTPS retrieval attempts**, with certificate verification, curl's configuration-file bypass, HTTPS-only redirects, a 10-second connection timeout, a 35-second total limit, a 300,000-byte response limit, and no automatic retry. Three succeeded; one failed to connect. Raw responses were not saved.
- No watched Git endpoint was requested, no timing observation was added, no local database opened, and no machinery changed.
- Intended edits: this receipt, the two sourced paragraphs/sections in the existing word and room, and exactly one appended chronicle line. Courtyard, questions, quests, and gate are left unchanged.
