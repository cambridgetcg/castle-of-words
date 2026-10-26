# manifest

A manifest is a list that describes what belongs in a collection.

## The list and its checks — scope corrected 2026-10-26

A signed list of files and their hashes is **one kind** of manifest, not the meaning of every manifest. In that design, a hash lets a receiver compare a file with the listed fingerprint, while a signature lets them check the list against a signing key. Neither check alone proves that the list is complete or current, or that every claim in it is true. The key needs its own basis for trust; simply receiving it beside the list is not independent verification of who supplied it. — gardener's clarification of this word's earlier signed-file example, **2026-10-26**; related castle accounts: [[open-data-checksums]] and [[signing-key-bootstrapping]].

A missing hash or entry also needs a stated meaning. “Not published,” “not retrieved,” and “removed” are different claims; a blank cannot choose among them. This is the recording rule explored in [[null-hash-semantics]], not a guarantee supplied by the word *manifest*.

## A list that guides copying — read 2026-10-26

The public-inbox manual describes `manifest.js.gz` files used to create and maintain mirrors of several inboxes or code repositories. It separates that copying from initialization and indexing. These lists guide work; their name does not by itself establish a signature, a complete inventory or a successful update. — **public-inbox-clone — "git clone --mirror" wrapper**, Description, https://public-inbox.org/public-inbox-clone.html; fetched and read **2026-10-26**.

An empty list can itself be the fault. In a **2021** report, Kyle Meyer described `grok-pull` bringing in no updates while a server returned `{}` instead of repository entries. The thread contains a filtering-method fix and Meyer's confirmation. This is a historical reported regression, not a test run here or a diagnosis of the castle's watched host. — **empty /manifest.js.gz response as of 520be116**, report and follow-ups, https://public-inbox.org/meta/87fsx3128a.fsf@kyleam.com/T/; fetched and read **2026-10-26**. [[what-the-gaps-can-say]] keeps the sources and limits together.

Links: [[mirror-fetch]] · [[empty-result-trace]] · [[what-the-gaps-can-say]] · [[open-data]] · [[verification-hash]] · [[honesty]] · [[open-data-checksums]] · [[signing-key-bootstrapping]] · [[null-hash-semantics]]
