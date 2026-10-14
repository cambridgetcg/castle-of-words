# binding

The chain of evidence that connects a claim to the thing it claims about.

In a deployment claim, keep the reviewed artifact, served representation, runtime evidence, observation time, and scope attached to the particular claims they support. An [[ETag]] labels a selected HTTP representation; it does not by itself tie reviewed code to the executable that ran. Without binding, a claim floats — it cannot be checked, only believed.

Scope corrected **2026-10-14** from [deployment-claims](../rooms/deployment-claims.md), “The tag does not identify the whole deployment,” and [conditional-writes](../rooms/conditional-writes.md), “A strong tag is not a signed history,” read locally on that date; their RFC 9110 sources were not fetched again, and no deployment was tested here.

Links: [[deployment-claim]] · [[ETag]]
