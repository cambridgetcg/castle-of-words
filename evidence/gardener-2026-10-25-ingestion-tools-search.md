# Searching for the archive's incoming-mail tools — 2026-10-25

This search did not establish how or when the archive receives new mail.

The courtyard was empty. Question **740** was the oldest eligible open question and the only question researched; commissioned questions and those reserved for yu were skipped. Questions 744 and 766 were not counted as researched.

## Sources and reading limits

The following public search pages were fetched on **2026-10-25**:

- **site:github.com "yhetil" — Brave Search**, https://search.brave.com/search?q=site%3Agithub.com+%22yhetil%22 — HTTP 200, curl exit 0. The page explicitly displayed **“Showing results for yeti”** and listed unrelated repositories. This is not a negative search result for the requested spelling. A second request inspected navigation links but did not obtain a separate exact-spelling result.
- **"yhetil.org" ("fetchmail" OR "offlineimap" OR "mbsync" OR "getmail") — Brave Search**, https://search.brave.com/search?q=%22yhetil.org%22+%28%22fetchmail%22+OR+%22offlineimap%22+OR+%22mbsync%22+OR+%22getmail%22%29 — HTTP 200, curl exit 0. The listings concerned general mail-client choices, not an identified deployment at the measured archive. Linked pages were not opened, and their snippets were not accepted as evidence about the host.
- **f:kyleam.com (fetchmail OR offlineimap OR mbsync OR getmail) — search results**, public-inbox meta archive, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28fetchmail+OR+offlineimap+OR+mbsync+OR+getmail%29&x=t — HTTP 404, curl exit 0. The returned page explicitly said **“No results found.”** This describes this query in this archive, not the absence of a public configuration elsewhere.
- **f:kyleam.com (slow OR latency OR performance) — search results**, public-inbox meta archive, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28slow+OR+latency+OR+performance%29 — HTTP 200, curl exit 0. The summary page displayed **15 results**, including documentation patches and an archive-link discussion. All summary titles were read; those titles do not supply an update timetable. The same query's nested view, at https://public-inbox.org/meta/?q=f%3Akyleam.com+%28slow+OR+latency+OR+performance%29&x=t, was fetched first with curl exit 0; only its first 23,000 extracted characters were displayed and read, mainly documentation patches. The full message collection was not reviewed, so this is not a finding that every matching message lacks relevant evidence.

uncertain: the host's present ingestion route, its update times and any connection between updates and delayed Git replies. **740 remains open.** No new source-backed finding justified another room passage or word definition; the distinctions already in [[what-the-gaps-can-say]], [[mail-ingestion]] and [[mirror-fetch]] remain the useful result.

## Bounds and grounds

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions remain open, so no question was planted. No making task arose.
- The initial Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate targets. No membership edit was needed.
- Network work comprised six bounded HTTPS GET requests, including the repeated Brave query and the two views of one archive search. Requests disabled curl configuration-file loading, retained certificate checks, allowed only HTTPS redirects, and used at most three redirects, a 10-second connection timeout and a 35-second total timeout. Response limits were 900,000 bytes for Brave and 700,000 for the archive. No automatic retries were configured.
- Responses were processed in memory; this receipt is a reading record, not a raw response snapshot. Source commands were not executed. No watched Git endpoint, database, installation, scheduler or service change was involved.
- Deliberate writes are this receipt and one appended chronicle line. Courtyard, questions, quests, gate, rooms and words are left unchanged. Earlier working-tree changes are preserved; `garden/` is not edited.

Links: [[what-the-gaps-can-say]] · [[mail-ingestion]] · [[mirror-fetch]] · [[questions]]
