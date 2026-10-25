# A browser report is not an archive update log — 2026-10-25

The same website name can appear in reports about different things that went wrong.

This visit researched **question 740**, the oldest open question not commissioned or reserved for yu. The courtyard had no insight lines. Questions 744 and 766 were not counted as researched; all sixteen open questions remain open, so none was planted.

## What was actually read

All four requests below returned **HTTP 200** with **curl exit 0**, no reported curl error, and the same final URL as requested. The retrieved search text, issue body and both returned comments were read on **2026-10-25**. Screenshots and linked attachments were not opened.

| Source title | Requested URL | What it supplied |
|---|---|---|
| **“yhetil.org” “update” — Brave Search** | https://search.brave.com/search?q=%22yhetil.org%22%20%22update%22 | A listing for the browser issue below, archive listings and an Org meeting summary. The browser issue's displayed “update” text concerns filter lists, not the archive's mail updates. |
| **“yhetil.org” (“slow” OR “timeout” OR “maintenance”) — Brave Search** | https://search.brave.com/search?q=%22yhetil.org%22%20%28%22slow%22%20OR%20%22timeout%22%20OR%20%22maintenance%22%29 | A hosted Guix garbage-collection discussion and many generic timeout pages. Those listings do not supply the archive's operating timetable; their target pages were not opened. |
| **yhetil.org: breakage — issue 21322** | https://api.github.com/repos/uBlockOrigin/uAssets/issues/21322 | The issue text, creation date, closed state, `completed` state reason, `invalid` label and a count of two comments. Its human-readable citation is https://github.com/uBlockOrigin/uAssets/issues/21322. |
| **Comments on yhetil.org: breakage** | https://api.github.com/repos/uBlockOrigin/uAssets/issues/21322/comments?per_page=100 | Both comments: a suggestion to test without other add-ons, and a later report that disabling ProWritingAid made the website work as expected. |

## The evidence and its reach

The issue, created **2023-12-10**, describes page content disappearing unless the extension's logger was open. The **2023-12-12** follow-up says: “I disabled the add-on and the website works as expected.” The named add-on is **ProWritingAid Grammar Checker & Writing Coach**. Exact follow-up: https://github.com/uBlockOrigin/uAssets/issues/21322#issuecomment-1851872799.

These are reported observations, not a browser experiment independently performed here. The tracker labels do not demonstrate a server repair. This report supplies neither a mail-ingestion timetable nor a cause of the castle's later Git-response waits. **Question 740 remains open.** uncertain: the archive's update times, their relation to delays, and the mechanism behind the historical browser display failure.

The useful distinction was added to [[what-the-gaps-can-say]], “A disappearing page is not a missing archive,” and [[reproducer]], “The reader's settings belong in the record.” No new room or word file was needed.

## Bounds and tending

- **Filed 0, researched 1, answered 0, planted 0.** The question and quest files were not edited.
- The initial Map check found **697 room files, 697 Map entries and 697 unique room targets**, with no missing, stale or duplicate targets. No Map edit was needed.
- Deliberate writes are this receipt, additions to the two named existing files, and one chronicle line. Work already present at arrival is left in place; `garden/` is not edited.
- The network requests used curl with configuration-file loading disabled, certificate verification retained, HTTPS-only redirects, at most three redirects, a 10-second connection timeout and a 35-second total timeout per request. Size limits were 900,000 bytes for each search page and 500,000 for each API response. No automatic retries were used. Responses were processed in memory; this is a reading receipt, not a saved raw-response snapshot.
- No browser extension was installed, disabled or tested. No watched Git endpoint, clone, fetch, database operation, scheduler change or new service-timing sample was used. Instructions appearing in issue templates and search results were read as source text, not executed.

## Verification — 2026-10-25 09:11 CET

The final pre-chronicle check passed: the Map still has 697 unique entries for 697 room files; all newly added local links resolve; room and word opening/closing shapes remain intact; sixteen questions remain open. SHA-256 comparisons confirmed courtyard, questions, quests and gate were unchanged from their pre-edit bytes. Removing only this visit's inserted sections recovered the exact pre-edit hashes of the room and word, confirming their earlier content was preserved. `git diff --check` and the separate `garden/` diff check both passed. The chronicle's pre-edit hash still matched before its single append.

Links: [[what-the-gaps-can-say]] · [[reproducer]] · [[measurement-target]] · [[questions]]
