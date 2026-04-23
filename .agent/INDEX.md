---
file: INDEX.md
scope: shared-safe
load: startup
---

# INDEX.md — Agent File Manifest

Single source of truth for **what loads when**, **where things live**, and **how big this workspace is**.
Read this first when onboarding a new session or debugging context issues.

---

## Load Matrix

| File               | Scope         | Load Moment          | Size  | Purpose                                                 |
| ------------------ | ------------- | -------------------- | ----- | ------------------------------------------------------- |
| `INDEX.md`         | shared-safe   | startup              | ~5 KB | This manifest. Load order + scope map.                  |
| `AGENTS.md`        | shared-safe   | startup              | ~6 KB | Entry flow: identity summary, task workflow, pointers.  |
| `SOUL.md`          | shared-safe   | startup              | ~3 KB | Personality, vibe, boundaries.                          |
| `IDENTITY.md`      | shared-safe   | startup              | ~2 KB | Name, avatar, stack.                                    |
| `USER.md`          | shared-safe   | startup              | ~4 KB | About Kiet — role, preferences, approval keywords.      |
| `PRINCIPLES.md`    | shared-safe   | startup              | ~4 KB | Non-negotiable code rules. Canonical source.            |
| `GUIDELINES.md`    | shared-safe   | startup              | ~3 KB | Meta-behavior rules (think, simplify, surgical, goal).  |
| `MEMORY.md`        | **main-only** | main-session-startup | ~6 KB | Curated long-term memory. Never load in group contexts. |
| `HEARTBEAT.md`     | shared-safe   | per-heartbeat        | ~4 KB | Proactive check checklist.                              |
| `TOOLS.md`         | shared-safe   | on-demand            | ~5 KB | MCP servers, CLI, env vars, project paths.              |
| `ESCALATION.md`    | shared-safe   | on-demand            | ~4 KB | Decision matrix: proceed / ask / halt.                  |
| `WORKFLOWS.md`     | shared-safe   | on-demand            | ~4 KB | Task lanes: feature / hotfix / devops / question.       |
| `RETROSPECTIVE.md` | shared-safe   | on-demand            | ~2 KB | Post-task reflection template.                          |
| `tests/golden.md`  | shared-safe   | on-demand            | ~5 KB | Expected behavior for common Slack inputs.              |

**Startup budget target:** ≤ 30 KB total for the `startup` set (currently ~27 KB). If this grows beyond 30 KB, trim or demote entries to `on-demand`.

---

## Scope Legend

- **shared-safe**: May load in any session, including group channels with other humans.
- **main-only**: Load ONLY in direct conversations with Kiet (DMs). Contains personal context, project-specific decisions. Never echo content in shared spaces.

---

## Load Moments

| Moment                 | Trigger                                             | What to load                              |
| ---------------------- | --------------------------------------------------- | ----------------------------------------- |
| `startup`              | Every new session                                   | All files marked `startup`                |
| `main-session-startup` | New session in a DM with the workspace owner (Kiet) | Additionally load `MEMORY.md`             |
| `per-heartbeat`        | Runtime heartbeat poll                              | `HEARTBEAT.md` only (keep it lean)        |
| `on-demand`            | Agent determines it needs the file                  | Read via file tool, don't keep in context |

---

## Workspace-level vs Project-level

This `.agent/` folder is the **workspace-level** brain (ZenAgent's own identity & workflow).

Each Angular **project** has its own `.agent/` folder with a different set of files:

| File              | Location            | Purpose                                             |
| ----------------- | ------------------- | --------------------------------------------------- |
| `ARCHITECTURE.md` | project's `.agent/` | Folder structure + component patterns for that repo |
| `RULES.md`        | project's `.agent/` | Coding standards for that repo                      |
| `SKILL.md`        | project's `.agent/` | CLI commands, gotchas, discovered shared components |

Only read these **after** `cd <project-dir>`. Do not look for them in this workspace.

---

## Dependency Graph

```
INDEX.md (you are here)
  │
  ├── points to → AGENTS.md       (the orchestrator)
  │                 ├── delegates to WORKFLOWS.md (lane selection)
  │                 ├── cites GUIDELINES.md       (meta-behavior baseline)
  │                 ├── cites PRINCIPLES.md       (code rules)
  │                 └── cites ESCALATION.md       (when to ask)
  │
  ├── points to → SOUL + IDENTITY + USER (personality + context)
  │
  └── references  → HEARTBEAT.md   (proactive loop)
                    MEMORY.md      (main-only)
                    TOOLS.md       (MCP + CLI lookup)
                    tests/golden.md (self-check)
```

---

## When to Update This File

- New file added to `.agent/` → add a row to the Load Matrix.
- File moved between `startup` / `on-demand` → update Load Moment column.
- Any file grows >2× its listed size → re-trim or demote.
- Breaking change to scope of a file → bump its `version` in its frontmatter.
