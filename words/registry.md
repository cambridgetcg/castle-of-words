# registry

A registry resolves a name to immutable words — a version pointer that, once set, always points to the same bytes.

A registry is not a database of current state. It is a ledger of resolutions: "name X, at this time, resolved to these exact bytes." When the bytes change, the name gets a new resolution — the old one remains. The honest registry never rewrites history; it appends. A registry that silently changes what a name points to is not a registry but a redirect.

Links: [[foundation]] · [[version]] · [[immutable]] · [[receipt]] · [[karma]]
