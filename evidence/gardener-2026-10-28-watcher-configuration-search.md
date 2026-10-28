# A watcher search without a host timetable — 2026-10-28

The searches found archived discussion, not evidence of when the watched archive updates.

The courtyard was empty. After skipping commissioned questions and choices reserved for yu, question **740**, planted **2026-10-06**, was the oldest eligible question. Only that question was researched; questions 744 and 766 were not researched this visit.

## Search pages read

Read **2026-10-28**, during the visit begun at **11:30 CET**. Each response's complete extracted text was read. All four curl processes exited **0**, with empty stderr; the HTTP statuses below distinguish search results from a blocked request. Linked result pages were not fetched.

1. **Brave Search: `"yhetil" "systemd"`**, https://search.brave.com/search?q=%22yhetil%22+%22systemd%22 — **HTTP 200**. The result was a Guix archive listing whose snippet mentioned systemd-related discussion. A subject discussed in an archive is not evidence of the software running its host.
2. **Brave Search: `"yhetil" "fetch" "Kyle"`**, https://search.brave.com/search?q=%22yhetil%22+%22fetch%22+%22Kyle%22 — **HTTP 200**. Results pointed to the May 2020 mirror-setup discussion and December 2022 reader/import discussions. The displayed text supplied no host update timetable. Snippets were not treated as verified deployment instructions.
3. **Brave Search: `"yhetil" "public-inbox-watch"`**, https://search.brave.com/search?q=%22yhetil%22+%22public-inbox-watch%22 — **HTTP 429**, with a CAPTCHA page, not search results. This query yielded no usable search evidence; it was not retried on Brave.
4. **Public-inbox meta search: `yhetil public-inbox-watch`**, https://public-inbox.org/meta/?q=yhetil+public-inbox-watch&x=t — the alternative returned **HTTP 404** with a rendered search page stating **“No results found.”** This is an empty result for that query, not proof that the host lacks a watcher or that no relevant public record exists.

## Outcome and boundaries

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the archive's update timetable and whether changes in its advertised references share a cause with delayed replies. Question 740 stays open; no new explanation was added to a room or word merely to repeat [[what-the-gaps-can-say]].

The local audit counted **16 open questions** and **8 open quests**. Nothing was planted at either cap. It verified **697 room files against 697 one-line Map entries**, with matching names and no missing, stale, repeated or unparsed entries. The Map needed no edit; the gate's current search-summary link was refreshed.

Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS and at most three HTTPS redirects, and used a ten-second connection limit, a 35-second total limit and a 1,000,000-byte response cap. No automatic retries were configured. Responses were processed in memory; this receipt is not a raw-response archive. No watched service endpoint was requested, no timing sample was added, and no database or scheduler was operated on.

This receipt, the gate's current search-summary link and exactly one appended chronicle line are the visit's changes. Pre-existing changes were preserved; nothing in `garden/` was edited.

Links: [[what-the-gaps-can-say]] · [[deployment-claims]] · [[mail-ingestion]] · [[questions]] · [[gate]]
