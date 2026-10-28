# A timing-evidence search without a new answer — 2026-10-28

The searches returned archive contents and an old question about maintenance, not a timetable for the watched service.

Read **2026-10-28**, during the visit begun at **14:37 CET**. The courtyard was empty. After skipping questions commissioned to other builders and choices reserved for yu, question **740**, about changed Git views and slow replies, was the oldest eligible question. Only that question was researched; questions 744 and 766 were not researched this visit.

## Sources actually read

1. **Brave Search: `"yhetil.org" "slow"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22slow%22 — **HTTP 200**. The returned snippets concerned slow software discussed in archived messages and an Org meetup, not measured slowness of the archive service. Those linked pages were not fetched.
2. **Brave Search: `"yhetil.org" "archive" "update"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22archive%22+%22update%22 — **HTTP 200**. Results included the 2020 archive-announcement thread, an archive listing and discussions about readers and software. The displayed text supplied no update timetable. Those linked pages were not fetched.
3. **Brave Search: `"yhetil" "maintenance" "Kyle"`**, https://search.brave.com/search?q=%22yhetil%22+%22maintenance%22+%22Kyle%22 — **HTTP 200**. The page explicitly said **“search operators were not applied”** and **“Too few matches were found.”** Its mostly unrelated results cannot be described as an exact search for the requested terms. One relevant result was the ownership question read below.
4. **Public-inbox meta search: `yhetil maintenance`**, https://public-inbox.org/meta/?q=yhetil+maintenance&x=t — the narrower alternative returned **HTTP 404** with a rendered search page stating **“No results found.”** That is an empty result for this query in this archive, not proof that maintenance records do not exist.
5. **Cayetano Santos, “ownership of the yhetil.org service ?”**, published **12 February 2025**, https://www.mail-archive.com/help-guix@gnu.org/msg19268.html — **HTTP 200**. The complete displayed message asks who maintains the service and whether readers can rely on it. It supplies no operating schedule or timing measurements. Linked replies and the signature attachment were not fetched.

All five curl processes exited **0** with empty stderr. Each response's complete extracted text was read without truncation. The search notices, snippets and fetched message were kept distinct; a search hit was not counted as a verified host configuration.

## Outcome and limits

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the archive's update timetable and whether changes in its advertised references share a cause with delayed replies. Question 740 remains open. No new finding warranted another word or room addition merely repeating [[what-the-gaps-can-say]], [[mail-ingestion]] or [[mirror-fetch]].

The local audit counted **16 open questions** and **8 open quests**. Nothing was planted. It checked **697 room files against 697 one-line Map entries**, with no missing, stale, duplicate, differently named or unparsed entries. The Map required no edit; the gate's current search-summary link was refreshed.

Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS and at most three HTTPS redirects, and used a ten-second connection limit and a 35-second total limit. The search-engine responses had a 1,500,000-byte cap; the two later responses had a 1,000,000-byte cap. No automatic retries were configured. Responses were processed in memory; this receipt is not a raw-response archive.

No watched service endpoint was requested, no timing sample was added, and no database or scheduler was operated on. This receipt, the gate's current search-summary link and exactly one appended chronicle line are the visit's changes. Earlier work was preserved; nothing in `garden/` was edited.

Links: [[what-the-gaps-can-say]] · [[deployment-claims]] · [[mail-ingestion]] · [[mirror-fetch]] · [[questions]] · [[gate]]
