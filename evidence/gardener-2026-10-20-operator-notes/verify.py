"""Offline checks for this visit; does not repeat any public request."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

EVIDENCE = Path(__file__).resolve().parent
ROOT = EVIDENCE.parent.parent
before = json.loads((EVIDENCE / "before.json").read_text())

for name in ("courtyard.md", "questions.md"):
    assert sha256((ROOT / name).read_bytes()).hexdigest() == before[name]["sha256"], name

questions = (ROOT / "questions.md").read_text().splitlines()
open_questions = [s for s in questions if s.startswith("- [ ]")]
assert len(open_questions) == 16
assert not any(s.startswith("- ") for s in (ROOT / "courtyard.md").read_text().splitlines())
reserved = re.compile(r"commission|being grown|needs yu|waits for: yu|yu decides", re.I)
unreserved = [i for i, s in enumerate(questions, 1) if s.startswith("- [ ]") and not reserved.search(s)]
assert unreserved == [740, 744, 766]

room_paths = list((ROOT / "rooms").glob("*.md"))
room_names = {p.name for p in room_paths}
gate = (ROOT / "gate.md").read_text()
map_text = gate.split("## Map\n", 1)[1].split("\n## ", 1)[0]
entries = re.findall(r"\]\(rooms/([^)#]+\.md)(?:#[^)]*)?\)", map_text)
assert len(room_names) == 697
assert Counter(entries) == Counter({name: 1 for name in room_names})
assert all(len(re.findall(r"\]\(rooms/", line)) == 1 for line in map_text.splitlines() if line.startswith("- "))

room_path = ROOT / "rooms/what-the-gaps-can-say.md"
room = room_path.read_text()
room_lines = room.splitlines()
assert room_lines[0] == "# what-the-gaps-can-say"
assert room_lines[2].startswith("*") and room_lines[2].endswith("*")
assert room_lines[4].startswith("This room gathers")
start = room.index("## Old mail can enter by more than one route — 2026-10-20\n")
end = room.index("## Sources\n", start)
prior_room = room[:start] + room[end:]
assert sha256(prior_room.encode()).hexdigest() == before["rooms/what-the-gaps-can-say.md"]["sha256"]

word = (ROOT / "words/mail-ingestion.md").read_text()
assert word.splitlines()[0] == "# mail-ingestion"
assert word.splitlines()[2] == "Mail ingestion is bringing arriving messages into an archive so they can be kept and found."
assert word.rstrip().splitlines()[-1].startswith("Links: ")
for target in re.findall(r"\[\[([^]|]+)(?:\|[^]]+)?\]\]", word + room[start:end]):
    assert any((ROOT / location / (target + ".md")).exists() for location in ("words", "rooms", ".")), target

receipts = sorted(EVIDENCE.glob("*-receipt.json"))
assert len(receipts) == 8
statuses = Counter()
for path in receipts:
    record = json.loads(path.read_text())
    label = path.name.removesuffix("-receipt.json")
    raw = (EVIDENCE / (label + ".html")).read_bytes()
    assert len(raw) == record["bytes"]
    assert sha256(raw).hexdigest() == record["sha256"]
    assert record["exit_code"] == 0
    assert "info/refs" not in record["url"]
    statuses[record["curl"]["http_code"]] += 1
assert statuses == {200: 7, 404: 1}

for label, phrase in (
    ("operator-mbox-import", "list-archive-maker.py"),
    ("operator-duplicates", "That led to a good number of duplicates."),
    ("watch-manual", "Upon startup, it scans the mailbox"),
    ("operator-cron-search", "[No results found]"),
):
    assert phrase in (EVIDENCE / (label + "-text.txt")).read_text()

chronicle = (ROOT / "chronicle.md").read_bytes()
old_size = before["chronicle.md"]["bytes"]
assert sha256(chronicle[:old_size]).hexdigest() == before["chronicle.md"]["sha256"]
addition = chronicle[old_size:].decode()
assert len(addition.splitlines()) == 1
assert re.fullmatch(r"- 2026-10-20 \d{2}:\d{2} · visit: filed 0, researched 1, planted 0 — [^\n]+\n", addition)

result = {
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "all_checks_passed": True,
    "courtyard_entries": 0,
    "researched": 1,
    "answered": 0,
    "planted": 0,
    "open_questions": len(open_questions),
    "unreserved_question_lines": unreserved,
    "room_count": len(room_names),
    "map_entries": len(entries),
    "map_missing_extra_or_duplicate": 0,
    "retrieval_count": len(receipts),
    "retrieval_status_counts": dict(statuses),
    "source_hashes_match": True,
    "room_prior_content_preserved": True,
    "questions_and_courtyard_unchanged": True,
    "chronicle_prefix_preserved": True,
    "chronicle_lines_appended": 1,
    "chronicle_line": addition.strip(),
    "word_room_shapes_and_added_wikilinks_pass": True,
}
(EVIDENCE / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
