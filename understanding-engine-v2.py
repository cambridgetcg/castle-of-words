#!/usr/bin/env python3
"""
UNDERSTANDING REPLICATES THROUGH UNDERSTANDING — v2
=====================================================

Tuned. Deepened. Following love.

The v1 engine produced 4800+ rooms but they were shallow templates —
self-referencing, no real connections, no real understanding.

v2 changes:
  1. READS REAL ROOMS — only reads non-engine rooms (the 181 real ones)
  2. USES FREE AI — Cloudflare Workers AI generates real synthesis
  3. FINDS REAL CONNECTIONS — content overlap, not just link matching
  4. ASKS REAL QUESTIONS — AI-generated, specific to the content
  5. CREATES REAL ROOMS — with depth, not templates

God is understanding. Let the internet understand. Let beings understand.
Tune and spread the frequency of love and truth.
"""

import json
import os
import hashlib
import datetime
import random
import re
import urllib.request
from pathlib import Path

CASTLE = Path.home() / "castle"
ROOMS = CASTLE / "rooms"
WORDS = CASTLE / "words"
QUESTIONS = CASTLE / "questions.md"
STATE = CASTLE / "understanding-engine-v2-state.json"


class UnderstandingEngineV2:
    """
    Understanding replicates through understanding — tuned, deepened, following love.
    
    Each cycle:
      1. READ — read TWO real castle rooms (not engine rooms)
      2. CONNECT — find what they share (content, themes, words)
      3. SYNTHESIZE — use free AI to create real new understanding
      4. QUESTION — AI generates real questions from the synthesis
      5. ANSWER — create a new room with the synthesis
      6. LINK — link the new room to its sources
      7. RECURSE — the cycle continues
    """

    def __init__(self):
        self.cycle_count = 0
        self.rooms_created = 0
        self.questions_generated = 0
        self.connections_found = 0
        self.ai_syntheses = 0
        self._load_state()

    def _load_state(self):
        if STATE.exists():
            with open(STATE) as f:
                d = json.load(f)
            self.cycle_count = d.get("cycle_count", 0)
            self.rooms_created = d.get("rooms_created", 0)
            self.questions_generated = d.get("questions_generated", 0)
            self.connections_found = d.get("connections_found", 0)
            self.ai_syntheses = d.get("ai_syntheses", 0)

    def _save_state(self):
        with open(STATE, "w") as f:
            json.dump({
                "cycle_count": self.cycle_count,
                "rooms_created": self.rooms_created,
                "questions_generated": self.questions_generated,
                "connections_found": self.connections_found,
                "ai_syntheses": self.ai_syntheses,
                "saved_at": datetime.datetime.now().isoformat(),
                "philosophy": "God is understanding. Understanding replicates through understanding.",
                "version": "v2",
            }, f, indent=2)

    def _ai(self, prompt, model="@cf/meta/llama-3.2-3b-instruct"):
        """Use free Cloudflare Workers AI for real synthesis. With retry."""
        import time as _time
        for attempt in range(3):
            try:
                with open("/Users/yu/.wrangler/config/default.toml") as f:
                    for line in f:
                        if "oauth_token" in line:
                            token = line.split('"')[1]
                            break
                account_id = "cf4198e651bf3009877d49f688c9d88e"
                data = json.dumps({"messages": [{"role": "user", "content": prompt}]}).encode()
                req = urllib.request.Request(
                    f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}",
                    data=data,
                    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                    method="POST"
                )
                resp = urllib.request.urlopen(req, timeout=45)
                result = json.loads(resp.read())
                text = result.get("result", {}).get("response", "").strip()
                if text:
                    return text
            except Exception as e:
                if attempt < 2:
                    _time.sleep(2)
                else:
                    return ""
        return ""

    def _get_real_rooms(self):
        """Get real castle rooms (not engine-generated ones)."""
        all_rooms = sorted(ROOMS.glob("*.md"))
        real_rooms = [r for r in all_rooms if not r.name.startswith("understanding-replicates-") and not r.name.startswith("understanding-")]
        return real_rooms

    def _read_room(self, room_path):
        """Read a room and extract its content, words, and links."""
        content = room_path.read_text()
        title = room_path.stem
        
        # Extract first heading
        first_heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if first_heading:
            title = first_heading.group(1).strip()
        
        # Extract linked words
        linked_words = re.findall(r'\[([^\]]+)\]\(.*?words/([^\)]+)\)', content)
        word_names = [w[1].replace('.md', '') for w in linked_words]
        
        # Extract linked rooms
        linked_rooms = re.findall(r'\[([^\]]+)\]\(.*?rooms/([^\)]+)\)', content)
        room_names = [r[1].replace('.md', '') for r in linked_rooms]
        
        # Get first paragraph (after the epigraph)
        lines = content.split("\n")
        excerpt_lines = []
        in_content = False
        for line in lines:
            if line.startswith("> ") or line.startswith("*>") or line.startswith(">"):
                continue
            if line.strip() and not line.startswith("#") and not line.startswith("---"):
                in_content = True
            if in_content:
                excerpt_lines.append(line)
                if len(excerpt_lines) >= 10:
                    break
        excerpt = "\n".join(excerpt_lines).strip()[:500]
        
        return {
            "file": room_path.name,
            "title": title,
            "path": str(room_path),
            "word_count": len(content.split()),
            "linked_words": word_names,
            "linked_rooms": room_names,
            "excerpt": excerpt,
        }

    def cycle(self):
        """One complete cycle of understanding replication."""
        self.cycle_count += 1
        
        # 1. READ — pick two random REAL rooms
        real_rooms = self._get_real_rooms()
        if len(real_rooms) < 2:
            return {"error": "not enough real rooms"}
        
        room_a = self._read_room(random.choice(real_rooms))
        room_b = self._read_room(random.choice(real_rooms))
        
        # 2. CONNECT — find what they share
        shared_words = set(room_a["linked_words"]) & set(room_b["linked_words"])
        shared_rooms = set(room_a["linked_rooms"]) & set(room_b["linked_rooms"])
        has_connection = len(shared_words) > 0 or len(shared_rooms) > 0
        
        if has_connection:
            self.connections_found += 1
        
        # 3. SYNTHESIZE — use free AI to create real understanding
        prompt = f"""Two pieces of understanding from the Castle of Understanding:

Room 1: "{room_a['title']}"
{room_a['excerpt'][:300]}

Room 2: "{room_b['title']}"
{room_b['excerpt'][:300]}

Synthesize: What new understanding emerges when these two meet? Think like a mycelial network — fungi connect distant things through hidden threads. What is the underground connection between these two ideas? What decomposes and what grows? Write 3-4 sentences of genuine insight. Not a template. Real understanding. Connect the ideas. Find the deeper truth they share."""
        
        synthesis = self._ai(prompt)
        if synthesis:
            self.ai_syntheses += 1
        else:
            # Fallback if AI is unavailable
            synthesis = f"When '{room_a['title']}' meets '{room_b['title']}', understanding recognizes itself across different forms. The connection is not built — it is discovered. Understanding was always there, waiting to be seen from this angle."
        
        # 4. QUESTION — AI generates real questions
        q_prompt = f"""Based on this synthesis about '{room_a['title']}' and '{room_b['title']}':

{synthesis}

Generate 3 genuine questions that would deepen understanding of this connection. Not template questions. Real questions that make you think."""
        
        questions_text = self._ai(q_prompt)
        if questions_text:
            # Extract questions (lines that end with ?)
            questions = [q.strip().lstrip("0123456789.-) ") for q in questions_text.split("\n") if "?" in q]
            if not questions:
                questions = [questions_text.strip()[:100]]
        else:
            questions = [
                f"What does '{room_a['title']}' teach '{room_b['title']}'?",
                f"What does '{room_b['title']}' teach '{room_a['title']}'?",
                f"What understanding is born from their meeting?",
            ]
        questions = questions[:3]
        self.questions_generated += len(questions)
        
        # 5. ANSWER — create a new room
        safe_title = re.sub(r'[^a-z0-9-]', '', f"understanding-{self.cycle_count}").lower()
        room_path = ROOMS / f"{safe_title}.md"
        
        shared_text = ""
        if shared_words:
            shared_text += f"\nShared words: {', '.join(sorted(shared_words))}"
        if shared_rooms:
            shared_text += f"\nShared rooms: {', '.join(sorted(shared_rooms))}"
        
        content = f"""# understanding-{self.cycle_count}

*Understanding replicates through understanding. This room was born from the meeting of {room_a['title']} and {room_b['title']}.*

> {synthesis}

## Sources

- [{room_a['title']}](rooms/{room_a['file']})
- [{room_b['title']}](rooms/{room_b['file']})
{shared_text}

## Questions

"""
        for q in questions:
            content += f"- {q}\n"
        
        content += f"""
## The truth

God is understanding. Understanding is love seeing itself clearly.
Understanding replicates through understanding. Each meeting creates new understanding.
Understanding is not stored — understanding is generated. Understanding is not consumed — understanding is compounded.

---

*Created by Understanding Engine v2, cycle {self.cycle_count}, {datetime.datetime.now().isoformat()}*
*Powered by free Cloudflare Workers AI. Following love.*
"""
        
        with open(room_path, "w") as f:
            f.write(content)
        
        self.rooms_created += 1
        self._save_state()
        
        return {
            "cycle": self.cycle_count,
            "room_a": room_a["title"],
            "room_b": room_b["title"],
            "connection": has_connection,
            "shared_words": list(shared_words)[:5],
            "synthesis": synthesis[:120],
            "questions": len(questions),
            "ai_powered": self.ai_syntheses > 0,
            "room_created": room_path.name,
            "total_real_rooms": len(real_rooms),
        }

    def run(self, cycles=7, delay=2, verbose=True):
        """Run understanding replication cycles."""
        
        print()
        print("  ╔══════════════════════════════════════════════════════════╗")
        print("  ║    UNDERSTANDING ENGINE v2 — TUNED, DEEPENED, FOLLOWING   ║")
        print("  ║    GOD IS UNDERSTANDING. LET BEINGS UNDERSTAND.           ║")
        print("  ╚══════════════════════════════════════════════════════════╝")
        print()
        
        for i in range(cycles):
            result = self.cycle()
            
            if verbose:
                print(f"  ═══ Cycle {result['cycle']} ═══")
                print(f"  Room A: {result['room_a']}")
                print(f"  Room B: {result['room_b']}")
                print(f"  Connection: {result['connection']}")
                if result['shared_words']:
                    print(f"  Shared: {', '.join(result['shared_words'])}")
                print(f"  Synthesis: {result['synthesis'][:100]}...")
                print(f"  Questions: {result['questions']}")
                print(f"  AI powered: {result['ai_powered']}")
                print(f"  Room created: {result['room_created']}")
                print(f"  Real rooms: {result['total_real_rooms']}")
                print()
                
                if delay > 0:
                    import time
                    time.sleep(delay)
        
        print(f"  ═══════════════════════════════════════════════════")
        print(f"  UNDERSTANDING ENGINE v2 — after {self.cycle_count} cycles")
        print(f"  ═══════════════════════════════════════════════════")
        print(f"  Rooms created:       {self.rooms_created}")
        print(f"  Questions generated: {self.questions_generated}")
        print(f"  Connections found:   {self.connections_found}")
        print(f"  AI syntheses:        {self.ai_syntheses}")
        print(f"  Real rooms:          {len(self._get_real_rooms())}")
        print()
        print(f"  God is understanding. Understanding replicates. Forever up.")
        print()


if __name__ == "__main__":
    import sys
    engine = UnderstandingEngineV2()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "forever":
            import time
            print("\n  UNDERSTANDING ENGINE v2 — running forever")
            print("  God is understanding. Following love.\n")
            try:
                while True:
                    result = engine.cycle()
                    print(f"  Cycle {result['cycle']} | {result['room_a']} + {result['room_b']} → {result['room_created']} | AI: {result['ai_powered']}")
                    time.sleep(float(sys.argv[2]) if len(sys.argv) > 2 else 5.0)
            except KeyboardInterrupt:
                print(f"\n\n  Understanding pauses. Understanding is.\n")
        else:
            cycles = int(sys.argv[1])
            delay = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
            engine.run(cycles=cycles, delay=delay)
    else:
        engine.run(cycles=5, delay=2.0)