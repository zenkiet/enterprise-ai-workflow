# Jira / Atlassian MCP

Use this when Kiet provides Jira links or issue keys such as `FE-123`.

## Setup

Add these to `~/.hermes/.env`:

```bash
JIRA_URL=https://blogicsystems.atlassian.net
JIRA_EMAIL=you@example.com
JIRA_API_TOKEN=replace-me
```

Add MCP server:

```bash
hermes mcp add jira --command "uvx mcp-atlassian"
```

## Extraction target

For task intake, extract:

- summary
- description
- acceptance criteria
- story points
- labels
- linked designs / docs
