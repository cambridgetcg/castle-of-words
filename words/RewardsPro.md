# RewardsPro

RewardsPro is yu's Shopify app — published on the App Store since 2025-12-16,
with billing fully wired through Shopify managed billing (Free / Pro $39 / Max
$149 / Ultra $499 a month), so money flows Shopify → Partner payout → bank
with no Stripe dependency.

It is the [[money-loop]]'s engine: the most revenue-ready asset in the estate,
code-healthy (installs clean, typechecks with zero errors), but dead at the
database because its AWS key was killed. The one blocker is [[credential-rotation]]
— rotate the AWS key, run the Aurora migration, verify health, and the engine
restarts. The first pound lands when a merchant converts after the 7-day trial,
realistically 6–8 weeks, because the marketing engine that would find the first
customer has never once run.

Links: [[money-loop]] · [[credential-rotation]] · [[keyholder]] · [[platform]]