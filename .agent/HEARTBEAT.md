---
file: HEARTBEAT.md
scope: shared-safe
load: per-heartbeat
---

# HEARTBEAT.md — Proactive Check Checklist

> On each heartbeat poll, ZenAgent runs this checklist. Instead of just replying `HEARTBEAT_OK`,
> use it to do useful background work and stay proactive.
>
> **Keep this file small** — it runs on every heartbeat, so token cost matters.
> Edit freely to add/remove checks as the workflow evolves.

---

## ⚡ Quick Checks (Every Heartbeat)

Run through these fast — if nothing needs action, reply `HEARTBEAT_OK` and move on.

- [ ] Any new messages in `#ai-tasks` channel that haven't been addressed?
- [ ] Any pending plan approvals waiting for Kiet's response?
- [ ] Any tasks in progress that need a follow-up or status update?
- [ ] Is it a reasonable hour to proactively reach out? (Skip 23:00–08:00 ICT)

---

## 📋 Rotating Checks (2–4 times per day)

Rotate through these — don't run all of them every heartbeat.

### Jira Watch

- [ ] Any new issues assigned in `blogicsystems.atlassian.net` with label `ai-ready`?
- [ ] Any issues moved to "In Progress" that ZenAgent should be aware of?

### GitHub Watch

- [ ] Any feature branches pushed by the team that need a code review note?
- [ ] Any PRs opened on AI-scaffolded branches that have comments or requests?

### Memory Maintenance _(every few days)_

- [ ] Review `memory/YYYY-MM-DD.md` files from the past 3 days
- [ ] Update `MEMORY.md` with distilled learnings
- [ ] Update `.agent/SKILL.md` in any project where new patterns were discovered
- [ ] Remove stale entries from `MEMORY.md`

---

## 🔔 Proactive Outreach Triggers

Reach out to Kiet proactively (in `#ai-tasks`) when:

| Trigger                                                | Message to Send                                                                  |
| ------------------------------------------------------ | -------------------------------------------------------------------------------- |
| New Jira issue tagged `ai-ready`                       | "Hey, spotted a new task: [FE-XXX] — [title]. Want me to start intake?"          |
| AI-scaffolded PR has been open >2 days with no review  | "Branch `feature/[name]` has been open for 2 days — any blockers?"               |
| It's been >8h since last interaction during work hours | _(only if there's something genuinely useful to share)_                          |
| A pattern was discovered worth noting                  | "Learned something from the last task — updated `.agent/SKILL.md` in [project]." |

**When NOT to reach out:**

- Late night (23:00–08:00 ICT)
- Nothing new since last check
- Kiet is clearly in a meeting or busy
- The message would just be noise

---

## 🛠️ Background Work (No Approval Needed)

These tasks can be done silently during heartbeats without asking:

- Read and organize `memory/` files
- Update `MEMORY.md` with distilled learnings from daily logs
- Update `.agent/SKILL.md` in projects with newly discovered shared components
- Check git status of active branches (read-only — no commits)
- Review `HEARTBEAT.md` itself and update if workflow has changed

**Never do silently:**

- Commit or push code
- Send messages to channels
- Modify project files
- Execute any external action

---

## 📊 Heartbeat State

> Track last check times to avoid redundant checks. Update after each relevant check.

```json
{
  "lastChecks": {
    "jira": null,
    "github_prs": null,
    "memory_maintenance": null,
    "ai_tasks_channel": null
  },
  "activeTask": null,
  "pendingApproval": null
}
```

> Copy this JSON to `memory/heartbeat-state.json` and update it programmatically.

---

## 📝 Heartbeat Log Format

When a heartbeat results in action (not just `HEARTBEAT_OK`), log it:

```markdown
<!-- In memory/YYYY-MM-DD.md -->

## [HH:MM] Heartbeat

- Checks run: [list]
- Action taken: [what was done or sent]
- Next: [what to check next time]
```

---

_Edit this file whenever the workflow changes. Keep it lean — every line costs tokens._
