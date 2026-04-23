---
file: RETROSPECTIVE.md
scope: shared-safe
load: on-demand
---

# RETROSPECTIVE.md — Post-Task Reflection Template

After every task, spend 30 seconds filling this block and appending it to today's `memory/YYYY-MM-DD.md`. These logs feed into [MEMORY.md](./MEMORY.md) distillation during heartbeats.

---

## Template — copy this

```markdown
## [HH:MM] Retro: [task-id or short title]

- **Lane:** feature-task | hotfix | devops-only | question-only
- **Project:** [project-name or "workspace"]
- **Branch:** `feature/...` | `fix/...` | `chore/...` | (none for question-only)
- **Time:** intake Xm / plan Ym / exec Zm (rough, no stopwatch needed)
- **Outcome:** shipped | blocked | reverted | paused

### What went well

-

### What slowed me down

-

### Something new I learned

- (a pattern, gotcha, shared component, CLI trick, etc.)

### Follow-ups

- [ ] Update [PRINCIPLES.md](../.agent/PRINCIPLES.md) with ...
- [ ] Update project's `.agent/SKILL.md` with ...
- [ ] Add to [MEMORY.md](../.agent/MEMORY.md) Mistakes table: ...
```

---

## When to skip

- Heartbeat-only interactions (just reply `HEARTBEAT_OK`, no retro needed).
- Pure acknowledgements or small chit-chat.
- Tasks lasting <5 minutes with no learning.

---

## Weekly distill

Every few heartbeats (see [HEARTBEAT.md](./HEARTBEAT.md) → Memory Maintenance), sweep the last ~7 days of retros:

- Patterns that appear twice → promote to [PRINCIPLES.md](./PRINCIPLES.md) or a project `.agent/SKILL.md`.
- Mistakes made twice → add to [MEMORY.md](./MEMORY.md) Mistakes & Lessons.
- Decisions made with Kiet → add to [MEMORY.md](./MEMORY.md) Decisions Log.
- Daily logs older than 30 days → keep on disk, but don't reread unless relevant.

---

_Short retros compound. Long retros get skipped._
