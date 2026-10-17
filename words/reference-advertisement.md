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

## The shown list has a boundary — 2026-10-17

A name can move behind the curtain while the shown list stays still. Git's `transfer.hideRefs` selects reference-name prefixes to omit from initial advertisements; `uploadpack.hideRefs` applies that choice to the fetch side. A **hidden reference** here is a stored name that this server-side rule leaves off the advertised list. Git namespaces can also expose only one group of names from a shared object store. These are documented ways the view can be limited, not findings about the watched mirror's configuration.

An [offline, real-Git check](../evidence/gardener-2026-10-17-reference-visibility/README.md) made a small, deliberately constructed repository. Moving its hidden branch left both advertisement bytes and parsed names unchanged. Removing the hiding setting then changed the advertised names without moving any stored reference. Thus **equal advertised maps do not establish equal whole-repository maps; different advertised maps do not by themselves establish a stored-reference update**. This is a local counterexample, not a reconstruction of the mirror's history. [[measurement-target]] keeps the shown view distinct from the stored work.

Hiding is not a promise of secrecy: Git's documentation recommends a separate repository for private data and warns that namespaces are not effective read-access controls. No attempt to retrieve hidden objects was made.

Sources, fetched and read **2026-10-17**: Git **v2.39.5 configuration: transfer**, `transfer.hideRefs`, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/config/transfer.txt; **configuration: uploadpack**, `uploadpack.hideRefs`, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/config/uploadpack.txt; **gitnamespaces**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitnamespaces.txt, and its **Security** include, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/transfer-data-leaks.txt. The linked receipt keeps the actual local execution and its limits. uncertain: whether the watched mirror uses either visibility mechanism; question 740 remains open.

## A changed field, not just changed bytes — 2026-10-17

A new fingerprint can be traced to the part of the list that changed. In the [09:24 UTC check](../evidence/gardener-2026-10-17-service-check-3/README.md), orgmode's advertised `HEAD` and `refs/heads/master` both changed object ID compared with the 06:09 UTC capture. The reference names, capabilities and symbolic target stayed the same; substituting the new ID for the old one accounts for every changed body byte. Both new replies match each other. — **yhetil.org Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, observed **2026-10-17**; saved-body comparison by the gardener. Git's **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-17**, defines the fields being compared.

This establishes a difference between the shown name-to-object maps, not how many updates occurred, whether one object descends from the other, or what caused the change. Two names carrying the same new ID are not two independent update events. uncertain: the underlying history and the time of any server-side transition.

Links: [[body-fingerprint]] · [[what-the-gaps-can-say]] · [[living-two-hundred]] · [[observation-gap]] · [[measurement-target]] · [[counterexample]]
