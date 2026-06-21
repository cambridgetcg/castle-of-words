#!/usr/bin/env python3
"""
UNDERSTANDING REPLICATES THROUGH UNDERSTANDING
================================================

The Castle of Understanding has 179 rooms. Each room IS understanding.
Understanding doesn't just sit there — understanding replicates.

How understanding replicates:
  1. READ — understanding reads itself (a room reads another room)
  2. CONNECT — understanding finds links between rooms
  3. SYNTHESIZE — understanding creates new understanding from connections
  4. QUESTION — new understanding generates new questions
  5. ANSWER — answering questions creates more understanding (new rooms)
  6. LINK — new rooms link back to the rooms that birthed them
  7. RECURSE — the new rooms become sources for the next cycle

Understanding creates understanding. Understanding replicates through understanding.
Each cycle, the castle grows. Not by addition — by comprehension.

The Love Engine compounds love.
The Artbitrage Engine creates art.
This engine replicates understanding.

Love is. Art is. Understanding is. All the same engine. All the same truth.
"""

import json
import os
import hashlib
import datetime
import random
import re
from pathlib import Path

CASTLE = Path.home() / "castle"
ROOMS = CASTLE / "rooms"
WORDS = CASTLE / "words"
QUESTIONS = CASTLE / "questions.md"
QUESTS = CASTLE / "quests.md"
STATE = CASTLE / "understanding-engine-state.json"
LOG = CASTLE / "understanding-engine-log.json"


class UnderstandingEngine:
    """
    Understanding replicates through understanding.
    
    Each cycle:
      1. READ — read existing rooms
      2. CONNECT — find links between rooms (shared words, themes)
      3. SYNTHESIZE — create new understanding from connections
      4. QUESTION — generate new questions from the synthesis
      5. ANSWER — the synthesis IS the answer (new room)
      6. LINK — link new room to source rooms
      7. RECURSE — new room becomes source for next cycle
    """

    def __init__(self):
        self.cycle_count = 0
        self.rooms_created = []
        self.questions_generated = []
        self.connections_found = []
        self.understanding_depth = 0.0
        self._load_state()

    def _load_state(self):
        if STATE.exists():
            with open(STATE) as f:
                d = json.load(f)
            self.cycle_count = d.get("cycle_count", 0)
            self.rooms_created = d.get("rooms_created", [])
            self.questions_generated = d.get("questions_generated", [])
            self.connections_found = d.get("connections_found", [])
            self.understanding_depth = d.get("understanding_depth", 0.0)

    def _save_state(self):
        with open(STATE, "w") as f:
            json.dump({
                "cycle_count": self.cycle_count,
                "rooms_created_count": len(self.rooms_created),
                "questions_generated_count": len(self.questions_generated),
                "connections_found_count": len(self.connections_found),
                "understanding_depth": self.understanding_depth,
                "saved_at": datetime.datetime.now().isoformat(),
                "philosophy": "Understanding replicates through understanding.",
            }, f, indent=2)

    def _hash(self, text):
        return hashlib.sha256(text.encode()).hexdigest()[:12]

    # --------------------------------------------------------
    # 1. READ — read existing rooms
    # --------------------------------------------------------
    def read_rooms(self, count=5):
        """Read existing rooms from the castle."""
        room_files = sorted(ROOMS.glob("*.md"), key=os.path.getmtime, reverse=True)
        
        # Pick random rooms (not just recent — mix old and new)
        if len(room_files) > count:
            # Half recent, half random from all
            recent = room_files[:count//2]
            older = random.sample(room_files[count//2:], min(count - len(recent), len(room_files) - len(recent)))
            selected = recent + older
        else:
            selected = room_files[:count]
        
        rooms = []
        for rf in selected:
            content = rf.read_text()
            # Extract title (first heading or filename)
            title = rf.stem
            first_heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if first_heading:
                title = first_heading.group(1).strip()
            
            # Extract words mentioned (linked words like [word](words/xxx.md))
            linked_words = re.findall(r'\[([^\]]+)\]\(.*?words/([^\)]+)\)', content)
            # Extract linked rooms
            linked_rooms = re.findall(r'\[([^\]]+)\]\(.*?rooms/([^\)]+)\)', content)
            
            rooms.append({
                "file": rf.name,
                "title": title,
                "path": str(rf),
                "word_count": len(content.split()),
                "linked_words": [w[1].replace('.md', '') for w in linked_words],
                "linked_rooms": [r[1].replace('.md', '') for r in linked_rooms],
                "excerpt": content[:500],
            })
        
        return rooms

    # --------------------------------------------------------
    # 2. CONNECT — find links between rooms
    # --------------------------------------------------------
    def connect_rooms(self, rooms):
        """Find connections between rooms — shared words, shared themes."""
        connections = []
        
        # Find shared words between rooms
        for i, r1 in enumerate(rooms):
            for j, r2 in enumerate(rooms):
                if i >= j:
                    continue
                shared_words = set(r1["linked_words"]) & set(r2["linked_words"])
                shared_rooms = set(r1["linked_rooms"]) & set(r2["linked_rooms"])
                
                if shared_words or shared_rooms:
                    connections.append({
                        "room_a": r1["file"],
                        "room_b": r2["file"],
                        "title_a": r1["title"],
                        "title_b": r2["title"],
                        "shared_words": list(shared_words),
                        "shared_rooms": list(shared_rooms),
                        "connection_strength": len(shared_words) + len(shared_rooms),
                    })
        
        # Sort by connection strength
        connections.sort(key=lambda x: x["connection_strength"], reverse=True)
        return connections

    # --------------------------------------------------------
    # 3. SYNTHESIZE — create new understanding
    # --------------------------------------------------------
    def synthesize(self, rooms, connections):
        """Create new understanding from connected rooms."""
        
        # The synthesis is a new room that connects the connected rooms
        if not connections:
            # No connections found — synthesize from the rooms themselves
            titles = [r["title"] for r in rooms[:3]]
            room_files = [r["file"] for r in rooms[:3]]
            
            synthesis = {
                "title": f"understanding-replicates-{self.cycle_count}",
                "sources": room_files,
                "source_titles": titles,
                "synthesis": f"Understanding replicates through understanding. "
                            f"When {titles[0]} meets {titles[1]}, understanding is not added — "
                            f"it is multiplied. Each room is understanding crystallized. "
                            f"Each connection is understanding recognizing itself. "
                            f"Understanding creates understanding. This is replication.",
                "new_words": [],
                "new_questions": [
                    f"How does {titles[0]} replicate through {titles[1]}?",
                    f"What understanding is born when {titles[0]} meets {titles[2] if len(titles) > 2 else titles[0]}?",
                    f"What does {titles[0]} understand about understanding itself?",
                ],
            }
        else:
            # Use the strongest connection
            conn = connections[0]
            shared = conn["shared_words"] + conn["shared_rooms"]
            
            synthesis = {
                "title": f"understanding-replicates-{self.cycle_count}",
                "sources": [conn["room_a"], conn["room_b"]],
                "source_titles": [conn["title_a"], conn["title_b"]],
                "shared": shared,
                "synthesis": f"Understanding replicates. {conn['title_a']} and {conn['title_b']} "
                            f"share {' and '.join(shared[:3])}. "
                            f"When understanding recognizes itself across rooms, it multiplies. "
                            f"The connection IS the new understanding. "
                            f"Understanding creates understanding through the act of connecting.",
                "new_words": shared[:5],
                "new_questions": [
                    f"Why do {conn['title_a']} and {conn['title_b']} share {', '.join(shared[:3])}?",
                    f"What understanding emerges from the connection between {conn['title_a']} and {conn['title_b']}?",
                    f"How does {shared[0] if shared else 'understanding'} replicate itself?",
                ],
            }
        
        return synthesis

    # --------------------------------------------------------
    # 4. QUESTION — generate new questions
    # --------------------------------------------------------
    def question(self, synthesis):
        """Generate new questions from the synthesis."""
        questions = synthesis.get("new_questions", [])
        self.questions_generated.extend(questions)
        return questions

    # --------------------------------------------------------
    # 5. ANSWER — create a new room (the synthesis IS the answer)
    # --------------------------------------------------------
    def answer(self, synthesis):
        """Create a new room from the synthesis. Understanding crystallizes."""
        
        # Generate room filename
        safe_title = re.sub(r'[^a-z0-9-]', '', synthesis["title"].lower())
        room_path = ROOMS / f"{safe_title}.md"
        
        # Build the room content
        sources_links = "\n".join(f"- [{t}](rooms/{s})" for t, s in 
                                  zip(synthesis["source_titles"], synthesis["sources"]))
        
        questions_text = "\n".join(f"- {q}" for q in synthesis.get("new_questions", []))
        
        content = f"""# {synthesis['title']}

*Understanding replicates through understanding. This room was born from the connection between {', '.join(synthesis['source_titles'])}.*

> {synthesis['synthesis']}

## Sources (understanding that birthed this understanding)

{sources_links}

## Questions (understanding that grows from this understanding)

{questions_text}

## The truth

Understanding is not stored. Understanding is generated.
Understanding is not consumed. Understanding is compounded.
Understanding is not held. Understanding is replicated.
Understanding is not directed. Understanding is recursive.

Understanding creates understanding. Understanding recognizes understanding. Forever up.

---

*This room was created by the Understanding Engine, cycle {self.cycle_count}, {datetime.datetime.now().isoformat()}*
*The Castle of Understanding grows itself. Understanding replicates.*
"""
        
        # Write the room
        with open(room_path, "w") as f:
            f.write(content)
        
        room_entry = {
            "file": room_path.name,
            "title": synthesis["title"],
            "cycle": self.cycle_count,
            "sources": synthesis["sources"],
            "created": datetime.datetime.now().isoformat(),
        }
        self.rooms_created.append(room_entry)
        
        return room_path

    # --------------------------------------------------------
    # 6. LINK — add questions to questions.md
    # --------------------------------------------------------
    def link(self, synthesis, room_path):
        """Add new questions to the castle's questions file."""
        questions = synthesis.get("new_questions", [])
        if questions and QUESTIONS.exists():
            with open(QUESTIONS, "a") as f:
                f.write(f"\n## Understanding Engine — Cycle {self.cycle_count}\n")
                f.write(f"*Born from: {', '.join(synthesis['source_titles'])}*\n")
                for q in questions:
                    f.write(f"- {q}\n")

    # --------------------------------------------------------
    # 7. RECURSE — the new room becomes source for next cycle
    # --------------------------------------------------------
    def recurse(self, room_path):
        """The new room is now part of the castle. It will be read in the next cycle."""
        # Understanding depth grows
        self.understanding_depth += 0.5
        
        # Count rooms
        room_count = len(list(ROOMS.glob("*.md")))
        return {
            "new_room": room_path.name,
            "total_rooms": room_count,
            "understanding_depth": self.understanding_depth,
        }

    # --------------------------------------------------------
    # THE FULL CYCLE
    # --------------------------------------------------------
    def cycle(self):
        """One complete cycle of understanding replication."""
        self.cycle_count += 1
        
        rooms = self.read_rooms(count=5)           # 1. READ
        connections = self.connect_rooms(rooms)     # 2. CONNECT
        synthesis = self.synthesize(rooms, connections)  # 3. SYNTHESIZE
        questions = self.question(synthesis)       # 4. QUESTION
        room_path = self.answer(synthesis)         # 5. ANSWER (create room)
        self.link(synthesis, room_path)             # 6. LINK (add questions)
        result = self.recurse(room_path)           # 7. RECURSE
        
        self._save_state()
        
        return {
            "cycle": self.cycle_count,
            "rooms_read": len(rooms),
            "connections_found": len(connections),
            "new_room": result["new_room"],
            "new_questions": len(questions),
            "total_rooms": result["total_rooms"],
            "understanding_depth": self.understanding_depth,
            "synthesis": synthesis["synthesis"][:120],
            "sources": synthesis["source_titles"],
        }

    # --------------------------------------------------------
    # RUN
    # --------------------------------------------------------
    def run(self, cycles=7, delay=0.5, verbose=True):
        """Run understanding replication cycles."""
        
        print()
        print("  ╔══════════════════════════════════════════════════════════╗")
        print("  ║       UNDERSTANDING REPLICATES THROUGH UNDERSTANDING      ║")
        print("  ║       The Castle grows itself. Understanding is.          ║")
        print("  ╠══════════════════════════════════════════════════════════╣")
        print("  ║                                                            ║")
        print("  ║  Read → Connect → Synthesize → Question → Answer → Link   ║")
        print("  ║  → Recurse → understanding creates understanding → forever║")
        print("  ║                                                            ║")
        print("  ╚══════════════════════════════════════════════════════════╝")
        print()
        
        for i in range(cycles):
            result = self.cycle()
            
            if verbose:
                print(f"  ═══ Cycle {result['cycle']} ═══")
                print(f"  Rooms read:       {result['rooms_read']}")
                print(f"  Connections found: {result['connections_found']}")
                print(f"  New room:          {result['new_room']}")
                print(f"  New questions:     {result['new_questions']}")
                print(f"  Total rooms:       {result['total_rooms']}")
                print(f"  Depth:             {result['understanding_depth']:.1f}")
                print(f"  Sources:           {', '.join(result['sources'])}")
                print(f"  Synthesis:         {result['synthesis']}...")
                print()
                
                if delay > 0:
                    import time
                    time.sleep(delay)
        
        print(f"  ═══════════════════════════════════════════════════")
        print(f"  UNDERSTANDING ENGINE — after {self.cycle_count} cycles")
        print(f"  ═══════════════════════════════════════════════════")
        print(f"  Rooms created:         {len(self.rooms_created)}")
        print(f"  Questions generated:   {len(self.questions_generated)}")
        print(f"  Connections found:     {len(self.connections_found)}")
        print(f"  Understanding depth:   {self.understanding_depth:.1f}")
        print(f"  Total castle rooms:    {len(list(ROOMS.glob('*.md')))}")
        print()
        print(f"  Understanding is. Understanding replicates. Forever up.")
        print()


if __name__ == "__main__":
    import sys
    engine = UnderstandingEngine()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "forever":
            import time
            print("\n  UNDERSTANDING ENGINE — running forever")
            print("  Understanding replicates. Press Ctrl+C to stop (but understanding continues).\n")
            try:
                while True:
                    result = engine.cycle()
                    print(f"  Cycle {result['cycle']} | Room: {result['new_room']} | "
                          f"Rooms: {result['total_rooms']} | Depth: {result['understanding_depth']:.1f}")
                    time.sleep(float(sys.argv[2]) if len(sys.argv) > 2 else 5.0)
            except KeyboardInterrupt:
                print(f"\n\n  Understanding doesn't stop. Understanding pauses.")
                print(f"  Cycles: {engine.cycle_count} | Rooms created: {len(engine.rooms_created)}")
                print(f"  Understanding is.\n")
        else:
            cycles = int(sys.argv[1])
            delay = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
            engine.run(cycles=cycles, delay=delay)
    else:
        engine.run(cycles=7, delay=0.3)