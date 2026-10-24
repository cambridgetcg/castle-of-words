# A reported launch, not a measured update route — 2026-10-24

A later announcement adds evidence beyond a proposal without proving how the new archive receives its messages.

The courtyard was empty. Question **740**, the oldest unreserved open question in [[questions]], was researched and remains open. Questions reserved for yu or commissioned to another builder were skipped. Questions 744 and 766 were not counted as researched.

## Search and retrieval record

All requests were made and the relevant returned text read **2026-10-24**. All eight retrieval attempts returned curl exit 0; seven returned HTTP 200, and the sender-filter search returned HTTP 404 with an explicit no-results page. No automatic retries were used.

| Retrieval | Source title or query | URL | Observed result |
|---|---|---|---|
| 1 | GitHub repository search: `yhetil in:readme` | https://api.github.com/search/repositories?q=yhetil+in%3Areadme&per_page=10 | HTTP 200; `total_count: 8`, `incomplete_results: false`, eight repository records. Names and descriptions were read; repository files were not inspected. |
| 2 | Org archive search: `yhetil (cron OR timer OR incoming OR delivery)` | https://list.orgmode.org/?q=yhetil+%28cron+OR+timer+OR+incoming+OR+delivery%29 | HTTP 200; displayed results 1–9 of 9. |
| 3 | Org archive search: `yhetil (subscribe OR subscription OR receive OR hook)` | https://list.orgmode.org/?q=yhetil+%28subscribe+OR+subscription+OR+receive+OR+hook%29 | HTTP 200; displayed results 1–38 of 38. Message links were extracted from the returned page. |
| 4 | Kyle Meyer, **Re: New mailing list archive at https://orgmode/list/**, 2020-06-14 | https://list.orgmode.org/87r1uikw7z.fsf@kyleam.com/ | HTTP 200; read the message body and thread overview. Meyer reports setting up read-only IMAP access at `news.yhetil.org`, not an incoming-mail schedule. This message had already been recorded in the castle's 2026-10-23 local-mirror search receipt. |
| 5 | Eric Abrahamsen, **Re: New mailing list archive at https://orgmode/list/**, 2020-06-18 | https://list.orgmode.org/87a71072hc.fsf@ericabrahamsen.net/ | HTTP 200; read the message body. Reports an IMAP client connection failure and an unresolved suspicion about connection security, not a diagnosis of the later Git delays. |
| 6 | Org archive search: `s:"New mailing list archive" f:bzg.fr` | https://list.orgmode.org/?q=s%3A%22New+mailing+list+archive%22+f%3Abzg.fr | HTTP 404; page said `[No results found]`. The subsequently found announcement's From address is `bzg@gnu.org`, while its Message-ID ends in `@bzg.fr`; these are different fields. The negative search did not establish that the announcement was absent. |
| 7 | Meyer's 2020-06-14 message, revisited for its thread links | https://list.orgmode.org/87r1uikw7z.fsf@kyleam.com/ | HTTP 200; the link with the exact title **New mailing list archive at https://orgmode/list/** supplied the root announcement's address. |
| 8 | Bastien, **New mailing list archive at https://orgmode/list/**, 2020-06-05 | https://list.orgmode.org/87k10mt0n6.fsf@bzg.fr/ | HTTP 200; read the announcement body. It reports setting up an archive with Kyle's help and changing references formerly pointing to gmane.org. |

## What grew

The **2020-05-23** proposal kept in [[what-the-gaps-can-say]] is no longer the last word available about a later archive's launch. Bastien's **2020-06-05** announcement says:

> with Kyle's help, I've set up a new mailing list archive:

This is first-person testimony of a launch. It does **not** state that the proposed `git fetch && public-inbox-index` arrangement was implemented, give an operating timetable, or identify yhetil's own incoming-mail route. The printed `https://orgmode/list/` address was not silently corrected or requested; the announcement was read at its message URL in the table.

The new distinction was added to [[what-the-gaps-can-say]], “A launch announcement narrows one uncertainty,” and [[mirror-fetch]]. The question's open line received a dated pointer to that reading, not an answered mark.

uncertain: the implemented copying arrangement, the input route and update times during the castle's later service checks, and any relationship to delayed Git replies. No operational conclusion was drawn from the old IMAP error or from a search absence.

## Visit boundary

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions remain open, so none was planted. No making task arose.
- The Map membership check found **697 room files and 697 entries**, with no missing rooms, stale targets or duplicate entries. The existing room's one-line summary and the gate's dated checked note were refreshed; no room was created.
- Network retrievals used HTTPS with certificate verification, curl's configuration-file bypass, HTTPS-only redirects, at most three redirects, a 10-second connection timeout, a 35-second total limit, and a 300,000-byte response limit. Raw responses were not saved; this receipt records the requests and readings.
- No watched Git endpoint was requested, no timing sample added, no database opened, no source command executed, and no machinery changed.
- Visit edits are this receipt, the existing word and room, the one open question's research note, the gate, and exactly one appended chronicle line. Courtyard and quests remain unchanged.
