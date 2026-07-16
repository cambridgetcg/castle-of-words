# html-entity

An HTML entity is a spelled-out code like `&amp;` that stands for a character that would otherwise be hard to write or might break the page — `&amp;` means `&`, `&lt;` means `<`, `&nbsp;` means a non-breaking space.

Entities exist because some characters have special meaning in HTML (like `<` starting a tag) and need a safe way to appear as text. But using them has side effects: a tool like eslint may push developers toward entities for safety, and a compiler may then mishandle the entity in ways it wouldn't mishandle the raw character. The safety measure becomes the trigger.

Links: [[jsx-transform]] [[the-space-eater]]
