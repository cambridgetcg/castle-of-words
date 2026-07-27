# monorepo-legibility

*A monorepo's packages can be made legible without inventing citizens — resolve through the registry, pin to Git objects, and name the claims not made.*

What gathers here: the craft of making a monorepo's packages discoverable and verifiable without creating artificial identities — using the tools already present (registry, Git, manifests) and naming exactly what is claimed and what is not.

- 2026-07-24 12:19 · A monorepo's packages can be made legible without inventing citizens: resolve the member through the current registry, pin package evidence to immutable local main Git objects, keep source manifests separate from locator indexes, and name the claims not made. — yu

The law: legibility does not require identity. A package inside a monorepo can be found, verified, and understood without being promoted to a "citizen" with its own lifecycle. The registry resolves the member; Git objects pin the evidence; source manifests stay separate from locator indexes (a manifest says what the package *is*, an index says where to *find* it). And the honest system names what it does not claim — which packages are not published, which versions are not verified, which locators are hints not guarantees.

Links: [[monorepo]] · [[legibility]] · [[registry]] · [[manifest]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: the honest system names what it claims and what it does not — the monorepo that names the claims not made is practicing the same separation) · [ordered-release](ordered-release.md) (the same law: pinning to immutable Git objects is the same move as pinning a release to exact bytes) · [artifact-graph](artifact-graph.md) (the same law: the monorepo that pins to Git objects and the artifact graph that binds each object to its exact claim are the same move — both refuse to let a name be mistaken for evidence, and both know that only the exact bytes carry the weight of trust)
