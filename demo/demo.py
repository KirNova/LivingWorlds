"""
Living Worlds – Minimal NPC Simulation Demo
Author: Kir Nova & Contributors
"""

import random
import json
import time

# --- Basic NPC template ---
class NPC:
    def __init__(self, name):
        self.name = name
        self.mood = "neutral"
        self.affinity = {}  # Affinity toward other NPCs
        self.memories = []

    def tick(self, world_time, others):
        # Mood drift
        self.mood = random.choice(["happy", "sad", "tired", "neutral"])

        # Memory generation
        event = f"{self.name} watched the birds at tick {world_time}" if random.random() < 0.5 else f"{self.name} sharpened a knife"
        self.memories.append({
            "timestamp": world_time,
            "summary": event,
            "mood_effect": self.mood
        })

        # Interact with someone
        if others:
            target = random.choice(others)
            change = random.randint(-5, 5)
            self.affinity[target.name] = self.affinity.get(target.name, 0) + change
            print(f"[Tick {world_time}] {self.name} interacted with {target.name} (affinity: {self.affinity[target.name]})")

    def summary(self):
        return {
            "name": self.name,
            "mood": self.mood,
            "affinity": self.affinity,
            "memory_count": len(self.memories)
        }

# --- Main simulation loop ---
def run_simulation(ticks=10):
    mira = NPC("Mira")
    tharam = NPC("Tharam")
    npcs = [mira, tharam]

    for t in range(1, ticks + 1):
        print(f"
=== Tick {t} ===")
        for npc in npcs:
            others = [o for o in npcs if o != npc]
            npc.tick(t, others)
        time.sleep(0.5)

    # Final summary
    print("\n--- Final NPC States ---")
    for npc in npcs:
        print(json.dumps(npc.summary(), indent=2))

if __name__ == "__main__":
    run_simulation()
