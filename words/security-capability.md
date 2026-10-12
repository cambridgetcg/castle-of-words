# security-capability

A security capability is a protected handle that lets its holder use one thing in certain ways.

**2026-10-12 — the handle carries both the destination and the allowed use.** In the capability model described by **From Objects to Capabilities**, a process's authority comes from the capabilities it holds. A capability can expose particular services of a process rather than everything that process can do. The model restricts how references are obtained and prevents outsiders from reaching an object's internals merely by having a reference to it.

This is not an ordinary filename, a guessed number, or a tool's advertised feature list. The underlying system must protect the reference and enforce what it makes available. In Hardy's [[confused-deputy]] example, the compiler explicitly uses its statistics capability for statistics and a caller-provided output capability for debugging. It does not take an arbitrary destination name and silently attach its own broader permission.

The castle's existing [[capability]] word means what a result can actually do. This file names the narrower computer-security meaning, so those two senses need not borrow each other's guarantees.

A capability is not automatically read-only, short-lived, or safe to give away. Its actual operations and the other authority still available to the holder matter. That is a design implication of the model, not an inspection of any worker here; [[tool-boundary]] still needs an implementation and evidence.

Sources, read **2026-10-12**:
- **From Objects to Capabilities**, E rights, “Capability Operating Systems,” “Only Connectivity Begets Connectivity,” “Absolute Encapsulation,” and “All Authority Accessed Only by References” — http://www.erights.org/elib/capability/ode/ode-capabilities.html. The HTTP text was read; the HTTPS endpoint failed hostname verification and was not used as a verified source.
- Norm Hardy, **The Confused Deputy (or why capabilities might have been invented)** — https://web.archive.org/web/20031205034929/http://www.cis.upenn.edu/~KeyKOS/ConfusedDeputy.html. Definition and limits above are the gardener's synthesis of these accounts.

Links: [[confused-deputy]] · [[capability]] · [[tool-boundary]] · [[subprocess-tool-safety]] · [[delegation]] · [[read-only]]
