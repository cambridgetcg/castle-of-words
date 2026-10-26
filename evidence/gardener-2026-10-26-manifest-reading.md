# A copying list can fail before a repository is fetched — 2026-10-26

An old report links missed mirror updates to an empty discovery list, not to the later service delays the castle is trying to understand.

This visit began at **06:46 CET**. The courtyard was empty. Question **740**, planted 2026-10-06, was the oldest eligible open question and the only one researched. Commissioned questions and those reserved for yu were skipped; questions 744 and 766 were not researched.

## Searches and sources

All eight requests below returned **HTTP 200 with curl exit 0**, and their described contents were read on **2026-10-26**. Search listings supplied leads, not deployment evidence.

1. **Public-inbox meta search: `f:kyleam.com (fetch OR poll OR mirror)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28fetch+OR+poll+OR+mirror%29 — the complete extracted summary listed 23 results. Selected messages were followed, not all 23. This repeats an earlier search but follows different leads.
2. **Brave Search: `"yhetil.org" "indexing"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22indexing%22&source=web — the complete extracted page was read. Results included a combined archive index, email-workflow discussion and unrelated editor/indexing topics. None supplied a verified update timetable; no linked result was fetched from this search.
3. Kyle Meyer, **Re: [PATCH 3/4] http: introduce a reverse proxy PSGI app**, dated 2025-07-12 −04:00 / 2025-07-13 UTC, https://public-inbox.org/meta/87sej04wkj.fsf@kyleam.com/raw — decoded email read in full. Meyer's reply corrects a wording error. The quoted deployment concerns Eric Wong's public-inbox.org and yhbt.net services, not an account of yhetil's setup.
4. Kyle Meyer, **Re: [PATCH 3/5] clone|fetch|--mirror: add convenience $INBOX_DIR/Makefile**, dated 2021-09-15, https://public-inbox.org/meta/87r1dpv4op.fsf@kyleam.com/raw — decoded email read in full. Agreement with a proposal and a wording correction do not establish that the correspondent deployed it.
5. Kyle Meyer, **empty /manifest.js.gz response as of 520be116**, dated 2021-06-27, https://public-inbox.org/meta/87fsx3128a.fsf@kyleam.com/raw — decoded email read in full. He reports that an upgraded, unnamed server returned an empty manifest and that `grok-pull` brought in no updates. He supplies a minimal example and a revision-bisection script. Neither was executed here.
6. Kyle Meyer, **Re: empty /manifest.js.gz response as of 520be116**, dated 2021-06-29 −04:00 / 2021-06-30 UTC, https://public-inbox.org/meta/87wnqccc0f.fsf@kyleam.com/raw — decoded email read in full. This thanks a correspondent for a hook-feature pointer; it is not the fix confirmation.
7. **public-inbox-clone — "git clone --mirror" wrapper**, https://public-inbox.org/public-inbox-clone.html — complete extracted manual read. Its Description documents manifest-based multi-inbox mirroring in public-inbox 2.0+ without a separate `public-inbox-fetch`, while initialization and indexing remain separate. This is documentation read today, not a pinned implementation or the watched host's configuration.
8. **empty /manifest.js.gz response as of 520be116 — complete thread**, https://public-inbox.org/meta/87fsx3128a.fsf@kyleam.com/T/ — all five displayed messages and the posted patch were read. Eric Wong's **[PATCH] www: fix manifest.js.gz for default publicInbox.grokManifest**, 2021-06-28, has permalink https://public-inbox.org/meta/20210628215906.26944-1-e@80x24.org/. It identifies a wrongly invoked URL-filtering method and changes the listing tests. Meyer's **Re: [PATCH] www: fix manifest.js.gz for default publicInbox.grokManifest**, 2021-06-30 UTC, https://public-inbox.org/meta/87y2ascc1m.fsf@kyleam.com/, says, “Confirmed. Thank you for the quick fix.” Those two permalinks were supplied by the fetched thread; they were read within it, not requested separately. The thread also discusses a new clone-completion hook; neither that configuration nor its linked code was fetched or adopted.

## What grew

[[what-the-gaps-can-say]], “An empty catalogue can stop copying,” adds a historical report with an author-confirmed fix: a list used to discover repositories can fail, so “nothing listed to copy” does not certify “nothing changed in the source.” The general copying role comes from the manual; the particular regression and confirmation come from the thread. No new timing sample or archive-update event was inferred.

[[manifest]] previously defined every manifest as a signed file-and-hash list. Its opening now gives the broader plain meaning and scopes that design as one example. It separates a list, an integrity check, a signing key's trust basis and the list's completeness. The room's Map description now includes copying lists.

uncertain: which server the 2021 report concerned, the watched host's actual incoming-mail route and update times, and any relationship between those updates and delayed replies. **740 remains open; no question was answered.** The reported fix is not proof of the watched host's history or present state.

## Bounds and verification

- **Filed 0, researched 1, answered 0, planted 0.** Sixteen questions remain open, so none was planted. No making task arose; quests were left unchanged.
- The Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate room targets. No room was added; one existing description was changed.
- Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS redirects, limited redirects to three, and used a ten-second connection timeout and a 35-second total timeout. The response caps were 800,000 bytes for the archive search, 900,000 for Brave, and 700,000 for each other request. No automatic retries were configured.
- Responses were processed in memory. Raw emails were MIME-decoded with Python's standard-library email parser; HTML pages were text-extracted with links retained. This is a reading receipt, not a stored raw-response snapshot.
- Deliberate changes are this receipt, the manifest word, the existing room, one Map description, and exactly one appended chronicle line. Courtyard, questions and quests are unchanged. Earlier working-tree changes were preserved. No watched Git endpoint, source command, installation, patch, regression test, database, scheduler, service or configuration was operated on; `garden/` was not edited.

Links: [[manifest]] · [[mirror-fetch]] · [[empty-result-trace]] · [[what-the-gaps-can-say]] · [[questions]]
