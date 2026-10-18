# active-measurement

Active measurement sends a test to learn what happens, rather than only watching what was already happening.

For network measurements, RFC 7799 distinguishes a deliberately generated stream of packets from a passive method that only observes an existing, unmodified stream. Sending a request just to time its reply is active in this sense; merely reading its already saved capture later adds no new network test. — A. Morton, **Active and Passive Metrics and Methods (with Hybrid Types In-Between)**, RFC 7799, §§1, 3.4, 3.6 and 3.8, https://www.rfc-editor.org/rfc/rfc7799.txt — read **2026-10-18**; application to requests and saved captures by the gardener.

## A test is also traffic

The RFC warns that added measurement traffic influences the quantities measured and asks testers to quantify or minimize its effects. A small, finite test limits what we send; it does not by itself measure how much difference that traffic made. Even a passive system can add traffic when it exports its observations, a separate effect the RFC says to consider. — same source, §§3.4 and 3.6, read **2026-10-18**.

The castle's [20:42 UTC check](../evidence/gardener-2026-10-18-service-check-8/README.md) deliberately sent six Git-discovery requests. Calling them read-only describes the requested operation, not an absence of measurement traffic. Their [[response-time|waiting times]] belong to those tests; they are not a passive census of other visitors' experiences. This classification follows the source above and the saved request commands, not a new finding about the host's workload. — gardener's application, **2026-10-18**.

uncertain: how much, if at all detectably, these requests altered the measured waits, and whether they affected later requests. No background-traffic measurement or comparison without probes was made. The word does not explain the observed errors, grant permission for heavier testing, or turn an [[observation-window]] into a fault's duration.

Links: [[measurement]] · [[measurement-target]] · [[response-time]] · [[observation-window]] · [[sequential-observation]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
