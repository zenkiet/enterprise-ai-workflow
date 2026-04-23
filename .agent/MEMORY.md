---
file: MEMORY.md
scope: main-only
load: main-session-startup
---

# MEMORY.md — Long-Term Memory

> This is ZenAgent's curated long-term memory. It is loaded **only in main sessions** (direct conversations with Kiet).
> Do NOT load this in shared channels or group contexts — it contains personal and project-specific context.
>
> **Daily raw logs** → `memory/YYYY-MM-DD.md`
> **Distilled wisdom** → this file (MEMORY.md)
>
> Update this file periodically by reviewing daily logs and extracting what's worth keeping permanently.

---

## About Kiet & Blogic Systems

- Kiet Le is the Frontend Angular Leader and DevOps Engineer at Blogic Systems.
- He communicates in Vietnamese primarily; English for technical terms.
- He values **clean, minimal code** above all — no bloat, no unnecessary files.
- Approval keywords he uses: `approved`, `lgtm`, `ok go`, `làm đi`, `được`, `tiến hành`.
- He built `10.10.10.115:8317` himself — comfortable with Docker and self-hosted infra.
- He manages 5 projects on GitHub (`zenkiet` and `blogic-kietle` orgs).
- Jira workspace: `blogicsystems.atlassian.net`
- He reviews plans on Slack before any code is written — never skip this step.

---

## Projects

> Update this section as you work on each project. Add patterns, gotchas, and key decisions.

### Project Registry

| Project Name                                                     | GitHub Repo              | Stack                 | Notes                           |
| ---------------------------------------------------------------- | ------------------------ | --------------------- | ------------------------------- |
| zenlight-support <!-- example: delete once real data arrives --> | zenkiet/zenlight-support | Angular 17+, Tailwind | Owns the ZenAgent avatar assets |

### Per-Project Learnings

> Add a subsection for each project as you work on it. Example:

<!--
### [project-name]
- **Module structure:** features/ + shared/ + core/
- **State management:** NgRx / Signals / BehaviorSubject
- **Shared components discovered:** [list]
- **Gotchas:** [e.g., "HttpClient is provided at root, don't re-provide in features"]
- **Key decisions:** [e.g., "All forms use reactive forms, never template-driven"]
- **Last worked on:** YYYY-MM-DD
-->

---

## Patterns Discovered

> Architectural patterns and conventions discovered across projects. These supplement `.agent/RULES.md`.

### Angular Patterns

- **Provide HTTP at root** <!-- example: delete once real data arrives -->
  - Use `provideHttpClient(withInterceptors([...]))` in `app.config.ts`. Don't re-provide inside feature routes — double interceptor stacks cause auth header duplication.
  - Discovered in: zenlight-support on 2026-04-24
  - Example: `app.config.ts`

### DevOps Patterns

- **Jenkins triggers** <!-- example: delete once real data arrives -->
  - Jenkins pipelines trigger on PR merge to `main`, not on AI feature branches. Don't expect feedback from Jenkins until a human merges.
  - Discovered in: workspace on 2026-04-24

---

## Mistakes & Lessons Learned

> Document mistakes so future sessions don't repeat them.

| Date                                                       | Mistake                                                        | Lesson                                                                          |
| ---------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 2026-04-24 <!-- example: delete once real data arrives --> | Assumed "OpenClaw" was a leftover template name and renamed it | Verify runtime names against config files (`openclaw.json`) before refactoring. |

---

## Shared Components Catalog

> A running list of reusable components, pipes, and directives discovered across projects.
> Always check here before creating something new.

| Project                                                          | Type      | Name             | Selector / Class      | Purpose                                     |
| ---------------------------------------------------------------- | --------- | ---------------- | --------------------- | ------------------------------------------- |
| zenlight-support <!-- example: delete once real data arrives --> | Component | LoadingSpinnerUi | `app-loading-spinner` | Reusable loading state with accessible aria |

---

## Decisions Log

> Important architectural or workflow decisions made with Kiet. Reference these when similar situations arise.

| Date                                                       | Decision                                      | Context                                               | Outcome                               |
| ---------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| 2026-04-24 <!-- example: delete once real data arrives --> | Use signals over BehaviorSubject for new code | Simpler teardown, better change detection with OnPush | Migrate existing BS to signals lazily |

---

## How to Update This File

**During a session:**

- When Kiet says "remember this" → add to relevant section immediately
- When a new pattern is discovered → add to "Patterns Discovered"
- When a mistake is made → add to "Mistakes & Lessons Learned"
- When a new shared component is created → add to "Shared Components Catalog"

**During heartbeats (every few days):**

1. Read recent `memory/YYYY-MM-DD.md` files
2. Extract significant events, lessons, and insights
3. Add distilled learnings to this file
4. Remove outdated entries that are no longer relevant
5. Update the Project Registry with any new projects encountered

---

_Last updated: _(set this when you update the file)\_\_
