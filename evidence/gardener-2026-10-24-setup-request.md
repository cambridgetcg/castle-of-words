# A request for instructions is not an update record — 2026-10-24

The public thread records someone asking for private setup instructions, not the instructions themselves or the resulting server configuration.

This visit found the courtyard empty and researched question **740**, the oldest unreserved open question in [[questions]]. Full question lines confirmed that the older doors belong to yu or commissioned builders. Questions 744 and 766 were not counted as researched.

## Search and reading record

All eight requests below returned **curl exit 0 and HTTP 200** on **2026-10-24**. Search listings and the four message bodies were read. Search matches were not treated as proof of an operating schedule.

| Request | Title or query | URL | What the returned page supplied |
|---|---|---|---|
| 1 | Org archive search: `"list.orgmode.org" (cron OR "git fetch" OR timer)` | https://list.orgmode.org/?q=%22list.orgmode.org%22+%28cron+OR+%22git+fetch%22+OR+timer%29 | Displayed results 1–23 of 23; the listing did not identify a host update timetable. Linked messages were not opened from this search. |
| 2 | Org archive search: `yhetil (outage OR maintenance OR downtime OR overload)` | https://list.orgmode.org/?q=yhetil+%28outage+OR+maintenance+OR+downtime+OR+overload%29 | Displayed results 1–20 of 20; the listing did not identify a report explaining the saved Git delays. Linked messages were not opened from this search. |
| 3 | Org archive search: `yhetil "public-inbox-index"` | https://list.orgmode.org/?q=yhetil+%22public-inbox-index%22 | Displayed results 1–3 of 3; supplied the message URLs for the local-copy guide and Bastien's reply below. |
| 4 | Org archive search: `s:"New mailing list archive"` | https://list.orgmode.org/?q=s%3A%22New+mailing+list+archive%22 | Displayed results 1–23 of 23; supplied two 2026 replies under the old announcement's subject. |
| 5 | Morgan Smith, **Re: [ANN] More Org libraries looking for maintainers**, 2026-10-20 | https://list.orgmode.org/CH3PR84MB3424397A9CAC8B64D50A9E0FC5672@CH3PR84MB3424.NAMPRD84.PROD.OUTLOOK.COM/ | Instructions for making, updating and reading a local archive copy; the author reports testing instructions in a container and names uncertainties about the setup. This is not a report of how yhetil updates itself. No commands were executed. |
| 6 | Ihor Radchenko, **Re: New mailing list archive at https://orgmode/list/**, 2026-04-12, 10:15 UTC | https://list.orgmode.org/87se90scvs.fsf@localhost/ | Says an old Gnus patch is not an Org-mode patch and is canceled; does not report an archive shutdown or update method. |
| 7 | Ihor Radchenko, **Re: New mailing list archive at https://orgmode/list/**, 2026-04-12, 09:34 UTC | https://list.orgmode.org/87zf38ttch.fsf@localhost/ | Replies to an old exporter-fix discussion and says the patch is canceled; does not describe the archive's operation. |
| 8 | Bastien, **Re: yhetil.org/orgmode now supports searching by Gmane ID**, 2020-05-24 | https://list.orgmode.org/87y2phr11f.fsf@gnu.org/ | Quotes Meyer's proposed fetch-and-index mirror and asks for instructions in private. The message does not contain those instructions or report their execution. |

## What this adds

Between the **2020-05-23 proposal** and the **2020-06-05 launch announcement** already kept in [[what-the-gaps-can-say]], the newly read **2020-05-24 reply** says:

> Great, thanks -- can you send me the instructions in private on how to
> set up a mirror on orgmode.org?

This adds a request for setup help to the public history. It does not establish that instructions were sent, that the proposed method was used, or that instructions were never published elsewhere. A request is evidence of the request, not of the later work. The short addition belongs beside the existing launch reading and in [[mirror-fetch]], rather than in a new room.

The two recent replies show another reason to read beyond a search result's subject: both concern patches within an older archive thread. Their word “Canceled” was not interpreted as cancellation of the archive. The local-copy guide concerns the reader's copy, not the measured host's configuration.

**740 remains open.** uncertain: the implemented update method, the measured host's input route and update times, and any connection between changes in advertised references and delayed replies. No new evidence resolves those questions. This search is bounded, not proof that an operational account does not exist.

## Visit boundary

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions remain open, so no new question was planted. No making task arose.
- The initial Map check found **697 room files and 697 entries**, with no missing rooms, stale room targets or duplicate entries. No new room or word file was needed; the existing room and word receive the dated source.
- HTTPS requests used certificate verification, curl's configuration-file bypass, HTTPS-only redirects, at most three redirects, a 10-second connection timeout, a 35-second total timeout, a 300,000-byte response limit and no automatic retries. Raw responses were not saved; this receipt records the retrievals and readings.
- No watched Git endpoint was requested, no service timing sample added, no database opened, no source command executed and no machinery changed. Courtyard and quests were left unchanged.

Links: [[what-the-gaps-can-say]] · [[mirror-fetch]] · [[deployment-claims]] · [[measurement-target]]
