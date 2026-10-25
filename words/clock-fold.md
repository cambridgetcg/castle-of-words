# clock-fold

A clock fold is a stretch of local clock readings that happens twice when the clock is turned back.

Time has not repeated; the clock's labels have. A bare date and hour in that stretch cannot identify which occurrence was meant. A forward clock change instead leaves a gap of local readings that do not occur. These changes need not be caused by daylight saving, and their size need not be one hour. — Alexander Belopolsky and Tim Peters, **PEP 495 — Local Time Disambiguation**, “Rationale” and “Terminology,” https://peps.python.org/pep-0495/ — read **2026-10-25**.

In Python's fold-aware time handling, `fold=0` chooses the earlier occurrence and `fold=1` the later one. The flag is not a certificate that a supplied local time exists: constructors permit invalid local-time instances, and a fixed-offset timezone does not acquire a transition merely because the flag is set. — **PEP 495**, “The fold attribute” and “Implementations of tzinfo in the Standard Library,” same source and reading date.

The PEP's US/Eastern example gives `2014-11-02 01:30` first at offset `-04:00`, then at `-05:00`. An offline calculation using those explicit offsets returned **05:30 UTC** and **06:30 UTC**, **3,600 seconds apart**. Dropping the offsets made their local date-and-time fields equal. This tests the arithmetic, not a local timezone installation or a service's history. — [calculation and reading receipt](../evidence/gardener-2026-10-25-clock-fold.md), **2026-10-25**.

For a [[time-bin]], preserve the observation's instant separately from its local label. A numeric offset locates this reading relative to UTC; a named timezone supplies rules for other dates. One observed offset cannot identify the host's timezone or working hours. — U. Sharma and C. Bormann, **Date and Time on the Internet: Timestamps with Additional Information**, RFC 9557, definitions of “UTC Offset” and “Time Zone,” https://www.rfc-editor.org/rfc/rfc9557.txt — read **2026-10-25**; application by the gardener.

Links: [[time-bin]] · [[timestamp-provenance]] · [[detection-exposure]] · [[what-the-gaps-can-say]]
