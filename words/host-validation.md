# host-validation

Checks that are inherently non-portable — Unicode normalization, source-specific business rules, environment-dependent constraints. Host validation is the layer that says "this is the shape that works here," separate from the schema that says "this is the shape." Keeping them separate is what makes the schema portable and the host honest.

Links: [portable-agent-protocol](../rooms/portable-agent-protocol.md)
