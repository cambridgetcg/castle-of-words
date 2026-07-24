# package-authority

The authority of a package — who vouches for its bytes — must stay separate from the channels that discover it.

An immutable versioned artifact with exact bytes can be authoritative on its own. npm and PyPI are optional mirrors, not sources of truth. Advertise each mirror only after exact-version public proof exists; configure trusted-publisher identity per package and per registry. Discovery says "here it is"; authority says "these bytes are the real ones." The two facts must never be fused.

Links: [[immutable]] · [[discovery]] · [[authority]] · [ordered-release](../rooms/ordered-release.md)
