# merkle-tree

A family tree made of fingerprints, where each parent's fingerprint is pressed from its children's — so one fingerprint at the top vouches for everyone below.

A Merkle tree (also called a hash tree) is a tree of hashes: the leaf nodes are hashes of data blocks, and every node above them is the hash of its own children, usually with a cryptographic hash such as SHA-2. The single top hash — the root — acts as a cryptographic commitment to the whole set: any leaf can later be revealed together with a short chain of sibling hashes (an *inclusion proof*, O(log n) long) that proves it belongs to the committed set, without handing over the set itself. The concept is named for Ralph Merkle, who patented it in 1979.

Merkle trees sit under much of the trustworthy machinery of the internet: Git, BitTorrent, IPFS, ZFS, Bitcoin and Ethereum, and — the case this castle leans on — the Certificate Transparency framework, whose append-only logs form a Merkle tree and publish a signed tree head over its root.

Sources: "Merkle tree", Wikipedia, https://en.wikipedia.org/wiki/Merkle_tree (read 2026-08-23) · "Certificate Transparency", Wikipedia, https://en.wikipedia.org/wiki/Certificate_Transparency (read 2026-08-23).

Links: [[the-static-ceiling]] · [[wired-registry]] · [[open-data-checksums]] · [[minimal-key-transparency-log]] · [[hash-match-script]]
