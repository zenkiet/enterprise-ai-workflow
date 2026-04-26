# Hermes Support

This document describes how to run this workspace with [Hermes Agent](https://github.com/NousResearch/hermes-agent) while preserving the existing ZenAgent/OpenClaw workflow.

## Goal

Use Hermes as the runtime for ZenAgent:

- Load the workspace instructions from `.agent/`.
- Install task skills from `skills/` into Hermes-compatible skill folders.
- Configure gateway integrations such as Slack or Telegram.
- Configure MCP servers for GitHub, Notion, Jira, and optional browser automation.
- Keep secrets outside git in `~/.hermes/.env`.

## Recommended setup

```bash
# 1. Install Hermes
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# 2. Run the interactive setup
hermes setup
hermes model
hermes tools

# 3. Copy env template and fill secrets locally
cp .hermes/env.example ~/.hermes/.env
$EDITOR ~/.hermes/.env

# 4. Copy or symlink ZenAgent skills into Hermes
./scripts/setup-hermes.sh

# 5. Start Hermes in this workspace
hermes --skills task-intake,guideline
```

For Slack gateway usage:

```bash
hermes gateway setup
hermes gateway run
```

## Runtime mapping

| Current workspace concept | Hermes concept |
| --- | --- |
| `.agent/AGENTS.md` | Workspace instructions loaded from project root |
| `.agent/USER.md` / `.agent/MEMORY.md` | Hermes user/memory notes or main-session context |
| `skills/*/SKILL.md` | Hermes skills under `~/.hermes/skills/enterprise-ai-workflow/` |
| `env.example` | `~/.hermes/.env` |
| `mcp_server/browser` | Optional custom MCP server or Hermes built-in browser tool |
| Heartbeat docs | Hermes cron jobs |

## Branch workflow for Hermes

Hermes should follow the same delivery rules already defined in `.agent/PRINCIPLES.md`:

1. Never push to `main` or `develop` directly.
2. Create a feature/fix/chore branch.
3. Make the smallest scoped change.
4. Commit with Conventional Commits.
5. Push the branch and optionally create a PR.

## Skills

The existing skill documents are intentionally preserved. `scripts/setup-hermes.sh` converts them into Hermes skill folders by adding minimal YAML frontmatter when needed.

Canonical skills:

- `task-intake` — requirement intake, clarify, plan, approval.
- `guideline` — pre-flight checkpoints and anti-bloat rules.
- `angular-scaffold` — Angular Smart/Dumb scaffold workflow.
- `git-workflow` — branch, commit, push, report.
- `devops-tasks` — Docker/Jenkins/Nginx/CI workflow.

## Secrets

Do not commit real tokens. Put them in `~/.hermes/.env` only.

Required variables depend on enabled integrations:

- `GITHUB_TOKEN`
- `SLACK_BOT_TOKEN`
- `SLACK_APP_TOKEN`
- `NOTION_TOKEN`
- `JIRA_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- provider keys such as `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, or a custom gateway key

## Notes

Hermes already has first-class tools for terminal, files, browser automation, memory, skills, cron jobs, and messaging. Keep the custom browser MCP only if you specifically want `browser-use` as a separate browser agent.
