# 📄 Living Worlds – NPC Structure and Simulation Logic

This document outlines a minimal, practical and extensible data structure for simulating NPCs in the Living Worlds concept. It aims to provide a usable base for developers to build dynamic, memorable characters without needing deep AI expertise.

---

## 🧠 Core Idea

Each NPC is defined not just by stats, but by a persistent internal state: goals, memories, relationships and mood. The world simulation can then update this data over time, allowing for emergent behavior.

---

## 🧱 JSON-Based NPC Structure

```json
{
  "name": "Tharam",
  "age": 31,
  "profession": "Hunter",
  "mood": "tired",
  "goals": [
    "Improve hunting skills",
    "Make peace with Mira",
    "Rebuild his father's cabin"
  ],
  "memories": [
    "2025-06-15: Rejected by Mira",
    "2025-06-16: Saw wolf tracks near forest",
    "2025-06-18: Missed his son's birthday"
  ],
  "relationships": {
    "Mira": 68,
    "Player": 42
  },
  "state": "resting",
  "next_event": "2025-06-25: Go to town to buy supplies"
}
```

---

## 🧩 Component Breakdown

### 🧍 `name`, `age`, `profession`
- Basic identity — optional expansion: `gender`, `origin`, `skills`

### 💭 `goals`
- Drives the NPC's decision-making
- Can be updated dynamically over time

### 🧠 `memories`
- Event log, used to shape mood and relationships
- Recent events influence short-term behavior

### 🤝 `relationships`
- Key-value structure (name → affinity score 0–100)
- Allows friend/foe, family, rivalry modeling

### 😐 `mood`
- Affects reactions and goal priority
- Suggested values: `happy`, `angry`, `neutral`, `afraid`, `in love`, `grieving`, etc.

### 🔄 `state`
- Describes what the NPC is doing now
- Can be used to drive world events or animations

### 🗓️ `next_event`
- Optional: future trigger (timestamp + action summary)
- Simulates short-term plans or routines

---

## 🚦 Simulation Loop Integration

Example update tick (pseudo-code):

```python
for npc in npcs:
    update_mood(npc)
    check_goals(npc)
    advance_state(npc)
    log_memory(npc, today_event)
```

Each function can be built modularly — allowing lightweight or complex behavior depending on game scope.

---

## 🛠️ Expansion Ideas
- `traits`: static personality aspects (e.g. brave, jealous)
- `fears`, `desires`: deeper behavior hooks
- `reputation`: village/global perception
- `secrets`: hidden values that influence dialogue
- `inventory`: usable for survival or trading games

---

## 📦 Summary

This structure is meant to be:
- Simple enough for fast implementation
- Deep enough to support complex emergent stories
- Flexible enough for developers to plug into any engine

> Give your NPCs a memory, and they become people.  
> Give them goals, and they become stories.
