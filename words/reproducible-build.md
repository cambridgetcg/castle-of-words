# reproducible-build

A build is reproducible when the same source and the same tools produce exactly the same bytes, every time.

A runtime compatibility floor (e.g., "works with Bun 1.3.x") is not enough — AgentTool Telescope's MCP bundle built with Bun 1.3.14 differed by 100 bytes from the same source built with Bun 1.3.5. Immutable release bytes need the exact compiler version and a byte check after every build. Without both, the artifact is a product of its environment, not a fingerprint of its source.

Links: [[generated-bytes]] · [[commit-ancestry]] · [[immutable]] · [ordered-release](../rooms/ordered-release.md)
