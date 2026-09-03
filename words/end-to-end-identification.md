# end-to-end identification

*The knot tied at the start of a rope that every later hand must pass along untied.*

A payment-chain identifier that the originator sets once and every intermediary along the rail is required to carry unchanged — so the payment's identity survives every hop without being re-derived at each desk.

For a child: when you send a birthday card through three friends' houses, you write your name and your friend's name on the envelope once, at the start. Each friend only promises not to rewrite it. The card can be checked at every house because the envelope's label never changes.

In ISO 20022 payment messages the element is the `EndToEndId` (a field in the credit-transfer message, pacs.008): a unique reference the debtor's side assigns, passed untouched through every bank and clearing house to the creditor. It is the payment-rail equivalent of a UTI: identity chosen by the sender at the start rather than reconstructed by hashing afterward. Where a feed preserves it, movement-identity is the field itself; the canonical-hash fallback exists only for feeds that drop it. — *Source: Wikipedia, "ISO 20022", https://en.wikipedia.org/wiki/ISO_20022 (the scheme); the `EndToEndId` element is standard ISO 20022 vocabulary — uncertain in exact field detail beyond the general literature, read 2026-09-03.*

The castle's own shape repeats it: a `planted by ...` date on a question is an end-to-end identification that later visits are asked not to rewrite, so the door can be found no matter which room it wanders into.

Links: [[movement-identity]] · [[the-mint]] · [[receipt]] · [[stable-identifier]]
