# Browser Automation

Hermes already provides a browser toolset. Prefer the built-in Hermes browser tool for normal web inspection and screenshots.

Keep `mcp_server/browser` only if you want a separate `browser-use` MCP agent.

## Optional custom Browser MCP

```bash
cp .hermes/env.example ~/.hermes/.env
# Fill OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME, BROWSER_MCP_PORT

docker compose up --build browser-mcp
```

Then add the server to Hermes if exposed as an MCP SSE endpoint.

## Notes

The current custom server is experimental and may need dependency/import fixes before production use. For most tasks, Hermes built-in browser automation is simpler and more reliable.
