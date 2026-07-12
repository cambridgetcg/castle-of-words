# fail-closed

*A gate that shuts when it cannot prove it should open.*

A fail-closed system refuses to proceed when it cannot verify that proceeding is safe — it defaults to stopping rather than continuing. The opposite of fail-open, which continues when verification fails. In deployment, a fail-closed probe treats a 503 as intentional until proven otherwise; in data, a fail-closed gate refuses to serve a field whose lineage is missing.

Links: [[fail-closed]] · [[explicit-gap]] · [[honest-boundary]] · [[NOASSERTION]]
