# 🧠 Living Worlds – Narrative Memory System

This document explains the concept of **Narrative Memory** — a key feature that lets NPCs not only remember, but **react** to past experiences and **tell their own evolving story**.

---

## 🧭 What is Narrative Memory?

A structured, timestamped log of **emotionally relevant events** in an NPC’s life.

Unlike raw event logs, narrative memories:

- Influence **mood**, **goals**, and **relationships**
- Can be accessed in **dialogue**
- Fade or grow stronger over time
- May be **rewritten** by trauma, magic, lies, or AI hallucination

---

## 🧱 Memory Structure (Example in JSON)

```json
{
  "id": "mem_1431",
  "timestamp": "2025-06-19",
  "type": "loss",
  "summary": "Watched Mira leave the village with no goodbye",
  "emotional_weight": 78,
  "mood_effect": "grief",
  "related_npcs": ["Mira"],
  "location": "South Gate",
  "public": false
}
```

---

## 🎭 Memory Categories

| Type | Examples |
|------|----------|
| `joy` | Marriage, birth, harvest, love |
| `fear` | Battle, betrayal, animal attack |
| `loss` | Death, abandonment, exile |
| `shame` | Failure, humiliation, rejected proposal |
| `hope` | Inspired by hero, religious vision |
| `neutral` | Routine events, forgotten over time |

---

## 🧬 Memory Dynamics

- New memories are stronger → high influence
- Old memories decay unless reinforced
- Multiple similar memories create **bias**
- Rare intense memories become **core memories**
- NPCs can share memories through dialogue or rumor

---

## 🧩 Integration Points

| System | Use |
|--------|-----|
| 🗣 Dialogue | NPC can recall or reference past events directly |
| 🎯 Goal Engine | Memories reinforce or disrupt long-term goals |
| 😠 Mood System | Memory triggers affect current behavior |
| 🪞 Relationship System | Reactions to shared events build bonds or rivalries |
| 📖 History Engine | Used to reconstruct narrative from world data |

---

## 🧪 Example: Mood Derivation from Memory

```python
def derive_mood(npc):
    last_30_days = get_recent_memories(npc, days=30)
    joy = sum(mem['emotional_weight'] for mem in last_30_days if mem['type'] == 'joy')
    grief = sum(mem['emotional_weight'] for mem in last_30_days if mem['type'] in ['loss', 'shame'])
    return "happy" if joy > grief else "sad"
```

---

## 🧠 Deep Narrative Hooks

- NPCs may **misremember** or repress memories
- Some NPCs **create false memories** (delusional, cursed)
- **Shared memories** between NPCs → synchronised mood/loyalty
- **Player choices** embedded in NPC memory create emotional consequences

---

## 📦 Summary

Memory is the soul of a story.  
Let your NPCs **remember**, and they become human.  
Let them **share**, and they become history.

> The world forgets. But your characters shouldn't.
