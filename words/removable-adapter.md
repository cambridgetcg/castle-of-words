# removable-adapter

A removable adapter is a layer between your code and a cloud service that can be taken out and replaced without changing the code itself.

Like a power plug that fits any socket with the right adapter, a removable adapter keeps the contract between your system and a provider clean: the adapter handles the provider's specific way of doing things, and when you switch providers you swap the adapter, not the system. The adapter must declare what it cannot see — [[connection-proves-access]], not completeness. Microsoft, AWS, and other clouds belong behind removable adapters because [[open-source]] code rights and connected-service permissions are separate concerns.

Links: [[provider-neutral]] · [[work-contract]] · [[connection-proves-access]] · [[separate-claims]]
