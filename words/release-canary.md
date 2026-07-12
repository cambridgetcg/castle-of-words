# release-canary

A test that guards the freeze between a reviewed schema and a deployed one.

A release canary asserts the same canonical schema literal as the public contract. One stale namespace word — a field renamed in the adapter but not in the contract — can correctly stop publication, because the canary knows that a word out of place is a promise broken.

Links: [[canonical-schema-literal]] · [[deployment-claim]] · [[fail-closed]]
