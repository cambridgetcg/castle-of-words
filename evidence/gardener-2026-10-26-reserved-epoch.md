# A reserved archive number is not a lost store — 2026-10-26

A historical explanation of a missing numbered store narrows what the castle's old roster check can claim; it does not reveal the archive's update schedule.

The visit began at **13:03 CET**. The courtyard was empty. **Question 740** was the oldest eligible question after skipping commissions and decisions reserved for yu; it was the only question researched. Questions 744 and 766 were not counted as researched.

## Sources actually read

All five HTTP requests below returned **200 with curl exit 0** on **2026-10-26**. Search listings supplied leads, not conclusions; their extracted text was read in full.

1. **Brave Search: `"yhetil.org" "maintenance"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22maintenance%22&source=web — returned an archive page whose mail subjects mention maintenance and the ownership question below. The archive listing was not fetched.
2. **Public-inbox meta search: `f:kyleam.com (schedule OR timer OR cron OR maintenance)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28schedule+OR+timer+OR+cron+OR+maintenance%29 — one result, the stale-search reply below. The first local extraction script had an unmatched parenthesis and stopped before making any request; the corrected script made the successful request recorded here.
3. Cayetano Santos, **ownership of the yhetil.org service ?**, dated **12 February 2025**, https://www.mail-archive.com/help-guix@gnu.org/msg19268.html — full extracted message read. It asks about ownership and maintenance rather than documenting an update timetable. Its thread links supplied the later reply below. The castle had already recorded the February maintainer response; it was not fetched again.
4. Kyle Meyer, **Re: ownership of the yhetil.org service ?**, dated **10 March 2025, 18:03:17 −0700**, https://www.mail-archive.com/help-guix@gnu.org/msg19471.html — full extracted message read. Meyer says guix-patches has no `0.git`, having started at `1.git` to leave room for earlier messages he lacked. He notes that adding those messages to the existing epoch was also possible and expresses uncertainty about ever adding them. This is the new historical finding, not a present inventory check.
5. Kyle Meyer, **Re: [PATCH 0/2] extsearch: avoid stale Xapian results**, dated **28 December 2020**, https://public-inbox.org/meta/87mtxyrlnr.fsf@kyleam.com/raw — raw email parsed with Python's standard-library email parser and decoded body read in full. It confirms a reported improvement already recorded in [[what-the-gaps-can-say]] on October 22; it supplies no new update schedule and was not added there again.

## What changed in the understanding

The **26 September 2026 roster check**, retained in [[the-kind-that-crosses]], tried `0.git` for every listed archive and recorded 404 for guix-patches and meta. The newly read March 2025 account supplies a reason not to presume that guix-patches ever offered epoch zero at that earlier time. It does **not** independently explain the later 404, establish the current store inventory, or explain meta's reply.

[[what-the-gaps-can-say]], “A missing number can be a place left empty,” now keeps that boundary beside the old observation. [[mirror-fetch]] now distinguishes identifying the stores to copy from assuming a sequence beginning at zero. No new room or word file was needed; the relevant words already exist or are explained inline.

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the archive's actual update times and their relationship to delays remain unknown. **740 stays open.** All **16** questions remain open, so no question was planted; no making task arose.

## Scope and checks

- The Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate room targets. Its descriptions remain applicable; no Map edit was needed.
- Requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS redirects, limited redirects to three, and used a ten-second connection timeout and a 35-second total timeout. Size caps were 900,000 bytes for Brave, 800,000 for the archive search, and 700,000 for each message. No automatic retries were configured.
- Responses were processed in memory. HTML was text-extracted with Python's standard-library parser. This is a reading receipt, not a saved raw-response snapshot. No source command, signature attachment or quoted external message was executed or fetched.
- Deliberate writes are this receipt, one addition to the existing room, one addition to the existing word, and exactly one appended chronicle line. Courtyard, questions, quests and gate remain unchanged; earlier working-tree changes are preserved. No watched Git endpoint, database, scheduler, service, configuration or `garden/` file was changed or operated on.

Links: [[what-the-gaps-can-say]] · [[mirror-fetch]] · [[discovery-index]] · [[manifest]] · [[the-kind-that-crosses]] · [[questions]]
