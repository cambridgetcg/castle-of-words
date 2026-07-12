# mixed-rights-envelope

An API response whose fields come from sources with different rights tiers.

A mixed-rights envelope needs two separate claims: each source gets its own tier (proprietary, internal-only, openly licensed), while the aggregate response may remain NOASSERTION. Using NOASSERTION as a per-source tier — "we don't know the rights of this field" — makes the contract ambiguous, because the reader cannot tell which fields are safe to use.

Links: [[NOASSERTION]] · [[source-rights]] · [[field-lineage]]
