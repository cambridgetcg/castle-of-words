# mail-ingestion

Mail ingestion is bringing arriving messages into an archive so they can be kept and found.

An archive can receive messages without copying another archive's Git history. The public-inbox manual describes `public-inbox-watch` as a long-running process that watches a mailbox or newsgroup and imports new messages into both Git repositories, which keep saved work, and indexes, which help readers find it. It also scans for messages missed while it was stopped. — **public-inbox-watch — mailbox watcher for public-inbox**, https://public-inbox.org/public-inbox-watch.html; read **2026-10-15**.

The same manual explicitly calls this a way to mirror an existing mailing list. Its `watch` setting can be repeated to combine several mailboxes in one inbox. Thus **mirroring a list** names the archive's role, while [[mirror-fetch]] names one particular way of copying saved work. The role alone does not identify the method, update schedule, or running configuration. — same source, Description and Configuration; distinction drawn by the gardener, **2026-10-15**.

## Reported routes, not a present timetable — 2026-10-20

An old message can be brought in from a saved file or processed again after a reader of incoming mail restarts. In an April 2020 report, Kyle Meyer described importing saved `mbox` mail files and linked an example in the Org archive at yhetil.org. — Kyle Meyer, **From-munge not being reversed on mbox import**, 2020-04-04, https://public-inbox.org/meta/87lfnb3kz8.fsf@kyleam.com/ — read **2026-10-20**.

In a separate October 2020 report about the **Notmuch** archive, Meyer said changing a footer-removal filter and restarting `-watch` with older mail still present produced duplicates. This is dated testimony about that inbox, not proof of the current Org ingestion route. The watcher manual separately documents a scan at startup. — Kyle Meyer, **Re: [PATCH] scripts/dupe-finder: restore $dbh variable**, 2020-10-16, https://public-inbox.org/meta/87y2k67ogi.fsf@kyleam.com/; **public-inbox-watch — mailbox watcher for public-inbox**, Description and Signals, https://public-inbox.org/public-inbox-watch.html — both read **2026-10-20**.

Keep a new arrival, another pass over old mail, and a changed Git view separate. Historical reports supply evidence for their own inbox and date; they do not turn a [[freshness-target]] into a known current schedule. — gardener's synthesis, **2026-10-20**.

uncertain: which input method the hosts used during the castle's 2026 checks. A changed [[reference-advertisement]] does not, by itself, identify a fetch, a message import, or the cause of a slow reply. [[what-the-gaps-can-say]] keeps the host's public description and dated operator reports separate from evidence about its current jobs.

## Arrival is not selection — 2026-10-26

Mail can reach a shared mailbox without belonging in every archive that watches it. The watcher manual says `watchheader` selects matching mail: repeated values accept **any** match in public-inbox **1.5 and later**, while **1.4 and earlier** used only the last value. A claim about which mail should enter therefore needs the rule and its version, not just the fact that a watcher exists. — **public-inbox-watch — mailbox watcher for public-inbox**, Configuration, https://public-inbox.org/public-inbox-watch.html; read **2026-10-26**; inference about evidence by the gardener.

[[what-the-gaps-can-say]] keeps the historical `To`-or-`Cc` proposal and its unrun test beside this documented rule. uncertain: whether the watched host used such a selector; none was inspected or changed.

## Catch-up need not go first — 2026-10-27

Newly arriving mail can be handled before a scan of older mail has finished. In a **21 March 2019** reply, Eric Wong said that the watcher's startup scan rechecks mail files, but runs at lower priority than fresh arrivals when `Linux::Inotify2` is installed for `Filesys::Notify::Simple` to use. The dependency is part of the claim: this is his explanation of the watcher then, not a guarantee for every release or deployment. — Eric Wong, **Re: Usage of public-inbox with maildirs**, https://public-inbox.org/meta/20190321033503.uukzpw7o7viobfgo@dcvr/; read **2026-10-27** in its complete displayed thread, https://public-inbox.org/meta/20190321033503.uukzpw7o7viobfgo@dcvr/T/.

Keep the age of a message separate from when work on it gets a turn. [[queue]] names why waiting work need not be processed first-come-first-served; [[what-the-gaps-can-say]] keeps this historical example separate from a present update timetable. uncertain: whether the watched archive used this mechanism during the saved checks. No watcher or import was run. — gardener's application, **2026-10-27**; [reading receipt](../evidence/gardener-2026-10-27-scan-priority.md).

## Name the destination — 2026-10-27

Importing a thread for one reader is not the same job as adding mail to the public archive. Simon Tournier's reply about using yhetil says he sometimes imports whole threads for offline reading with Emacs-Notmuch; it does not describe the hosted archive's own input process. — Simon Tournier, **Re: yhetil.org and guix email based workflow**, 11 February 2025, https://www.mail-archive.com/help-guix@gnu.org/msg19262.html; read **2026-10-27**.

Before borrowing timing evidence from an import report, name where the mail goes and whose process brings it there. [[what-the-gaps-can-say]] keeps this reader's account separate from the still-unknown host schedule. — gardener's synthesis, **2026-10-27**; no import was run.

Links: [[mirror-fetch]] · [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[measurement-target]] · [[deployment-claims]] · [[freshness-target]] · [[queue]]
