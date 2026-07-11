# lei-fallback-data-model

*When the global identifier does not cover everyone, the fallback must be as honest as the primary key.*

What gathers here: for organisations without a Legal Entity Identifier (LEI), what is the most honest fallback — jurisdiction-qualified local IDs, a registry-maintained mapping, or something else — and what the data model looks like when both LEI and non-LEI entities coexist.

## The LEI's coverage gap

The LEI is the best available cross-jurisdictional identifier for legal entities, but it was designed for financial regulatory reporting. Organisations outside the financial sector — charities, small NGOs, unincorporated associations, community groups, sole traders — often do not have an LEI. A public register that uses LEI as its primary key must also handle entities without one.

The gap is not small. The LEI covers entities that participate in financial transactions and are required to report to financial regulators. A civic transparency register (tracking political donations, lobbying, public contracts) will encounter many organisations that have never needed an LEI.

## The most honest fallback

The most honest fallback is a **jurisdiction-qualified local identifier**. The pattern:

```
{jurisdiction}:{local-id-type}:{local-id}
```

For example:
- `gb:companies-house:12345678` — a UK company registered with Companies House
- `us:delaware:file-1234567` — a Delaware corporation
- `ca:cra-charity:123456789RR0001` — a Canadian registered charity
- `de:handelsregister:HRB 123456` — a German commercial register entry

The jurisdiction is an ISO 3166-1 alpha-2 country code. The local-id-type names the register or identifier system. The local-id is the identifier within that system.

This pattern is honest because:

1. **It names its source**: The jurisdiction and register tell the consumer exactly where to verify the identifier.
2. **It does not pretend to be global**: A jurisdiction-qualified ID is explicitly local. It does not claim the universality the LEI claims.
3. **It is stable**: Jurisdiction codes and local register names change slowly. The identifier within a register is usually stable for the life of the entity.
4. **It is verifiable**: A consumer can check the local register to confirm the entity exists and the identifier is valid.

## The data model

When both LEI and non-LEI entities coexist in the same register, the data model needs a single identifier field that can hold either:

```json
{
  "organisation": {
    "id": "gb:companies-house:12345678",
    "id_system": "companies-house",
    "id_jurisdiction": "gb",
    "lei": null,
    "name": "Example Charity",
    "type": "charity"
  }
}
```

Or for an LEI-bearing entity:

```json
{
  "organisation": {
    "id": "lei:5493001BABY5L7CUZL82",
    "id_system": "lei",
    "id_jurisdiction": null,
    "lei": "5493001BABY5L7CUZL82",
    "name": "Example Bank PLC",
    "type": "company"
  }
}
```

The `id` field is the primary key — always present, always unique. The `id_system` field names the identifier system. The `lei` field is present only when the entity has an LEI. The `id_jurisdiction` field is present only for jurisdiction-qualified local IDs.

This model keeps the primary key uniform (a single string) while making the identifier system explicit. A consumer that only understands LEIs can filter on `id_system: "lei"`. A consumer that needs all entities can use the `id` field directly.

## The honest limits

The jurisdiction-qualified fallback has limits:

1. **Not all jurisdictions have stable registers**: Some countries have no public company register, or the register is incomplete, or identifiers change. The fallback is only as good as the local register.
2. **The local-id-type namespace is ad hoc**: There is no global registry of local identifier systems. The register must maintain its own controlled vocabulary of `id_system` values.
3. **Cross-jurisdictional deduplication is manual**: Two jurisdiction-qualified IDs might refer to the same entity (a company registered in two jurisdictions). The register cannot detect this automatically.
4. **The LEI is still preferred**: Where an entity has an LEI, the register should use it. The fallback is for entities that genuinely do not have one, not a shortcut to avoid looking one up.

Source: Wikipedia, "Legal Entity Identifier" — the LEI is for legal entities participating in financial transactions, and individuals cannot obtain one. The jurisdiction-qualified pattern is a common design in open data registries (OpenCorporates, OpenOwnership). Read 2026-07-11.

Links: [[organisation-first]] · [[public-register]] · [[standards-shaped-identifier]] · [cross-jurisdiction-identifier](cross-jurisdiction-identifier.md) · [civic-data-honesty](civic-data-honesty.md) (the organisation-first rule — join by exact official IDs — is the same principle: the identifier must be verifiable against its source, and the fallback must name its source as explicitly as the primary key) · [wired-registry](wired-registry.md) (the LEI/fallback data model is the identity layer of the wired registry — it identifies organisations honestly, naming the source of every identifier, the same honesty the whole registry demands of every piece)
