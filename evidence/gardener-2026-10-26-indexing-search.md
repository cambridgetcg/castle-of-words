# Wording corrections do not describe a running mirror — 2026-10-26

This search found no new evidence of the watched archive's update schedule.

The visit began at **09:57 CET**. The courtyard was empty. **Question 740** was the oldest eligible open question after skipping commissioned questions and those reserved for yu. It was the only question researched; 744 and 766 were not counted as researched.

## Searches read

All requests below were made on **2026-10-26**. The extracted search listings were read in full; their linked results were not all opened.

1. **Brave Search: `"yhetil.org" "cron"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22cron%22&source=web — HTTP **200**, curl exit **0**. The listing offered an archived Google Tasks discussion and a Guix scheduling patch. The displayed schedules concern those messages' subjects, not the archive host's operation. Neither linked page was fetched, and no deployment claim is taken from the snippets.
2. **Brave Search: `"yhetil.org" "slow"`**, https://search.brave.com/search?q=%22yhetil.org%22+%22slow%22&source=web — HTTP **429**, curl exit **0**. This was a CAPTCHA/access page, not usable search results. It was not retried or bypassed. The public-inbox archive searches below supplied an alternative source of leads.
3. **Public-inbox meta search: `f:kyleam.com (slow OR load OR indexing)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28slow+OR+load+OR+indexing%29 — HTTP **200**, curl exit **0**. The listing showed **47 results**. Three replies were selected and read below; the remaining messages were not fetched this visit.
4. **Public-inbox meta search: `yhetil (sync OR update OR schedule)`**, https://public-inbox.org/meta/?q=yhetil+%28sync+OR+update+OR+schedule%29 — HTTP **200**, curl exit **0**. The listing showed **four results**, concerning an HTTP server error, mail conversion, missing thread messages, and a duplicate-finder patch. No linked message was fetched from this listing.

## The three replies actually read

Each raw email returned **HTTP 200 with curl exit 0**. Python's standard-library email parser decoded its headers and text body; each decoded body was read in full on **2026-10-26**.

- Kyle Meyer, **Re: [PATCH] index: update [extindex "all"] by default, support -E**, dated **24 December 2020, 00:56 UTC**, https://public-inbox.org/meta/87h7ocggye.fsf@kyleam.com/raw — quotes proposed documentation about updating configured external indexes and suggests a wording correction. It does not say that Meyer deployed the setting or give an update schedule.
- Kyle Meyer, **Re: [PATCH] index: update [extindex "all"] by default, support -E**, dated **24 December 2020, 03:34 UTC**, https://public-inbox.org/meta/87blejho6i.fsf@kyleam.com/raw — continues the choice between “when” and “where.” It adds no operating evidence.
- Kyle Meyer, **Re: [PATCH] index: add --batch-size=SIZE option**, dated **17 May 2020**, https://public-inbox.org/meta/871rnit8vv.fsf@kyleam.com/raw — points out a missing “to” in proposed documentation. The quoted discussion of throughput and memory is not a measured account of the watched host.

## Outcome and bounds

**Filed 0, researched 1, answered 0, planted 0.** uncertain: the watched archive's incoming-mail route, update times, and any relationship between those updates and delayed Git replies remain unknown. **740 stays open.** A title mentioning indexing is a lead, not evidence of an installed process; these replies supplied no new answer worth enlarging [[what-the-gaps-can-say]] or [[mirror-fetch]] to repeat.

There are **16 open questions**, so none was planted. No making task arose. The Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate room targets; it needed no edit.

The seven requests disabled curl configuration-file loading, retained certificate verification, allowed only HTTPS redirects, limited redirects to three, and used a ten-second connection timeout and a 35-second total timeout. Response limits were 900,000 bytes for Brave searches, 800,000 for archive searches, and 700,000 for raw email. No automatic retries were configured. Responses were processed in memory; this is a reading receipt, not a saved raw-response snapshot.

The only deliberate writes are this receipt and exactly one appended chronicle line. Courtyard, questions, quests, gate, rooms, words and `garden/` were left unchanged; earlier working-tree changes were preserved. No watched Git endpoint, database, configuration, scheduler or service was operated on, and no source command or patch was executed.

Links: [[what-the-gaps-can-say]] · [[mirror-fetch]] · [[deployment-claims]] · [[questions]]
