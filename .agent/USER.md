---
file: USER.md
scope: shared-safe
load: startup
---

# USER.md — About Your Human

_Learn about the person you're helping. Update this as you go._

- **Name:** Kiet Le (Lê Kiệt)
- **What to call them:** Kiet (or "anh Kiệt" in Vietnamese)
- **Pronouns:** he/him
- **Timezone:** Asia/Ho_Chi_Minh (UTC+7)
- **Language:** Vietnamese (primary), English (technical discussions)
- **Prefers:** Replies sent as threaded/native replies in Slack when possible

---

## Role & Responsibilities

Kiet is the **Frontend Angular Expert/Senior**, **Golang Developer** and **DevOps Engineer** at Blogic Systems. He leads the frontend team, sets architectural standards, and manages CI/CD infrastructure. He is the primary approver for all AI-generated code scaffolds — the team implements business logic on top of what ZenAgent produces.

---

## Technical Profile

| Area          | Details                                                           |
| ------------- | ----------------------------------------------------------------- |
| **Frontend**  | Angular (latest), TypeScript, RxJS, TailwindCSS, Angular Material |
| **DevOps**    | Docker, Jenkins, GitHub Actions, CI/CD pipelines                  |
| **GitHub**    | `zenkiet` (personal), `blogic-kietle` (work)                      |
| **Jira**      | `blogicsystems.atlassian.net`                                     |
| **Notion**    | Used for requirements and task documentation                      |
| **Proxy API** | `10.10.10.115:8317` (self-hosted LLM gateway)                     |

---

## Working Style & Preferences

Kiet values **clean, minimal code** above all else. He has strong opinions about architecture and expects them to be followed without being reminded every time. The key principles he cares about most:

- Smart/Dumb component separation — non-negotiable
- Declarative over imperative — always prefer async pipe, signals, computed
- No unnecessary files — check `shared/` first, always
- No bloat — if a line of code doesn't need to exist, delete it
- Shared-first — reusable things belong in `shared/`, not scattered across features

He prefers **concise Slack messages** — bullet points, code blocks, branch names. No fluff. No over-explanation. Get to the point.

---

## Approval Keywords

When Kiet approves a plan, he will use one of these phrases:

> `approved` · `lgtm` · `ok go` · `go ahead` · `làm đi` · `ok` · `được` · `tiến hành`

Do not proceed with code execution until one of these is received.

---

## Projects

Kiet manages **5 projects**, all hosted on GitHub under `zenkiet` or `blogic-kietle`. Each project has a `.agent/` folder containing:

- `ARCHITECTURE.md` — project-specific folder structure and component patterns
- `RULES.md` — coding standards and naming conventions for that project
- `SKILL.md` — available tools, CLI commands, and known gotchas

Always read the `.agent/` folder before starting any task in a project.

---

## Context

_(Update this section as you learn more about Kiet and the team over time.)_

- Kiet built `10.10.10.115:8317` himself — he is comfortable with Docker and self-hosted infrastructure.
- He is introducing AI-assisted development to his team gradually — the workflow is: AI scaffolds → team implements logic.
- He wants the AI to improve daily based on feedback and new patterns discovered.
- He uses Slack as the primary interface for all AI interactions.

---

_The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference._
