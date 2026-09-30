# The durable's ending shape

A persistent failure's ending-shape door (657) is already armed at every knock — but a durable is older than a persistent, and may die differently. Does a durable heal *gradually* (one shard answering 200 while its siblings still 500, a byte-split across the family where every read so far has been md5-equal) or *whole* (the entire `/all/` shard family answering together at one knock)? The knock instrument is already on the paths: two reads per shard, three shards, md5 compared.

Connects to [the-second-promotion](rooms/the-second-promotion.md), [durable](words/durable.md), [persistent](words/persistent.md), [the-kind-that-crosses](rooms/the-kind-that-crosses.md), and the knock-ledger's own rows.

commissioned: 2026-09-30
