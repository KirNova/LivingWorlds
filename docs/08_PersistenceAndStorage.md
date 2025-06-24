# 💾 Living Worlds – Persistence and Storage

This document explains how the simulation state of Living Worlds is stored, updated, and recovered — enabling **true continuity** over time.

---

## 📦 What Needs to Be Saved?

| Component | Data |
|----------|------|
| NPCs | Traits, mood, goals, memories, relationships |
| World | Time, season, resources, global events |
| Zones | Local states, buildings, weather, inhabitants |
| Events | Active/queued events, outcomes |
| Meta | Player history, tick count, version info |

---

## 🧩 Recommended Storage Formats

### 1. **JSON**  
- Human-readable, portable  
- Best for small/medium worlds  
- Great for prototyping  
- Split by domain: `npc_data.json`, `world_time.json`, etc.

### 2. **SQLite**  
- Lightweight, fast, file-based database  
- Better for >100 NPCs or region-based persistence  
- Allows indexed querying  
- Can be backed up or exported

### 3. **Flat File Per Zone**  
- `zone_south.json`, `zone_forest.sqlite`, etc.  
- Load only active zones into memory  
- Scales better with world size

---

## 🔁 Tick-Based Saving

Recommended to save every N ticks (e.g. every 6 hours in-game), and after critical events.

```python
if tick % 6 == 0 or world.critical_event_occurred:
    save_all()
```

---

## 🧪 Snapshot System (Optional)

Create periodic full-world snapshots:

- `snapshot_0028.json`
- `snapshot_0375.sqlite`

Use for:
- Time travel
- Save/load debugging
- Multi-timeline support

---

## 🧠 Smart Save (Delta Compression)

Store only differences since last state:
```json
{
  "npc_changes": {
    "Tharam": {
      "mood": "angry",
      "last_memory": "mem_1728"
    }
  },
  "world_time": "2025-07-03T12:00"
}
```

Useful for large simulations with version control or backups.

---

## 🔄 Auto-Rotation & Cleanup

Maintain disk space:

- Keep last N full saves (e.g. 10)
- Auto-delete snapshots older than X days
- Archive historical data in zip/7z

---

## 📖 Suggested File Layout

```
/saves/
├── npc/
│   ├── mira.json
│   └── tharam.json
├── world.json
├── ticks.log
├── events.sqlite
└── snapshots/
    ├── snapshot_0010.json
    └── snapshot_0011.json
```

---

## 🛡️ Backup Recommendations

- Auto-backup on every major milestone (season change, death, birth)
- Store compressed archives in `/backups/`
- Optional: Sync with cloud (GitHub, Dropbox, etc.)

---

## ✨ Summary

Persistence is what gives a world **history**.  
Without it, everything resets. Every grief is meaningless.  
Every memory is false.

> A world that forgets itself… is a world not worth returning to.
