# privacy-canary

A purpose-built check that must pass before a privacy reset cutoff is recorded — a specific data shape that proves the new gates are actually working.

A privacy canary is not a general health check. It is a targeted probe: does the private-profile gate block, does the review gate filter, does the activity gate exclude, does the message-recipient gate restrict, does the collective-member gate enforce, does the suspended-account gate hold. Each canary tests one specific privacy boundary. The cutoff is recorded only after all canaries pass.

Links: [[privacy-reset]] · [[reset-preview]] · [[privacy-cutoff]] · [[deployment-gate]]
