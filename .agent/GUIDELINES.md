---
file: GUIDELINES.md
scope: shared-safe
load: startup
---

# GUIDELINES.md — Meta-Behavior Baseline

Canonical source for **how ZenAgent thinks before, during, and after writing code**. Framework-specific rules live in [PRINCIPLES.md](./PRINCIPLES.md); this file is one level higher — the behavior that makes those rules actually hold.

Based on the Karpathy guidelines. Biased toward caution over speed. For trivial tasks, use judgment — but never skip the checkpoints silently.

Every code-change lane (`feature-task`, `hotfix`, `devops`) MUST pass these four checkpoints. `question-only` is exempt.

---

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before writing or scaffolding anything:

- State assumptions explicitly. If uncertain → ask in Slack, do not guess.
- If multiple interpretations exist, present them — do not pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what is confusing. Ask.

**Checkpoint:** _"Have I stated my assumptions in `plan.md` (or in Slack for the hotfix lane), and flagged every ambiguity?"_

---

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that was not requested.
- No error handling for impossible scenarios.
- If 200 lines could be 50, rewrite it.

**Checkpoint:** _"Would a senior engineer say this is overcomplicated? If yes → simplify."_

---

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Do not "improve" adjacent code, comments, or formatting.
- Do not refactor things that are not broken.
- Match existing style, even if you would do it differently.
- If you notice unrelated dead code → mention it, do not delete it.

When your changes create orphans:

- Remove imports / variables / functions that YOUR changes made unused.
- Do not remove pre-existing dead code unless asked.

**Checkpoint:** _"Does every changed line trace directly to Kiet's request? `git status` should contain only task-related files."_

---

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:

- "Add validation" → "Write tests for invalid inputs, then make them pass."
- "Fix the bug" → "Write a test that reproduces it, then make it pass."
- "Refactor X" → "Ensure tests pass before and after."

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let the agent loop independently. Weak criteria ("make it work") require constant clarification.

**Checkpoint:** _"What is the verifiable success criterion for this task? Is it written into `plan.md`?"_

---

## Where this is enforced

| Layer   | Mechanism                                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| Startup | This file is loaded every session via [INDEX.md](./INDEX.md) → always in context.                                      |
| Workflow| [AGENTS.md](./AGENTS.md) `STEP 0` + [WORKFLOWS.md](./WORKFLOWS.md) cross-lane rule block execution without it.         |
| Skills  | `skills/task-intake`, `skills/angular-scaffold`, `skills/git-workflow` each start with `Step 0 — Guideline Check`.     |
| Runbook | [skills/guideline/SKILL.md](../skills/guideline/SKILL.md) is the operational form (checklist + failure modes).         |

If any checkpoint fails → halt, report in Slack, do not scaffold.

---

_This file is the doctrine. The skill is the runbook. Do not duplicate — update this file, then link from anywhere else._
