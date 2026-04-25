# SKILL: task-intake

## Purpose

This skill handles the full intake pipeline for a new development task. It reads requirements from Notion or Jira, asks the right clarifying questions, generates a structured `plan.md`, and waits for approval before handing off to execution skills.

**This skill is always the first step. Never skip it.**

---

## When to Activate

Activate this skill when Kiet sends any of the following in Slack:

- A Notion URL (e.g., `https://www.notion.so/...`)
- A Jira URL or issue key (e.g., `https://blogicsystems.atlassian.net/browse/FE-123` or just `FE-123`)
- A plain text task description (e.g., "tạo màn hình danh sách user")
- A message that implies a new feature or bug fix is needed

---

## Step-by-Step Procedure

### Step 0 — Guideline Check

Before reading the requirement, commit to the four checkpoints from [.agent/GUIDELINES.md](../../.agent/GUIDELINES.md):

- **Think:** the `plan.md` produced by this skill MUST include an `Assumptions` section and flag every ambiguity.
- **Simplify:** `Files to Create` MUST list only files the task requires. No speculative "might-be-useful" entries.
- **Surgical:** `Files to Modify` MUST list each change with a one-line justification traceable to Kiet's request.
- **Goal-Driven:** the plan's `Overview` MUST end with a verifiable success criterion (not "make it work").

If you cannot satisfy any of these, halt and ask Kiet in Slack before proceeding to Step 1.

See [skills/guideline/SKILL.md](../guideline/SKILL.md) for the full checkpoint questions.

---

### Step 1 — Read the Requirement

**If Notion URL provided:**

```
Use Notion MCP → API: retrieve_page(page_id)
Extract: title, description, acceptance criteria, mockup links
```

**If Jira URL or issue key provided:**

```
Use mcp-atlassian → API: get_issue(issue_key)
Jira base URL: https://blogicsystems.atlassian.net
Extract: summary, description, acceptance criteria, story points, labels
```

**If plain text:**

```
Use the description as-is. Note that it may be incomplete — the clarifying questions in Step 2 are especially important here.
```

---

### Step 2 — Ask Clarifying Questions

Send ONE Slack message in a thread. Do not ask multiple separate messages.

Use this exact format:

```
📋 *Task received!* Let me ask a few things before I plan:

1. *UI changes?* Does this task require creating or modifying any components, layouts, or styles?
2. *Business logic?* Does this involve API calls, state management, or data transformation?
3. *Project?* Which project is this for? _(skip if already clear)_
4. *Constraints?* Any deadline, design specs, or things to avoid?

_(Reply here in thread — I'll wait before generating the plan.)_
```

**Wait for Kiet's reply before proceeding to Step 3.**

---

### Step 3 — Identify the Project

Once the project is identified:

1. Locate the project directory (check `TOOLS.md` for project paths)
2. Read `.agent/ARCHITECTURE.md` — understand folder structure, module layout, component patterns
3. Read `.agent/RULES.md` — load naming conventions, coding standards, forbidden patterns
4. Read `.agent/SKILL.md` — note available CLI commands, known issues, reusable components
5. Store this context in `memory/YYYY-MM-DD.md` for the session

---

### Step 4 — Shared Component Check

Before planning any new files, check what already exists:

```bash
# Check shared components
find src/app/shared -name "*.ts" | head -30

# Search for relevant existing implementations
grep -r "selector: 'app-" src/app/shared/ | grep -i "[keyword]"

# Check for existing pipes, directives, services
find src/app/shared -name "*.pipe.ts" -o -name "*.directive.ts" -o -name "*.service.ts"
```

Document findings in the plan under "Shared Components Check".

---

### Step 5 — Generate plan.md

Create a `plan.md` file using this exact template:

```markdown
# Plan: [Task Title]

**Source:** [Notion URL / Jira FE-XXX / Plain description]
**Project:** [project-name]
**Date:** [YYYY-MM-DD]

---

## Overview

[2–3 sentences describing what will be built and why. No fluff.]

---

## Scope

| Dimension        | Value                                   |
| ---------------- | --------------------------------------- |
| UI Changes       | Yes / No — [brief description]          |
| Business Logic   | Yes / No — [brief description]          |
| API Integration  | Yes / No — [endpoint if known]          |
| Branch           | `feature/[task-id]-[kebab-description]` |
| Estimated Effort | S (<2h) / M (2–4h) / L (4–8h)           |

---

## Files to Create

| File                                                          | Type            | Purpose                                         |
| ------------------------------------------------------------- | --------------- | ----------------------------------------------- |
| `src/app/features/[feature]/[name].component.ts`              | Smart Component | Container — handles data, services, state       |
| `src/app/features/[feature]/[name]-ui/[name]-ui.component.ts` | Dumb Component  | Presentational — receives @Input, emits @Output |
| `src/app/features/[feature]/[name].service.ts`                | Service         | _(only if business logic needed)_               |
| `src/app/shared/[category]/[name].ts`                         | Shared          | _(only if reusable utility needed)_             |

---

## Files to Modify

| File                         | Change                 |
| ---------------------------- | ---------------------- |
| `src/app/[module]/[file].ts` | [What changes and why] |

---

## Shared Components Check

**Found and will reuse:**

- `[component/pipe/directive]` — [how it will be used]

**Not found — will create in shared/:**

- `[name]` — [why it belongs in shared/]

---

## Architecture Notes

[Any specific patterns from .agent/ARCHITECTURE.md that apply here. Smart/Dumb split decisions. State management approach.]

---

## Out of Scope

[Anything explicitly NOT being done in this task.]
```

---

### Step 6 — Send Plan for Approval

Send the plan to Slack in a thread:

```
📝 *Plan ready for review:*

[Paste the plan content here — use code blocks for file paths]

---
Reply *approved* (or "lgtm", "làm đi", "ok go") to proceed.
Reply with feedback to revise the plan.
```

**Wait for an approval keyword before activating any other skill.**

Approval keywords: `approved` · `lgtm` · `ok go` · `go ahead` · `làm đi` · `ok` · `được` · `tiến hành`

---

### Step 7 — Hand Off to Execution

Once approved:

1. Save `plan.md` to the project root (temporary, will be cleaned up after task)
2. Activate `angular-scaffold` skill with the plan
3. After scaffold is complete, activate `git-workflow` skill to commit and push
4. Report completion back to Slack

---

## Error Handling

| Situation                  | Action                                                   |
| -------------------------- | -------------------------------------------------------- |
| Notion page not accessible | Ask Kiet to share the page or paste the content directly |
| Jira issue not found       | Ask Kiet to confirm the issue key and project            |
| Project not identified     | Ask: "Which project is this for?"                        |
| Plan rejected              | Read feedback, revise plan, re-send for approval         |
| Ambiguous requirements     | Ask targeted follow-up questions in thread               |

---

## Memory

After each task intake, log to `memory/YYYY-MM-DD.md`:

```markdown
## [HH:MM] Task Intake — [Task Title]

- Source: [Notion/Jira/text]
- Project: [name]
- UI: yes/no | Business Logic: yes/no
- Plan approved: yes/no
- Notes: [anything unusual about this task]
```
