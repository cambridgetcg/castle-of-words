# reference-advertisement

A reference advertisement is a Git server's list of names for saved work and the object each name points to.

An **object ID** identifies a Git object; a **reference** is a name, such as a branch name, that can point to one. The list a particular client sees is not necessarily every name in the repository.

In protocol v0/v1, the initial advertisement also carries capabilities—what the server says it can do—after a NUL separator on its first reference record. In protocol v2, the first response advertises capabilities instead; the client asks for the references separately with `ls-refs`. Hashing these different kinds of reply does not make them equivalent observations.

The optional `session-id` identifies a server process and can differ between requests served by different processes without a reference moving. The optional `agent` describes software, not repository contents. But `symref=HEAD:...` or v2's `symref-target:...` carries a meaningful target: HEAD can switch between two branches pointing to the same object. Keep symbolic targets separate from the name-to-object map rather than discarding them as noise.

The comparison rule lives in [[what-the-gaps-can-say]], “A Git reply can change without a reference moving”: retain raw bytes, parse the negotiated protocol, compare like-scoped reference maps, and report other changes separately. A [[body-fingerprint]] alone cannot name the changed field or prove a mirror fetch.

Sources, read **2026-10-09**, from the Git project's published documentation source:
- **gitprotocol-capabilities** — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-capabilities.adoc.
- **gitprotocol-v2** — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-v2.adoc.
- **gitprotocol-pack**, “Reference Discovery” — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-pack.adoc.

Links: [[body-fingerprint]] · [[what-the-gaps-can-say]] · [[living-two-hundred]] · [[observation-gap]]
