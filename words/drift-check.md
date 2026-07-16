# drift-check

A CI step that verifies a generated artifact (like an OpenAPI spec or JSON Schema) still matches what the generator would produce from the same source — catching the moment when the committed snapshot and the live generation diverge.

Without a drift check, the committed contract can silently go stale while unit tests pass against the stale copy. The drift check is the gate that says: the contract you are about to deploy is the contract you think you are deploying.

Links: [[generated-snapshot]] · [[api-contract]] · [[deployment-gate]] · [[smoke-test]]
