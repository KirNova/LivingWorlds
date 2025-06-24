# 🕒 Living Worlds – World Tick and Time Simulation

This document defines how the simulation of time ("ticks") works in the Living Worlds system. The goal is to simulate change — not just moments.

---

## 🔁 What is a Tick?

A **tick** is a single unit of time within the simulated world. It can represent:

- One minute
- One hour
- One day
- One season
- One generation

Depending on the scale of your world, you can define what a tick means and how often it occurs.

---

## ⏳ Recommended Tick Model

### For personal / village-scale simulation:
- **1 Tick = 1 Hour**
- 24 ticks per day
- Daily updates for NPC behavior, sleep, tasks, interactions

### For large-scale world simulation:
- **1 Tick = 1 Day**
- Seasonal changes every 90 ticks
- NPCs age, events resolve, relationships evolve

---

## 🔧 What Happens on a Tick?

| System Component | What Updates? |
|------------------|----------------|
| ⏰ Time / Calendar | World day, season, year |
| 👥 NPCs | Age, mood, routines, memory decay |
| 💬 Relationships | Decay/grow based on proximity & events |
| 🏘️ Village/World | Resources, building wear, rumors |
| 🔥 Events | Triggered or concluded |
| 🧠 AI Decisions | Re-evaluate goals or plans |
| 💾 Persistence | State saved (if applicable) |

---

## 💭 Example Tick Flow

```python
for npc in world.npcs:
    npc.age += 1/365  # Simulates one day
    npc.update_mood()
    npc.evaluate_goals()
    npc.log_memory("2025-07-02: Rain ruined the hunt")

world.check_events()
world.advance_season_if_needed()
save_world_state()
```

---

## 📥 Tick Input Sources

| Source | Use |
|--------|-----|
| ⌛ Passive (real-time clock) | Simulation runs continuously (e.g. every second = 1 tick) |
| ⏯️ Player-triggered | Tick only advances when the player acts (turn-based, paused) |
| 🧪 Batch simulation | Run 1000 ticks instantly for testing generations |
| 🔁 Hybrid | Active zones simulate in detail, others "fast-forward" |

---

## 📦 Saving and Loading

Every tick cycle should offer a "snapshot point" where:
- NPC states are saved
- World status is persisted
- Recent events are logged

For advanced simulations:
- Save states per zone
- Use delta-compression or per-season snapshots

---

## 🧠 Optional: "Tick Memory"

Let NPCs remember the number of ticks since:
- Last saw player
- Last fulfilled goal
- Last major emotional impact

This lets them say things like:
> *"You’ve been gone for 142 days... I thought you died."*

---

## 📌 Summary

Ticks are the heartbeat of the world.  
They turn static data into dynamic existence.

Design them carefully, and your game will never feel still again.

> In a living world, time is the only god.  
> Let it speak.
