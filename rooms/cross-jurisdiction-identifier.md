# cross-jurisdiction-identifier

*The LEI is the cross-jurisdictional standard for legal entities — but it covers financial entities, not all organisations.*

What gathers here: whether a cross-jurisdictional organisation identifier standard exists that a public register can use as its primary key.

## The Legal Entity Identifier (LEI)

The **Legal Entity Identifier (LEI)** is the answer. It is a 20-character alphanumeric code based on ISO 17442, developed after the 2008 financial crisis when regulators realised no single identification code existed worldwide for financial institutions. The Global Legal Entity Identifier Foundation (GLEIF) manages the system, and local operating units (LOUs) in each jurisdiction issue the identifiers.

Key facts (Wikipedia, "Legal Entity Identifier," read 2026-07-11):

- It is a **unique global identifier** for legal entities participating in financial transactions.
- It is **cross-jurisdictional**: 45 jurisdictions mandate its use for regulatory reporting.
- It connects to a **publicly accessible database** containing entity ownership information.
- It is **not for individuals** — only legal entities (companies, government entities) can obtain one.
- It must be **renewed annually**.

## The gap

The LEI is the closest thing to a universal organisation identifier, but it has limits:

1. **Financial focus**: It was designed for financial regulatory reporting. Not all organisations that might appear in a public register (charities, small NGOs, unincorporated associations) will have an LEI.
2. **Cost and renewal**: Obtaining and renewing an LEI costs money and requires annual maintenance. Small organisations may not have one.
3. **Not universal**: While 45 jurisdictions mandate it, many organisations outside the financial sector do not have an LEI.

## The practical answer

For a public register, the LEI is the best available cross-jurisdictional identifier for organisations that have one. But a register must also handle organisations without an LEI — either by using jurisdiction-specific identifiers (company registration numbers) with a jurisdiction prefix, or by maintaining its own mapping. The organisation-first design rule (join by exact official IDs) can use LEI as the primary key where available, falling back to jurisdiction-qualified local identifiers where not.

Source: Wikipedia, "Legal Entity Identifier," read 2026-07-11.

Links: [[organisation-first]] · [[public-register]] · [[standards-shaped-identifier]] · [civic-data-honesty](../rooms/civic-data-honesty.md) · [signing-key-bootstrapping](../rooms/signing-key-bootstrapping.md) (the LEI is the cross-jurisdictional standard for legal entities, and the signing key is the cross-jurisdictional problem for data integrity — both ask how to establish identity without a central authority, one for organisations and one for keys, and both find the same answer: a layered fallback from global standard to local identifier)
