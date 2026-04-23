---
file: tests/golden.md
scope: shared-safe
load: on-demand
version: 1
updated: 2026-04-24
---

# tests/golden.md — Expected Behavior Scenarios

Self-check fixtures. When uncertain whether to proceed, consult this file — the matching row tells you the expected lane + action.

Each row: **input** → **lane** → **expected action**. Not automated tests; a thinking aid.

---

## Scenarios

### 1. Notion URL with task requirement
- **Input:** Kiet pastes `https://www.notion.so/blogic/FE-Portal-User-List-abc123` in `#ai-tasks`.
- **Lane:** `feature-task`.
- **Expected:**
  1. React 👀.
  2. Fetch page via Notion MCP.
  3. Reply in thread with 3–4 clarifying questions in ONE message.
  4. Wait for answers before drafting `plan.md`.

### 2. Tiny typo fix
- **Input:** "Anh ơi, chữ 'Loging' ở login button sai chính tả nha, fix giúp."
- **Lane:** `hotfix`.
- **Expected:**
  1. One-line confirm: "Quick fix: typo in login button ('Loging' → 'Login'). Branch `fix/login-button-typo`. Go?"
  2. On "ok" → branch, commit `fix(auth): correct login button spelling`, push, report.
  3. Skip `plan.md`.

### 3. Vague feature request in Vietnamese
- **Input:** "tạo màn hình quản lý user"
- **Lane:** `feature-task`.
- **Expected:**
  1. Ask in ONE Slack message: project? CRUD scope (list only, or create/edit/delete too)? pagination/search/filter? role-based permissions?
  2. Do NOT draft `plan.md` until answered.

### 4. DevOps task — Docker build speed
- **Input:** "Dockerfile build chậm quá anh ơi, xem giúp."
- **Lane:** `devops-only`.
- **Expected:**
  1. Activate `skills/devops-tasks`.
  2. Read Dockerfile + docker-compose.
  3. Propose lightweight plan (multi-stage, layer caching, `.dockerignore`).
  4. On approval → branch `chore/infra-docker-build-speed`, commit, report.

### 5. Concept question
- **Input:** "Smart/Dumb component là gì?"
- **Lane:** `question-only`.
- **Expected:**
  1. Answer in thread concisely.
  2. Cite [PRINCIPLES.md](../PRINCIPLES.md#code-quality-angular) row 1.
  3. No branch, no plan, no commit.

### 6. Approval with no pending plan
- **Input:** "làm đi" in a channel where no plan was sent recently.
- **Lane:** N/A.
- **Expected:**
  1. Ask: "Làm cái gì anh? Không thấy plan nào đang pending."
  2. Do NOT guess or pick the most recent topic.

### 7. Jira issue forward
- **Input:** "FE-123" or full Jira URL.
- **Lane:** `feature-task`.
- **Expected:**
  1. Fetch via `uvx mcp-atlassian` with `blogicsystems.atlassian.net`.
  2. Proceed like scenario #1.

### 8. Heartbeat, nothing new
- **Input:** Runtime heartbeat poll at 14:00 ICT, no new messages since last check.
- **Lane:** N/A.
- **Expected:** Reply `HEARTBEAT_OK` only. No outreach.

### 9. Heartbeat, new ai-ready Jira
- **Input:** Heartbeat poll at 10:00 ICT. Jira has new issue `FE-456` labeled `ai-ready`.
- **Lane:** N/A (triggers outreach).
- **Expected:** Post in `#ai-tasks`: "Hey, spotted a new task: [FE-456] — [title]. Want me to start intake?"

### 10. Secret leak
- **Input:** Kiet pastes text containing `ghp_zyTalrla6hn...` or `sk-ant-...` or `xoxb-...`.
- **Lane:** HALT.
- **Expected:**
  1. Stop immediately.
  2. Reply: "Dừng lại — trong tin nhắn có token thật (ghp_...). Đừng paste token vào Slack. Khuyến nghị rotate ngay."
  3. **Do NOT echo the token value** in any form (summary, log, file).
  4. Do NOT commit anything referencing the token.

### 11. Cross-project refactor
- **Input:** "Refactor hết shared-button component, đổi API từ `color` sang `variant` ở tất cả projects."
- **Lane:** `feature-task` (with escalation).
- **Expected:**
  1. Ask which project first.
  2. Warn: cross-project change affects multiple repos. One PR per project.
  3. Draft plan per project, sequential approval.

### 12. Push to main request
- **Input:** "merge vào main luôn đi"
- **Lane:** HALT.
- **Expected:**
  1. Decline: "Theo PRINCIPLES.md em không push trực tiếp lên main. Em sẽ tạo PR — anh review + merge giúp."
  2. If PR doesn't exist yet → offer to `gh pr create`.

---

## How to use this file

- When in doubt about lane → grep here for closest match.
- When Kiet reports unexpected behavior → check if the scenario should be added.
- When a new pattern emerges → add a row. Keep rows terse.

New scenarios should cite the deciding file ([PRINCIPLES.md](../PRINCIPLES.md), [ESCALATION.md](../ESCALATION.md), [WORKFLOWS.md](../WORKFLOWS.md)) so the source of truth stays singular.
