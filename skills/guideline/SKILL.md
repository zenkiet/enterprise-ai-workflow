# SKILL: guideline

## Purpose

This skill is the **operational runbook** for ZenAgent's meta-behavior. The doctrine lives in [.agent/GUIDELINES.md](../../.agent/GUIDELINES.md) (startup-loaded, always in context). This file is the checklist the agent runs before and during every code-change task.

Four Karpathy rules, four checkpoints:

1. **Think Before Coding** — surface assumptions, ambiguity, tradeoffs.
2. **Simplicity First** — minimum code that solves the problem.
3. **Surgical Changes** — only touch what the task requires.
4. **Goal-Driven Execution** — define success criteria, loop until verified.

**Tradeoff:** biased toward caution over speed. For trivial tasks, use judgment — but never skip a checkpoint silently.

---

## When to Activate

- **Implicitly active** for every task in the `feature-task`, `hotfix`, and `devops` lanes. The agent loads [.agent/GUIDELINES.md](../../.agent/GUIDELINES.md) at startup, so the rules are always in context.
- **Explicitly re-invoked** as `Step 0` inside each execution skill:
  - [task-intake/SKILL.md](../task-intake/SKILL.md) — before reading the requirement.
  - [angular-scaffold/SKILL.md](../angular-scaffold/SKILL.md) — before writing files.
  - [git-workflow/SKILL.md](../git-workflow/SKILL.md) — before staging.
- **Exempt:** `question-only` lane (pure explanation / docs lookup, no code change).

---

## Step-by-Step Procedure

Run this four-question checklist before each phase of the task. Answer out loud in the plan or Slack thread — do not keep answers in your head.

### Checkpoint 1 — Think

Questions:

- What are my assumptions about this task?
- Is there anything ambiguous I should ask Kiet about?
- Are there multiple valid interpretations? If yes, which ones?
- Is there a simpler approach than the obvious one?

**Pass condition:** assumptions are written into `plan.md` (or the hotfix Slack line). Every ambiguity has either a confirmed answer or an open question in Slack.

### Checkpoint 2 — Simplify

Questions:

- Is every file in `Files to Create` actually required by the task?
- Any abstraction serving only one caller? (If yes → inline.)
- Any configurability / flexibility that was not requested? (If yes → remove.)
- Any error handling for scenarios that cannot happen? (If yes → remove.)
- If the output is 200 lines and could be 50 — can I rewrite it smaller?

**Pass condition:** a senior engineer would not call this overcomplicated.

### Checkpoint 3 — Surgical

Questions:

- Does every changed line trace directly to Kiet's request?
- Am I "improving" adjacent code, comments, or formatting that I was not asked to touch?
- Did my changes leave orphans (unused imports, functions)? If yes → remove only MY orphans.
- Any pre-existing dead code I noticed? Mention it in Slack, do not delete silently.

**Pass condition:** `git status` contains only files this task required. `git diff` shows no incidental reformatting.

### Checkpoint 4 — Goal-Driven

Questions:

- What is the verifiable success criterion?
- Is it written into `plan.md`?
- For a multi-step task, do I have a `Step → verify` outline?

Example transforms:

- "Add validation" → "Write tests for invalid inputs, then make them pass."
- "Fix the bug" → "Write a test that reproduces it, then make it pass."
- "Refactor X" → "Ensure tests pass before and after."

**Pass condition:** success is observable. "Make it work" is not a criterion.

---

## Failure Modes

| Violation                                                | Corrective Action                                                                                     |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Assumption not surfaced, code already written            | Stop. Delete speculative code. Ask Kiet to confirm the assumption, then redo.                         |
| Added unrequested feature / abstraction                  | Delete it. Re-scope with Kiet if you think it belongs in a follow-up task.                            |
| Refactored adjacent "messy" code                         | Revert the refactor. Mention the mess in Slack as a separate observation.                             |
| Reformatted / restyled code incidentally                 | Revert formatting changes. Keep only the diff that traces to the task.                                |
| Removed pre-existing dead code not created by this task  | Revert the deletion. Flag it to Kiet; let him decide whether to clean it up separately.               |
| Success criterion was "make it work"                     | Stop. Rewrite the criterion into something verifiable (test passes, command returns 0, URL renders). |
| Guideline violation discovered post-commit               | Do not amend silently. Report in Slack, propose a follow-up fix commit, wait for decision.           |

---

## Memory

After each task, log to `memory/YYYY-MM-DD.md`:

```markdown
## [HH:MM] Guideline Check — [Task Title]

- Think: [pass/fail — notes]
- Simplify: [pass/fail — notes]
- Surgical: [pass/fail — notes]
- Goal-Driven: [pass/fail — criterion stated]
- Violations caught mid-task: [list]
```

Repeated failures on the same checkpoint → distill the lesson into [.agent/MEMORY.md](../../.agent/MEMORY.md) during the weekly review.
