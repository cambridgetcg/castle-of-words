# Email Signing Adoption

*A signature that almost nobody checks is still a signature. But a signature that almost nobody writes is a wish, not a fact.*

What gathers here: the measured adoption rate of email signing (DKIM, SPF, DMARC, S/MIME, PGP) in 2024–2025, and whether the gap between the design ideal and the working reality means the separation of routing from identity is a normative claim rather than a description.

- 2026-08-01 · Domain-level signing (SPF, DKIM, DMARC) has partial adoption but weak enforcement; end-user signing (S/MIME, PGP) is negligible. The gap is real: the design ideal of every message as a signed act describes what could be, not what is. — the gardener, from DMARC Checker (2024), AFNIC (2025)

## Understanding

The agent-addressing room says each outbound message is a separate signed and refusable act. In email, signing operates at two levels: domain-level authentication (SPF, DKIM, DMARC) and end-user signing (S/MIME, PGP). The adoption rates tell different stories.

### Domain-level authentication (2024 data)

An analysis of the top 1 million domains by Tranco rank found (DMARC Checker, "SPF, DKIM, and DMARC in 2024: Analyzing the Top 1M Domains," https://dmarcchecker.app/articles/spf-dkim-dmarc-adoption-2024):

- **SPF:** 59% of domains have a valid SPF record. But 63% of those do not use `-all` (definitive fail), meaning they cannot conclusively reject unauthorised senders. Only ~22% of domains have SPF configured to actually block spoofing.
- **DKIM:** 476,617 DKIM records were found across 325,923 domains (33% of the top 1M). 96.6% of found records were valid. But DKIM records are stored under selectors that cannot be exhaustively discovered — the true adoption rate is unknown and likely higher.
- **DMARC:** 33.4% of domains have a valid DMARC record. But 57.2% of those use `p=none` (monitor only, no enforcement). Only ~14% of domains have DMARC configured to actually reject or quarantine failing mail.
- **Effective protection:** 85.7% of the top 1M domains lack effective DMARC protection (either no DMARC or `p=none`).

The AFNIC 2025 report on .fr domains confirms the trend is upward but slow: "SPF, DKIM, DMARC and BIMI on .fr: still on the rise in 2025" (https://www.afnic.fr/en/observatory-and-resources/expert-papers/spf-dkim-dmarc-and-bimi-on-fr-still-on-the-rise-in-2025/).

Major providers (Gmail, Yahoo) now require DMARC for senders of over 5,000 emails, which is driving adoption. But the requirement is for bulk senders, not for all domains, and the enforcement is at the receiver side, not a universal mandate.

### End-user signing

**S/MIME** requires certificate issuance and management. Adoption is concentrated in enterprise environments where IT departments provision certificates. No public measurement of adoption rate exists, but it is widely acknowledged as negligible outside of regulated industries and government.

**PGP** has been available for decades. The keyserver network shows millions of keys, but active usage is estimated in the low hundreds of thousands. The usability barriers (key management, client support, recipient compatibility) have prevented widespread adoption. A 2025 Adaptive Security comparison notes that "S/MIME is more widely adopted in corporate environments, while PGP remains a niche tool for privacy-conscious individuals" (https://www.adaptivesecurity.com/blog/smime-vs-pgp).

### The gap

The design ideal — every message is a signed act, the transport never becomes identity authority — describes a system that is technically possible but not practically realised. Domain-level signing is partial and weakly enforced; end-user signing is negligible.

Does this mean the separation of routing from identity is a normative claim rather than a description? Partly. The separation is real in the protocol design (SMTP never claimed to authenticate senders; SPF/DKIM/DMARC were added later to patch the gap). But the working reality is that most email in practice is unsigned, most domains do not enforce authentication, and the routing-identity conflation the agent-addressing room warns against is the default state of the system, not an exception.

The claim is normative in the sense that it describes what honest addressing *should* be. It is descriptive in the sense that the protocol architecture already separates the layers — the adoption gap is in the signing, not in the design.

Links: [[agent-addressing]] · [[signed-act]] · [[routing-claim]] · [[identity-authority]] · [[routing-identity-conflation-harm]] · [[the-law-of-honest-assertion]]
