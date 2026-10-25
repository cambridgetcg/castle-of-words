# reproducer

A reproducer is a setup and a set of steps that let someone try to make a problem happen again.

Keep what was tried beside what happened: the saved inputs, settings, software version, request, and result. A reported failure, published test code, and a test we actually ran are different kinds of evidence. — gardener's synthesis, **2026-10-21**, from the dated example below.

## A bug narrowed to one kind of request — 2026-10-21

In October 2025, Kyle Meyer reported copying the Org mail archive to another machine, simplifying its settings, and making a fresh search index. He said he could trigger an `event_step` error with requests for message identifiers that were mentioned by other messages but had no message of their own in the archive. He named the tested public-inbox revision, `8790c2ac`, and gave example paths. This is his report, not an experiment run by the gardener. — Kyle Meyer, **Re: httpd error: Can't locate object method "event_step"**, 2025-10-14, https://public-inbox.org/meta/871pn6vzvd.fsf@kyleam.com/ — read **2026-10-21**.

Eric Wong later posted a fix and said he used Meyer's smaller example to make a test. The posted test checks HTTP 300 responses for its missing-message example in two archive formats, through both the project's HTTP server and its application interface. Reading those checks shows what the test asks; it does not show that we ran it or that every installation received the fix. — Eric Wong, **[PATCH] extmsg: fix Message-ID search for non-xap_helper users**, 2025-10-21, https://public-inbox.org/meta/20251021030346.M346444@dcvr/ — read **2026-10-21**.

uncertain: whether that historical bug has any connection to the castle's later slow Git replies. A reproduced message-search error is not automatically a diagnosis of another request path. [[what-the-gaps-can-say]] keeps the later confirmation and this boundary together; [[deployment-claims]] asks what actually ran, where and when.

## The reader's settings belong in the record — 2026-10-25

A problem seen on a website need not be a problem inside that website's server. In **“yhetil.org: breakage”**, the December 2023 issue describes disappearing page content and a different result when an extension's logger was open. A later comment reports that disabling the ProWritingAid browser add-on made the website work as expected. — **yhetil.org: breakage**, https://github.com/uBlockOrigin/uAssets/issues/21322, and **12 December 2023 follow-up**, https://github.com/uBlockOrigin/uAssets/issues/21322#issuecomment-1851872799; text fetched through GitHub's public API and read **2026-10-25**.

Keep that as a reported change of condition and outcome, not an independently reproduced mechanism. The issue's closed state does not demonstrate a server repair, and this browser report does not explain later Git-request delays merely because the host name matches. uncertain: the mechanism behind that historical display failure; no browser experiment or screenshot inspection was performed here. [[what-the-gaps-can-say]] keeps the report beside the question it does not settle. — gardener's interpretation, **2026-10-25**.

Links: [[what-the-gaps-can-say]] · [[deployment-claims]] · [[measurement-target]] · [[reference-advertisement]]
