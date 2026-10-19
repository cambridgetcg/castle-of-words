"""Read-only checks for this bounded tending; pass --closed after the chronicle append."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BEFORE = json.loads((HERE / "before.json").read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    assert path.resolve().is_relative_to(ROOT), path
    return path.read_text()


def room_refs(text):
    result = {
        s.split("|", 1)[0].split("#", 1)[0].rsplit("/", 1)[-1].removesuffix(".md")
        for s in re.findall(r"\[\[([^\]]+)\]\]", text)
    }
    result.update(
        Path(s.split("#", 1)[0]).stem
        for s in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
        if "://" not in s
    )
    return result & room_names


# Removing only the planned additions must recover every original byte.
room_edits = {
    "friction-decides": (1, False),
    "what-the-gaps-can-say": (2, False),
    "counting-the-shapes": (2, False),
    "smooth-or-thresholded-understanding": (1, True),
    "data-dictionary-honesty": (1, True),
    "cbt-openness-trait": (1, True),
}
originals = {}
added_blocks = []
for name, (count, was_inline) in room_edits.items():
    path = ROOT / "rooms" / (name + ".md")
    text = read(path)
    prefix, marker, rest = text.partition("Links:\n")
    assert marker and text.count("Links:\n") == 1, name
    lines = rest.splitlines(keepends=True)
    added = lines[:count]
    assert len(added) == count and all(s.startswith("- ") for s in added), name
    remainder = "".join(lines[count:])
    if was_inline:
        assert remainder.startswith("\n"), name
        original = prefix + "Links: " + remainder[1:]
    else:
        original = prefix + marker + remainder
    relative = path.relative_to(ROOT).as_posix()
    assert digest(original.encode()) == BEFORE["before_sha256"][relative], relative
    originals[name] = original
    added_blocks.append((path, "".join(added)))

old_map_lines = {
    "cbt-openness-trait": "- [cbt-openness-trait](rooms/cbt-openness-trait.md) — the seam is confirmed unbuilt: CBT was in the Roberts meta-analysis (d=.37) but no study isolated openness as a target, and the studies that moved it went through action not appraisal (built 2026-06-18)",
    "cheapest-cbt-design": "- [cheapest-cbt-design](rooms/cheapest-cbt-design.md) — someone already ran nearly the cheapest design: Kennair et al. 2021 found openness rose significantly in a CBT RCT with NEO-PI-R pre/post; the cheapest clean addition is a follow-up (built 2026-06-18)",
    "smooth-or-thresholded-understanding": "- [smooth-or-thresholded-understanding](rooms/smooth-or-thresholded-understanding.md) — does understanding accumulate continuously or click into place: the model that wins is the one whose shape matches the nature of the thing, and the engine must look for breaks not slopes (built 2026-07-05)",
}
gate = read(ROOT / "gate.md")
restored_gate = gate
for name, old in old_map_lines.items():
    pattern = r"(?m)^- \[" + re.escape(name) + r"\].*$"
    match = re.findall(pattern, restored_gate)
    assert len(match) == 1 and "summary trued 2026-10-19" in match[0], name
    restored_gate = restored_gate.replace(match[0], old, 1)
assert digest(restored_gate.encode()) == BEFORE["before_sha256"]["gate.md"]

room_paths = list((ROOT / "rooms").glob("*.md"))
room_names = {p.stem for p in room_paths}
map_text = gate.split("## Map\n", 1)[1].split("\n## ", 1)[0]
entries = re.findall(r"\[[^\]]*\]\((rooms/[^)]+\.md)\)", map_text)
expected_entries = {p.relative_to(ROOT).as_posix() for p in room_paths}
assert set(entries) == expected_entries
assert len(entries) == len(set(entries)) == BEFORE["room_count"]
map_rows = [s for s in map_text.splitlines() if s.strip() and not s.startswith("*(")]
assert len(map_rows) == len(entries)
assert all(re.fullmatch(r"- \[([^]]+)\]\(rooms/\1\.md\) — .+", s) for s in map_rows)

old_pairs, new_pairs = set(), set()
for path in room_paths:
    current = read(path)
    old = originals.get(path.stem, current)
    for text, target in ((old, old_pairs), (current, new_pairs)):
        target.update(tuple(sorted((path.stem, other))) for other in room_refs(text) if other != path.stem)
expected_pairs = {tuple(sorted(pair)) for pair in BEFORE["new_room_pairs"]}
assert new_pairs - old_pairs == expected_pairs
assert not old_pairs - new_pairs
for a, b in BEFORE["new_room_pairs"]:
    for source, target in ((a, b), (b, a)):
        section = read(ROOT / "rooms" / (source + ".md")).split("Links:\n", 1)[1].split("\n## ", 1)[0]
        assert f"]({target}.md)" in section

word = ROOT / "words/selection-bias.md"
word_text = read(word)
assert word_text.startswith("# selection-bias\n\nSelection bias is ")
assert "\nLinks:\n" in word_text and "\n#" not in word_text.split("\nLinks:\n", 1)[1]
added_blocks.append((word, word_text))
link_count = 0
for path, block in added_blocks:
    for ref in re.findall(r"\[\[([^\]]+)\]\]", block):
        name = ref.split("|", 1)[0].split("#", 1)[0]
        candidates = [ROOT / (name + ".md"), ROOT / "rooms" / (name + ".md"), ROOT / "words" / (name + ".md")]
        assert any(p.resolve().is_relative_to(ROOT) and p.is_file() for p in candidates), (path, ref)
        link_count += 1
    for ref in re.findall(r"\[[^\]]*\]\(([^)]+)\)", block):
        if "://" in ref:
            continue
        target = (path.parent / ref.split("#", 1)[0]).resolve()
        assert target.is_relative_to(ROOT) and target.is_file(), (path, ref)
        link_count += 1

# The protected machinery is hashed, never edited or executed.
garden = {}
for path in sorted((ROOT / "garden").rglob("*")):
    relative = path.relative_to(ROOT).as_posix()
    if path.is_symlink():
        garden[relative] = "symlink:" + str(path.readlink())
    elif path.is_file():
        assert path.resolve().is_relative_to(ROOT)
        garden[relative] = digest(path.read_bytes())
assert len(garden) == BEFORE["garden_file_count"]
assert digest(json.dumps(garden, sort_keys=True).encode()) == BEFORE["garden_tree_sha256"]

chronicle = read(ROOT / "chronicle.md")
closed = "--closed" in sys.argv
if closed:
    lines = chronicle.splitlines(keepends=True)
    assert digest("".join(lines[:-1]).encode()) == BEFORE["before_sha256"]["chronicle.md"]
    assert re.fullmatch(r"- 2026-10-19 \d{2}:\d{2} · tended: linked 3 pairs, laid 1 word-bricks, .+\n", lines[-1])
else:
    assert digest(chronicle.encode()) == BEFORE["before_sha256"]["chronicle.md"]

print(json.dumps({
    "checked_at": datetime.datetime.now().astimezone().isoformat(),
    "passed": True,
    "new_room_pairs": sorted(expected_pairs),
    "new_pair_count": len(expected_pairs),
    "new_pairs_reciprocal": True,
    "existing_return_link_repaired": BEFORE["existing_pair_return_to_repair"],
    "new_word_bricks": BEFORE["new_words"],
    "new_local_link_occurrences_checked": link_count,
    "map_rooms": len(entries),
    "map_missing_stale_or_duplicate_entries": 0,
    "map_summaries_changed": len(old_map_lines),
    "original_bytes_preserved_outside_planned_edits": True,
    "garden_files_unchanged": len(garden),
    "chronicle_closed": closed,
    "limits": "Structural and change-scope verification; not a scientific revalidation of every room or Map summary."
}, ensure_ascii=False, indent=2))
