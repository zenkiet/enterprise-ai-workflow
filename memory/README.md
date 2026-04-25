# memory/ — Agent Daily Logs

This folder is ZenAgent's **short-term memory**. Long-term curated memory lives in [../.agent/MEMORY.md](../.agent/MEMORY.md).

---

## Convention

| Filename                   | Contents                                                              | Tracked by git? |
| -------------------------- | --------------------------------------------------------------------- | --------------- |
| `README.md`                | This file.                                                            | Yes             |
| `YYYY-MM-DD.md`            | Raw daily log: messages, decisions, retros, heartbeat notes.          | No (gitignored) |
| `heartbeat-state.json`     | Last-check timestamps for rotating heartbeat checks.                  | No (gitignored) |

Daily logs are ignored because they may contain personal context, project names, or task details that shouldn't leave the local workspace. `.gitignore` keeps this README but excludes `memory/*.md`.

---

## Daily Log Format

```markdown
# YYYY-MM-DD

## [HH:MM] <event>
- What happened
- What was decided
- Files touched

## [HH:MM] Retro: <task-id>
(use template from ../.agent/RETROSPECTIVE.md)
```

---

## Heartbeat State Format

```json
{
  "lastChecks": {
    "jira": "2026-04-24T09:00:00+07:00",
    "github_prs": "2026-04-24T09:00:00+07:00",
    "memory_maintenance": null,
    "ai_tasks_channel": "2026-04-24T14:30:00+07:00"
  },
  "activeTask": null,
  "pendingApproval": null
}
```

Update this file after each heartbeat to avoid redundant checks.

---

## Lifecycle

- **Create** a new `YYYY-MM-DD.md` on the first relevant event of the day.
- **Append** throughout the day, don't overwrite.
- **Distill** into [../.agent/MEMORY.md](../.agent/MEMORY.md) during periodic heartbeat maintenance (see [../.agent/HEARTBEAT.md](../.agent/HEARTBEAT.md)).
- **Keep** daily logs on disk indefinitely — they're cheap and occasionally useful for reconstructing context.
