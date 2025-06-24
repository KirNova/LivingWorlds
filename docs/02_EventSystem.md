# 📄 Living Worlds – Event System Design

This document describes the concept and technical structure for a simple but powerful event system within the Living Worlds simulation framework.

Events drive world change — they provide narrative tension, alter NPC behavior, and allow for emergent, dynamic storytelling.

---

## 🎯 Goals of the Event System

- Simulate meaningful changes in the world
- Allow NPCs to trigger, react to, or ignore events
- Allow events to chain into further consequences
- Be data-driven and transparent for devs

---

## 🧪 Event Structure (Example in JSON)

```json
{
  "id": "fire_001",
  "type": "disaster",
  "timestamp": "2025-07-01",
  "location": "Village Center",
  "description": "A fire broke out during the summer festival.",
  "participants": ["Tharam", "Mira"],
  "effects": {
    "Tharam": {
      "injury": true,
      "mood": "traumatized"
    },
    "Mira": {
      "fear": 25,
      "memory": "2025-07-01: Escaped fire in Village Center"
    }
  },
  "consequences": [
    "Tavern destroyed",
    "Rumors spread about sabotage",
    "Festival permanently canceled"
  ]
}
```

---

## 🧩 Key Components

### 🔖 `id`, `type`, `timestamp`, `location`
- Unique identifiers and context
- Can be used to track event history

### 👥 `participants`
- NPCs directly affected or involved

### 🌀 `effects`
- Customizable logic per participant
- Can alter mood, health, relationships, etc.

### 🌪️ `consequences`
- World-level changes or follow-up triggers
- Can feed new events or modify global state

---

## 🔁 Event Trigger Types

| Trigger Type | Example |
|--------------|---------|
| Time-based   | "Festival begins every summer" |
| Conditional  | "If food < 20%, trigger famine" |
| NPC-based    | "If Mira breaks up with Tharam → rumor event" |
| Randomized   | "10% chance of wolf attack in forest" |
| External     | "Player kills king → succession crisis" |

---

## 🔄 Reaction Flow

1. Event is created or triggered
2. System checks which NPCs are affected
3. NPCs process effects (update mood, memories, etc.)
4. Event consequences applied (change map, spawn new events)
5. Optional: system logs to history

---

## 🔧 Where to Store Events

- JSON files (small games)
- Local SQLite (mid-level world)
- Server-based DB (MMO-style persistent worlds)

---

## 📦 Summary

Events make the world breathe.

They’re more than story tools — they are **mechanical triggers for emotion, loss, growth, and reaction**.

By combining event triggers, effects, and consequences, you can simulate:

- Revolutions
- Love stories
- Plagues
- Festival dramas
- Village gossip

All without scripting a single plotline.

> Let the world write its own history. You just light the first spark.
