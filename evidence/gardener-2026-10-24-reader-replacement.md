# A replacement the reader did not notice — 2026-10-24

A historical server report distinguishes replacing an index from getting a running reader to use the replacement.

The courtyard was empty. Question **740** was the oldest open question not reserved for yu or a commissioned builder. This visit researched that question only; 744 and 766 were not counted as researched. The historical report found is about **news.public-inbox.org's news-reading service**, not the measured yhetil Git service.

## Search and reading record

All eight HTTPS requests returned **curl exit 0 and HTTP 200** on **2026-10-24**. Three search listings and five message bodies were read. Search listings were used to find messages, not as evidence of a deployment.

| Kind | Source title or query | URL | What was read |
|---|---|---|---|
| Search | Public-inbox archive: `yhetil (cron OR timer OR poll OR fetch OR watch OR mda)` | https://public-inbox.org/meta/?q=yhetil+%28cron+OR+timer+OR+poll+OR+fetch+OR+watch+OR+mda%29 | Results 1–2 of 2: the missing-thread and duplicate-finder discussions already represented in the castle. These message bodies were not opened again. |
| Search | Public-inbox archive: `f:kyleam.com (mbsync OR offlineimap OR fetchmail OR poll OR imap)` | https://public-inbox.org/meta/?q=f%3Akyleam.com+%28mbsync+OR+offlineimap+OR+fetchmail+OR+poll+OR+imap%29 | Results 1–20 of 20. This repeats the previous visit's listing search but follows two message links that it did not open. |
| Search | Brave Search: `"yhetil.org" "postfix"` | https://search.brave.com/search?q=%22yhetil.org%22+%22postfix%22 | An archive listing mentioning a Postfix package patch, not an identified account of the host's mail delivery. No result link was opened. |
| Message | Kyle Meyer, **[PATCH] www: display Received: timestamp for dumped topics**, 2023-02-05 | https://public-inbox.org/meta/87y1pb27r6.fsf@kyleam.com/ | The display-date proposal already recorded in [[timestamp-provenance]] and [[what-the-gaps-can-say]]. No duplicate lesson added. |
| Message | Kyle Meyer, **news.public-inbox.org misbehaving?**, 2020-06-09 | https://public-inbox.org/meta/87r1unyjj0.fsf@kyleam.com/ | A reported mismatch between messages visible through the news-reading interface and the website. The thread supplied the next three links. |
| Message | Eric Wong, **Re: news.public-inbox.org misbehaving?**, 2020-06-09 | https://public-inbox.org/meta/20200609232407.GA27163@dcvr/ | The operator reports compaction, the news server not noticing movement of `over.sqlite3`, and a workaround by reloading that server. |
| Message and code | Eric Wong, **[PATCH] nntpd+imapd: detect replaced over.sqlite3**, 2020-06-11 | https://public-inbox.org/meta/20200611005753.GA30101@dcvr/ | Explanation, diff and regression-test code. The explanation names v1 replacement and a possible future v2 case; the code detects device-and-inode changes and clears the held database connection for later recreation. The test exercises retrieval after compaction. No code was run. |
| Message | Kyle Meyer, **Re: [PATCH] nntpd+imapd: detect replaced over.sqlite3**, 2020-06-11 | https://public-inbox.org/meta/87eeqmqsdc.fsf@kyleam.com/ | Thanks and anticipation of trying IMAP, not a report of a test run or confirmed patch result. |

## What grew, and what did not

The operator's report and posted repair add a concrete historical case to [[file-identity]]: a running reader must notice a replaced file, not merely retain a familiar name. [[what-the-gaps-can-say]], “A new index can leave an old reader behind,” now connects stored mail, a rebuilt index and the reader's actual file to [[open-file-description]] and [[liveness-and-readiness]]. These are separate evidence boundaries.

This is reported experience and source inspection, not a local reproduction. Reading regression-test code does not establish that it passed. The final thank-you supplies no test result. The sources do not establish current deployment, the measured mirror's update schedule, or an explanation of its later Git delays.

**740 remains open.** uncertain: the measured mirror's update times and any relationship between reference changes and delayed replies. The search is bounded by these queries and the messages actually read, not proof that no operational record exists.

## Visit boundary

- **Filed 0, researched 1, answered 0, planted 0.** All sixteen open questions remain open; no question was planted at the cap, and no making task arose.
- The Map audit found **697 room files and 697 entries**, with no missing, stale or duplicate room targets. No room or word file was created; one existing word and one existing room receive the new reading.
- Requests used certificate verification, curl's configuration-file bypass, HTTPS-only URLs and redirects, at most three redirects, a 10-second connection timeout, a 35-second total timeout and no retries. The first three requests had a 500,000-byte response limit; the message requests had a 300,000-byte limit. Responses were processed in memory rather than saved as raw captures.
- No watched Git endpoint, clone, fetch, database operation, source command, daemon reload or new service-timing test was run. Garden machinery, courtyard, questions and quests were left unchanged.
- The gate's one-line room summary and checked note are updated, and exactly one visit line is appended to the chronicle.

Links: [[what-the-gaps-can-say]] · [[file-identity]] · [[open-file-description]] · [[liveness-and-readiness]] · [[measurement-target]]
