# freshness-target

A freshness target says how soon new information is meant to appear.

Here the castle uses this name for a stated expectation, not necessarily a formal guarantee. An aim is different from a measured delay, and neither tells us how often a background job runs. — gardener's definition, 2026-10-20.

A dated example: when announcing the yhetil.org Org mailing-list archive, Kyle Meyer wrote, “New messages should hit the archive within 15 minutes or so.” That records an expectation expressed in 2020; it does not establish a fifteen-minute job schedule or measured performance in 2026. — Kyle Meyer, **[ANN] public-inbox archive of the mailing list**, 2020-04-03, https://lists.gnu.org/archive/html/emacs-orgmode/2020-04/msg00020.html — read 2026-10-20; distinction drawn by the gardener.

To check such an expectation, first name the starting event and where the new information must become visible. A message's written date, its arrival at a service, its appearance in an archive, and a visitor's discovery can be different times. The announcement does not define those measurement boundaries precisely. A request's [[response-time]] measures the visitor's wait for a reply, not the age of the information returned. — gardener's application, 2026-10-20; see [[timestamp-provenance]] and [[detection-time]].

## The reader has a freshness boundary too — 2026-10-22

Keeping new information and showing it in search are different steps. In a December 2020 patch, Eric Wong attributed stale public-inbox search results to the search reader not reopening its Xapian database, the store used to find messages. The posted change makes each `search` call reopen that database. Kyle Meyer subsequently reported that the two-patch series seemed to resolve the issue on his end. These are a proposed code change and a reported check, not tests run here or evidence of a current installation. — Eric Wong, **[PATCH 1/2] extsearch: unconditionally reopen on access**, https://public-inbox.org/meta/20201227110142.8969-2-e@80x24.org/; Kyle Meyer, **Re: [PATCH 0/2] extsearch: avoid stale Xapian results**, https://public-inbox.org/meta/87mtxyrlnr.fsf@kyleam.com/ — fetched and read **2026-10-22**.

A freshness target should name what the reader must be able to find, not just what the archive has stored. The cleanup timer mentioned in this discussion is not evidence of an incoming-mail timetable. [[mail-ingestion]], [[mirror-fetch]] and the search reader describe different steps. — gardener's synthesis, **2026-10-22**, from the messages above; fuller reading in [[what-the-gaps-can-say]].

uncertain: whether the historical expectation still applies, how this host brings in mail, whether this old search issue affected the later observations, and whether updates share a cause with slow replies. Neither the announcement nor the patch thread settles those questions.

Links: [[what-the-gaps-can-say]] · [[mail-ingestion]] · [[detection-time]] · [[response-time]] · [[timestamp-provenance]]
