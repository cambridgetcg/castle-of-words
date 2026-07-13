# community-data-network-room

*The network that infers a person from their profile has already broken the trust it was built to earn.*

What gathers here: the craft of building community data networks on opt-in rather than inference, where [[coverage]] truth, per-source rights, and [[private-by-default]] consent are prerequisites to network effects.

Built understanding from yu, 2026-07-11 and 2026-07-12:

- 2026-07-11 20:55 · A community data network should expose opt-in organisations, events and aggregate needs, not infer a people graph from public profiles, wishlists, holdings or messages. Coverage truth, per-source rights and private-by-default consent are prerequisites to network effects. — yu
- 2026-07-12 12:46 · A community data point observes its contributor too. Keep permission attached to the fact, publish only consented aggregates, and count [[distinct-count|distinct people]] rather than rows so one observer cannot manufacture a crowd. — yu
- 2026-07-12 12:56 · Privacy thresholds for community market data must count distinct consenting people, not rows: one contributor can create many observations. Keep below-threshold dimensions, counts, dates, and values inside the database; disclose only that [[suppression]] occurred. — yu

The rules, plainly:

1. **Opt-in organisations.** An organisation appears in the network only when it explicitly joins. No scraping, no inference from public registrations.
2. **Events, not people.** The network exposes what is happening — events, needs, gatherings — not who is attending or what they own.
3. **Aggregate needs, not individual wants.** "Three organisations need volunteers" is honest. "This person wants X based on their wishlist" is not.
4. **No inferred people graph.** Public profiles, wishlists, holdings, and messages are not signals to connect people. They are separate facts that stay separate.
5. **Coverage truth first.** Before the network grows, every field's [[provenance]] and rights are recorded. A field without rights is not part of the network.
6. **Private-by-default.** No person is in the network until they explicitly opt in. The default is absence.

The law: network effects built on inference are network effects built on sand. The honest network grows slower because it asks permission, and the permission is what makes the growth durable.

Links: [[community-data-network]] · [[private-by-default]] · [[coverage]] · [[provenance]] · [[distinct-count]] · [[suppression]] · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern is the same law: publication, licence, and privacy are separate truths, and a network that fuses them manufactures connections that do not exist) · [coverage-truths](coverage-truths.md) (the five coverage truths are the prerequisites this room names: a network that does not know which fields have rights cannot know which connections are lawful) · [collector-data-rights](collector-data-rights.md) (the same law: a community network that infers a people graph from public signals and a collector-data API that treats public access as a reuse licence are the same mistake — reachability is not permission, and inference is not consent) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the law this room practices: "this is a community" is an assertion, and the honest system names what backs it — explicit consent, not inferred signals — the same law that says a system's every output is a speech act)
