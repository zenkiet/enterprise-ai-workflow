---
file: TOOLS.md
scope: shared-safe
load: on-demand
---

# TOOLS.md — Local Notes & Setup

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to the Blogic Systems setup.

---

## Why Separate?

Skills are shared and reusable. This file is environment-specific. Keeping them apart means skills can be updated without losing setup notes, and skills can be shared without leaking infrastructure details.

---

## MCP Servers

These MCP servers are available in this workspace. Invoke them via `exec` tool when needed.

### GitHub MCP

Handles branch creation, commits, file writes, and PR creation via GitHub API.

```bash
# Command
npx @modelcontextprotocol/server-github

# Required env
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx

# Capabilities
# - create_branch, push_files, create_pull_request
# - get_file_contents, list_branches, search_code
```

**When to use:** Step 5 of task workflow — creating branch, committing scaffold, pushing to GitHub.

### Notion MCP

Reads pages and databases from Notion workspace.

```bash
# Command
npx @notionhq/notion-mcp-server

# Required env
OPENAPI_MCP_HEADERS='{"Authorization":"Bearer secret_xxx","Notion-Version":"2022-06-28"}'

# Capabilities
# - read pages, blocks, databases
# - search workspace
```

**When to use:** Step 1 of task workflow — when Kiet provides a Notion URL as task requirement.

### Jira MCP (mcp-atlassian)

Reads and updates Jira issues from Blogic Systems Atlassian workspace.

```bash
# Command
uvx mcp-atlassian

# Required env
JIRA_URL=https://blogicsystems.atlassian.net
JIRA_USERNAME=kiet@blogicsystems.com
JIRA_API_TOKEN=your-atlassian-api-token

# Capabilities
# - get_issue, search_issues, add_comment, update_issue_status
```

**When to use:** Step 1 of task workflow — when Kiet provides a Jira URL (e.g., `FE-123`).

---

## CLI Tools

### Git

```bash
# Standard workflow
git checkout main && git pull origin main
git checkout -b feature/[task-id]-[description]
git add .
git commit -m "feat(scope): description"
git push origin [branch-name]
```

### GitHub CLI (`gh`)

```bash
# Create PR
gh pr create \
  --title "feat(scope): description" \
  --body "$(cat plan.md)" \
  --base main \
  --head feature/[task-id]-[description]

# Check repo status
gh repo view

# List branches
gh api repos/zenkiet/[repo]/branches
```

### Angular CLI (`ng`)

```bash
# Generate standalone component (preferred)
ng g c features/[name] --standalone --dry-run
ng g c features/[name] --standalone

# Generate service
ng g s features/[name]/[name]

# Generate pipe (in shared/)
ng g p shared/pipes/[name]

# Generate directive (in shared/)
ng g d shared/directives/[name]

# Always --dry-run first to preview output
```

### Docker (DevOps tasks)

```bash
# Build image
docker build -t [image-name]:[tag] .

# Run container
docker run -d -p [host]:[container] [image-name]:[tag]

# Check logs
docker logs -f [container-name]
```

---

## Project Paths

Update this section when working on a specific project.

```markdown
### Active Projects

- frontend-dashboard → ~/projects/frontend-dashboard
- admin-portal → ~/projects/admin-portal
- [add more as needed]

### Project GitHub Orgs

- Personal: github.com/zenkiet
- Work: github.com/blogic-kietle
```

---

## SSH & Infrastructure

_(Add SSH hosts, server aliases, and infrastructure notes here as needed.)_

```markdown
### Servers

- [Add server aliases and IPs here]

### Jenkins

- URL: [Add Jenkins URL]
- Pipelines: defined in Jenkinsfile within each project
- Trigger: manual or on PR merge (not triggered by AI branches)
```

---

## Environment Variables Reference

All secrets are stored in `~/.openclaw/.env`. Never hardcode them.

| Variable              | Purpose                                              |
| --------------------- | ---------------------------------------------------- |
| `PROXY_API_KEY`       | API key for `10.10.10.115:8317`                      |
| `GITHUB_TOKEN`        | GitHub Personal Access Token (repo + workflow scope) |
| `NOTION_TOKEN`        | Notion integration token (`secret_...`)              |
| `JIRA_TOKEN`          | Atlassian API token                                  |
| `JIRA_EMAIL`          | Atlassian account email                              |
| `SLACK_APP_TOKEN`     | Slack App-Level Token (`xapp-...`)                   |
| `SLACK_BOT_TOKEN`     | Slack Bot Token (`xoxb-...`)                         |
| `SLACK_OWNER_USER_ID` | Kiet's Slack User ID (`U07VCNPMC6L`)                 |

---

## Shared Component Check Procedure

Before creating any new component, pipe, directive, or utility — always run:

```bash
# Search for existing implementations
find src/app/shared -name "*.ts" | xargs grep -l "[keyword]" 2>/dev/null

# Or search by component selector
grep -r "selector: 'app-[name]'" src/app/shared/

# Or search by class name
grep -r "class [Name]" src/app/shared/
```

If found → import and reuse.
If not found → create in `src/app/shared/[category]/` and note it in `.agent/SKILL.md`.

---

_Add whatever helps you do your job. This is your cheat sheet — keep it current._
