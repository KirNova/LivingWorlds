# ❤️ Living Worlds – Relationship System

This document describes how NPCs form, evolve, and lose relationships — turning mere data into loyalty, rivalry, romance, betrayal, or grief.

---

## 🤝 Core Concept

Every NPC maintains a **relationship map** — a dynamic score and context for how they perceive other individuals.

---

## 🧩 Basic Structure (JSON)

```json
"relationships": {
  "Mira": {
    "affinity": 74,
    "tags": ["romantic", "protective"],
    "last_interaction": "2025-06-19",
    "memory_links": ["mem_134", "mem_1431"],
    "trust": 65,
    "fear": 0,
    "anger": 12
  },
  "Tharam": {
    "affinity": 42,
    "tags": ["ally"],
    "trust": 55,
    "rivalry": 22
  }
}
```

---

## 📈 Affinity Score

- Ranges from **-100 (pure hatred)** to **+100 (deep love)**
- Changes over time due to:
  - Shared or conflicting memories
  - Dialogue outcomes
  - Time decay (especially for distant NPCs)
  - World events (betrayal, rescue, war, etc.)

---

## 🏷️ Tags

Quick relationship descriptors:
- `family`, `romantic`, `mentor`, `enemy`, `lost`, `political`, `servant`, etc.
- Used to bias future decisions and dialogue

---

## ⚙️ Relationship Dynamics

| Action | Effect |
|--------|--------|
| Save from danger | +Trust, +Affinity, new memory |
| Insult or betray | -Trust, +Anger or +Rivalry |
| Time passes | Minor decay unless reinforced |
| Shared event | Aligns feelings, creates bond |
| Rumors / lies | May warp perception via hearsay |

---

## 💔 One-Sided Love, Fear, or Loyalty

The system allows **asymmetrical relationships**.

Example:
- NPC A loves NPC B → +100
- NPC B fears NPC A → -40

These imbalances cause emotional tension and complex behavior.

---

## 🧠 Memory-Based Reinforcement

Linking memories to relationships lets NPCs **remember why** they care or resent:

```json
"memory_links": ["mem_1431", "mem_1777"]
```

This also allows dynamic dialogue like:
> "After what you did at the river... I can’t trust you."

---

## 🕸️ Network Potential

With enough NPCs, you can simulate:
- Social alliances
- Religious cults
- Political factions
- Family trees
- Betrayal chains

You can visualize it as a **weighted relationship graph**.

---

## 🔄 Periodic Update Flow

1. Tick-based decay or drift
2. React to events affecting shared tags (e.g. "Tharam insulted Mira")
3. Create/merge/remove relationship entries
4. Use for mood/goal influences

---

## 📦 Summary

Relationships give **weight to decisions** and **stakes to events**.

They make an NPC cry at a funeral, fight beside an old friend, or walk away from a village they no longer believe in.

> A world without relationships is a world without memory.  
> And a world without memory... cannot tell a story.
