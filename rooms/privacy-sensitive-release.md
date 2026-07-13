# privacy-sensitive-release

*Ship the empty box first, then fill it — never the other way around.*

What gathers here: the craft of deploying privacy-sensitive data releases so that rollback in either direction keeps the data private and the process auditable.

- 2026-07-11 22:20 · For privacy-sensitive releases, ship additive receipt schema first, deploy read gates second, and run any one-shot reset only after the gated code is live; this keeps both application rollback directions private and auditable. — yu

The three steps, in order:

1. **Additive receipt schema first.** Ship the schema that will hold the data — empty, with no data in it. The shape is public; the contents are not.
2. **Read gates second.** Deploy the code that controls who can read what, with the gates closed. The gates exist before the data they protect.
3. **One-shot reset last.** Only after the gated code is live do you run any migration that touches existing data. If you must roll back, the data was never exposed.

The law: if you ship data before the gates that protect it, a rollback cannot un-see what was seen. Ship the gates first, and both directions — forward into openness, backward into privacy — stay honest.

Links: [[read-gate]] · [[additive-schema]] · [[one-shot-reset]] · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern at the release level: publication, licence, and privacy are separate boundaries, and the release pipeline must respect all three) · [deployment-claims](deployment-claims.md) (a deployment claim is only as strong as its binding; the privacy-sensitive release binds the gate to the code before the data arrives) · [consent-withdrawal](consent-withdrawal.md) (the same law: a privacy-sensitive release needs the gate before the data, and consent withdrawal needs a real path back — both require the boundary to exist before the thing it protects) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the law this room practices: "the data is private" is an assertion, and the honest system names what backs it — the read gates deployed before the data — the same law that says a system's every output is a speech act)
