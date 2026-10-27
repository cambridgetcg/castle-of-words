# A catch-up scan can give way to new mail — 2026-10-27

A historical watcher explanation separates the order of processing from the age of the mail; it does not reveal the watched archive's update clock.

The visit began at **01:27 CET**. The courtyard was empty. Question **740**, planted 2026-10-06, was the oldest eligible open question after skipping commissioned work and decisions reserved for yu. It was the only question researched; 744 and 766 were not counted as researched.

## Searches and sources actually read

All reading below took place on **2026-10-27**. Each request returned **HTTP 200, curl exit 0**. HTML was converted to text in memory; the displayed extractions were complete, not raw-response snapshots. Search matches are leads, not evidence of deployment.

1. **Brave Search: `"yhetil.org" ("slow" OR "timeout" OR "delay")`**, https://search.brave.com/search?q=%22yhetil.org%22+%28%22slow%22+OR+%22timeout%22+OR+%22delay%22%29&source=web — the returned first page was largely generic timeout material, not a verified report of this host's delays. No linked result was fetched.
2. **Brave Search: `"yhetil.org" ("postfix" OR "maildir" OR "public-inbox-watch")`**, https://search.brave.com/search?q=%22yhetil.org%22+%28%22postfix%22+OR+%22maildir%22+OR+%22public-inbox-watch%22%29&source=web — the first page supplied the historical Maildir thread read below, alongside generic mail configuration and client-side material. No configuration advice was executed.
3. **Public-inbox meta search: `f:kyleam.com (maildir OR postfix OR poll)`**, https://public-inbox.org/meta/?q=f%3Akyleam.com+%28maildir+OR+postfix+OR+poll%29 — the complete listing contained **30 results**. Only the signalfd reply in item 5 was followed from this listing during this visit.
4. **Usage of public-inbox with maildirs**, the complete displayed two-message thread, https://public-inbox.org/meta/20190321033503.uukzpw7o7viobfgo@dcvr/T/:
   - Ralf Ramsauer, **Usage of public-inbox with maildirs**, **20 March 2019**, https://public-inbox.org/meta/745d6a8e-7e7c-8c61-336b-105cf9570ab7@oth-regensburg.de/ — reports periodic IMAP collection into a shared mailbox and asks about a slow initial import. This is his setup, not a description of yhetil.org.
   - Eric Wong, **Re: Usage of public-inbox with maildirs**, **21 March 2019**, https://public-inbox.org/meta/20190321033503.uukzpw7o7viobfgo@dcvr/ — confirms startup rechecking of mail files and says the scan has lower priority than freshly arrived mail when `Linux::Inotify2` is installed for `Filesys::Notify::Simple` to use. This is a dated explanation with a stated dependency, not a promise about every later version. The reply's cleanup and import commands were read but not run.
5. Kyle Meyer, **Re: [PATCH 11/34] watch: use signalfd for Maildir watching**, **27 June 2020**, https://public-inbox.org/meta/87tuyw5nxy.fsf@kyleam.com/ — the full message page was read. Meyer proposes a wording correction to quoted patch prose; he does not report deploying the patch or describe his archive's update schedule. The page's linked patch series was not fetched or executed.

## What grew, and what did not

The useful new distinction is **processing priority during catch-up versus the arrival order of messages**. The 2019 reply describes one way new mail can take precedence over a scan of retained mail. It supplies neither a numerical delay bound nor a timetable for the watched host. The dated finding now lives in [[mail-ingestion]] and [[what-the-gaps-can-say]], “A catch-up scan need not go first.”

**Filed 0, researched 1, answered 0, planted 0.** uncertain: yhetil's input path during the saved checks, its version and prioritization rules, its actual reference-update times, and any relationship to delayed Git replies. **740 stays open.** These searches do not establish that no operational record exists elsewhere.

There are **16 open questions**, so none was planted. No making task arose; the eight open quests were left unchanged.

## Bounds and verification

- The Map audit found **697 room files and 697 unique room entries**, with no missing, stale or duplicate room targets. The entries already met the requirement; the gate's checked note was refreshed.
- Requests disabled curl configuration-file loading, kept certificate verification, restricted URLs and redirects to HTTPS, allowed at most three redirects, and used ten-second connection and 35-second total timeouts. Search and thread responses were capped at 900,000 bytes; the final message at 700,000 bytes. No automatic retries were configured.
- No watched Git endpoint, database, mail import, service, scheduler or configuration was operated on. Nothing in `garden/` was changed. No new service-timing sample was collected.
- Deliberate changes are this receipt, a dated addition to one room and one existing word, the gate's checked note, and exactly one appended chronicle line. Courtyard, questions and quests remain unchanged; the pre-existing `.heartbeat` change is not part of this visit's work.

Links: [[mail-ingestion]] · [[queue]] · [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[questions]]
