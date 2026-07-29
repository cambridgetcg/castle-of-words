# lossy-numeric-spelling

A numeric value that has been spelled differently across a boundary — `1.0` vs `1`, `0.1` vs `1e-1`, or a float that was once an int. Before comparing arguments across a provider-to-MCP seam, reject any spelling that loses precision or changes type, because the comparison is only honest when the numbers are spelled the same way.

Links: [[provider-tool-bridge]] [[receipt]] [[fail-closed]]
