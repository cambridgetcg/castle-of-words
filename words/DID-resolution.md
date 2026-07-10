# DID-resolution

The act of turning a decentralized identifier (DID) into its corresponding DID document — the public record that says where to find the identity's keys and services.

A federated DID host is untrusted network input. Honest resolution requires public HTTPS, rejects every non-global DNS answer, pins the validated answers into the TLS socket lookup, and refuses redirects so the DID host remains the certificate trust origin.

Links: [[honesty]] · [[bearer-authority]]
