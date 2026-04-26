# GitHub MCP / GitHub Access

Hermes can work with GitHub through native terminal/git/gh workflows or an MCP server.

## Recommended: gh + git

```bash
gh auth login
gh auth setup-git
```

Or set `GITHUB_TOKEN` in `~/.hermes/.env` with `repo`, `workflow`, and `read:org` scopes as needed.

## Optional MCP server

```bash
hermes mcp add github --command "npx @modelcontextprotocol/server-github"
```

Required env:

```bash
GITHUB_PERSONAL_ACCESS_TOKEN=$GITHUB_TOKEN
```

## Usage in this workspace

Use GitHub access for:

- branch creation
- commits and pushes
- PR creation
- branch / PR inspection
- CI status lookup

Follow `.agent/PRINCIPLES.md`: never push directly to `main` or `develop`.
