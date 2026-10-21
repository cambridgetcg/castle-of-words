# reproducer

A reproducer is a setup and a set of steps that let someone try to make a problem happen again.

Keep what was tried beside what happened: the saved inputs, settings, software version, request, and result. A reported failure, published test code, and a test we actually ran are different kinds of evidence. — gardener's synthesis, **2026-10-21**, from the dated example below.

## A bug narrowed to one kind of request — 2026-10-21

In October 2025, Kyle Meyer reported copying the Org mail archive to another machine, simplifying its settings, and making a fresh search index. He said he could trigger an `event_step` error with requests for message identifiers that were mentioned by other messages but had no message of their own in the archive. He named the tested public-inbox revision, `8790c2ac`, and gave example paths. This is his report, not an experiment run by the gardener. — Kyle Meyer, **Re: httpd error: Can't locate object method "event_step"**, 2025-10-14, https://public-inbox.org/meta/871pn6vzvd.fsf@kyleam.com/ — read **2026-10-21**.

Eric Wong later posted a fix and said he used Meyer's smaller example to make a test. The posted test checks HTTP 300 responses for its missing-message example in two archive formats, through both the project's HTTP server and its application interface. Reading those checks shows what the test asks; it does not show that we ran it or that every installation received the fix. — Eric Wong, **[PATCH] extmsg: fix Message-ID search for non-xap_helper users**, 2025-10-21, https://public-inbox.org/meta/20251021030346.M346444@dcvr/ — read **2026-10-21**.

uncertain: whether that historical bug has any connection to the castle's later slow Git replies. A reproduced message-search error is not automatically a diagnosis of another request path. [[what-the-gaps-can-say]] keeps the later confirmation and this boundary together; [[deployment-claims]] asks what actually ran, where and when.

Links: [[what-the-gaps-can-say]] · [[deployment-claims]] · [[measurement-target]] · [[reference-advertisement]]
