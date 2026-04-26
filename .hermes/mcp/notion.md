# Notion MCP

Use Notion MCP when Kiet provides a Notion requirement page.

## Setup

Add `NOTION_TOKEN` to `~/.hermes/.env`.

```bash
hermes mcp add notion --command "npx @notionhq/notion-mcp-server"
```

The Notion server may require headers depending on the package version:

```bash
OPENAPI_MCP_HEADERS='{"Authorization":"Bearer replace_me","Notion-Version":"2022-06-28"}'
```

## Extraction target

For task intake, extract:

- title
- description
- acceptance criteria
- mockup links
- constraints
