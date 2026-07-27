# extension-boundary

The seam where a host and its extension meet — safe only when the host pins its own platform, identity, policy, and brake primitives before the extension can evaluate any code.

An extension boundary is lazy when the host defers pinning its own primitives until after the extension loads. At that point the extension's initialization can redefine the baseline that later checks trust, and the boundary is no boundary at all. The honest host captures every primitive it will later check — platform, identity, policy, brakes — before evaluating a single line of extension code, and passes an explicit child working directory so the extension cannot inherit the caller's environment.

Links: [[preload]] [[brake]] [[fail-closed]] [[child-environment]]
