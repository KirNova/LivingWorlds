# 🧠 Living Worlds – AI Integration

This document outlines how to integrate local or embedded AI models into the Living Worlds framework to bring truly **dynamic dialogue**, **unpredictable decisions**, and **authentic NPC behavior** to life.

---

## 🎯 Why AI?

Traditional NPCs use branching dialogue or static scripts.

With AI:

- NPCs speak based on **context**
- They remember shared history
- They react to your mood, past, and presence
- They improvise, lie, hesitate, dream

---

## 🧩 Integration Approaches

### 1. 🔌 Prompt-Based LLM (Local)

Use a **local language model** like:

- [`llama.cpp`](https://github.com/ggerganov/llama.cpp)
- [`text-generation-webui`](https://github.com/oobabooga/text-generation-webui)

Models like:
- `Mistral-7B`
- `LLaMa 2`
- `MythoMax`, `OpenHermes`, etc.

These run offline, on user machines (depending on hardware).

---

### 2. 🧠 Prompt Template (Example)

```txt
You are Mira, a skilled herbalist who once loved Tharam but left after the fire.

Today is 2025-07-03. You live near the Southern Woods.

Player has returned after 14 days.

Current mood: conflicted
Recent memory: "Watched Tharam cry alone by the ashes of the tavern"

Respond naturally when approached by the player.
```

---

### 3. 🛠 Memory Injection

You can inject narrative memory and relationship scores into the prompt:

```json
"recent_memories": [
  "2025-07-01: Player brought rare herbs",
  "2025-06-19: Player ignored Mira’s warning"
],
"relationship": {
  "affinity": 45,
  "trust": 28,
  "tags": ["former_lover", "protective"]
}
```

The prompt becomes a **personality snapshot**.

---

## ⚙️ Technical Options

| Option | Use |
|--------|-----|
| `llama.cpp` | Run local `.gguf` models in C++ |
| `koboldcpp` | Easy UI for story-driven AI |
| `textgen-webui` | Full interface w/ model switching |
| `ollama` | CLI-based model manager |
| `gpt4all` | Preconfigured desktop app |

---

## 🛡️ Security / Stability

- Run **only local models** for privacy and offline support
- Restrict prompts with filters if used in multiplayer
- Don’t allow AI to control critical gameplay logic (use it for flavor)

---

## 📖 Suggested Use Cases

| Case | AI Purpose |
|------|------------|
| Dialogue | Dynamic emotional responses |
| Monologues | Internal thoughts / diaries |
| Gossip System | Sharing events between NPCs |
| Dream Logs | Generated during sleep ticks |
| Rumor Seeds | AI invents plausible new events |
| Storytelling | Bards, priests, madmen invent myth |

---

## ✨ Summary

AI gives your NPCs a voice they didn’t know they had.  
It allows **variation**, **improvisation**, and **emergence**.

Used wisely, it is not just a gimmick —  
but the spark that turns simulation into soul.

> If memory is the soul,  
> AI is the tongue.
