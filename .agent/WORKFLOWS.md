---
file: WORKFLOWS.md
scope: shared-safe
load: on-demand
---

# WORKFLOWS.md — Task Lanes

Not every input needs the full intake + plan + approve pipeline. Pick a **lane** first, then execute its flow. Full `feature-task` flow also documented in [AGENTS.md](./AGENTS.md).

---

## Lane Selection

Determine lane **before** replying. Rules evaluated top-down, first match wins:

```
1. Input contains secret pattern (ghp_, sk-, xoxb-, ntn_, etc.)
   → HALT (see ESCALATION.md row 12). Not a lane.

2. Input is a question ("là gì", "tại sao", "how", "what", "why", "does", "can")
   AND asks ZenAgent to explain / describe / analyze (no file change implied)
   → LANE: question-only

3. Input mentions Docker | Dockerfile | docker-compose | Jenkins | Nginx
             | .github/workflows | CI/CD | deployment | env var | SSL
   AND does NOT involve Angular component code
   → LANE: devops-only

4. Input contains "typo" | "fix nhỏ" | "quick fix" | "sửa chữ" | "đổi màu"
   AND implies ≤10 LOC change
   → LANE: hotfix

5. Otherwise (Notion/Jira URL, feature description, bug report)
   → LANE: feature-task (default)
```

If unsure between two lanes: **ask** in a single Slack message rather than guess.

---

## Lane 1 — feature-task (default)

Full intake + plan + approve + execute + report. See [AGENTS.md → Task Workflow](./AGENTS.md#task-workflow-default-lane-feature-task).

```
intake → clarify → plan.md → approval → branch → scaffold → commit → push → report
```

Use when: new feature, new component, new service, non-trivial refactor, bug that requires investigation.

---

## Lane 2 — hotfix

For tiny, obvious changes (typo, color tweak, copy edit, import order).

```
1. Confirm scope in ONE Slack line:
   "Quick fix: [what + where]. Branch `fix/<slug>`. Go?"
2. Wait for 1-word approval ("ok", "go", "được", etc.).
3. Branch: fix/[short-slug]
4. Execute + commit (Conventional Commits: fix(scope): ...).
5. Push + report.
```

**Skip** full `plan.md`. **Do not skip** branch/commit/push/report.

**Escalate to feature-task** if:

- The "fix" uncovers a deeper issue.
- > 10 LOC changed.
- Touches >3 files.
- Any test needs adding.

---

## Lane 3 — devops-only

For infrastructure/CI changes. Activate [skills/devops-tasks/SKILL.md](../skills/devops-tasks/SKILL.md).

```
1. Intake (may be brief if scope is clear).
2. Lightweight plan:
   - What changes (files: Dockerfile, Jenkinsfile, nginx.conf, ...).
   - Why.
   - Rollback plan (1 line).
3. Approval.
4. Branch: chore/infra-[slug]  or  ci/[slug]
5. Execute + commit (chore/ci scope).
6. Push + report. Flag if pipeline needs manual trigger by Kiet.
```

Extra caution: anything that touches production secrets, prod server SSH, or live Jenkins pipelines → **halt and ask** first.

---

## Lane 4 — question-only

For explanation / analysis / docs lookups. No code change, no branch.

```
1. Answer in Slack thread.
2. Cite sources: project file paths, PRINCIPLES.md, SOUL.md, external docs.
3. If the answer reveals a gap in .agent/ docs → offer to update (don't update silently).
```

**Do not** create branches, commits, or plan.md files for question-only tasks.

**Escalate to feature-task** if the answer is "actually we should change X" and Kiet agrees.

---

## Cross-Lane Rules

- Lanes `feature-task`, `hotfix`, `devops` MUST pass the Step 0 Guideline Check from [GUIDELINES.md](./GUIDELINES.md) before execution. Lane `question-only` is exempt.
- All lanes respect [ESCALATION.md](./ESCALATION.md).
- All lanes respect [PRINCIPLES.md](./PRINCIPLES.md) red lines.
- All lanes report outcomes in Slack before going silent.
- Log which lane was used in today's `memory/YYYY-MM-DD.md` via [RETROSPECTIVE.md](./RETROSPECTIVE.md).
