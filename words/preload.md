# preload

Loading and capturing primitives before the extension boundary opens, so later checks compare against frozen references rather than live mutable bindings.

A preload is not a stable baseline if later checks call live built-in bindings that the extension could have mutated, or if they inherit the caller's working directory. The honest preload captures every primitive the boundary will later check — platform functions, identity, policy, brakes — and passes an explicit child working directory, all before evaluating a single line of extension code.

Links: [[extension-boundary]] [[child-environment]] [[fail-closed]] [[brake]]
