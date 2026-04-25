import os
from fastapi import FastAPI
from mcp.server.fastapi import FastApiServer
from mcp.server import Server
from browser_use import Agent
from browser_use.browser.context import BrowserContextConfig
from langchain_openai import ChatOpenAI # replace with your AI provider
from playwright_stealth import stealth_async


# Initialize MCP Server
mcp_server = Server("browser-use-node")
app = FastAPI()

# Configure AI
CUSTOM_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://proxy-ai.zenkiet.dev/v1")
CUSTOM_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt5.4-mini")
llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=SecretStr(CUSTOM_API_KEY),
    base_url=CUSTOM_BASE_URL
)

# Initialize Browser
browser = Browser(
    config=BrowserConfig(
        headless=True,
        extra_chromium_args=[
            '--no-sandbox',
            '--disable-dev-shm-usage',
            '--disable-blink-features=AutomationControlled',
            '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        ]
    )
)

@mcp_server.list_tools()
async def list_tools():
    return [
        {
            "name": "browse_and_act",
            "description": "Browse the web and perform complex actions (click, search, extract data)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "instruction": {"type": "string", "description": "Instruction for the agent (e.g: Find the price of iPhone on Shopee)"},
                    "url": {"type": "string", "description": "Starting URL"}
                },
                "required": ["instruction"]
            }
        }
    ]

@mcp_server.call_tool()
async def call_tool(name, arguments):
    if name == "browse_and_act":
        instruction = arguments.get("instruction")
        url = arguments.get("url", "https://google.com")

        # Initialize Agent from browser-use
        agent = Agent(
            task=instruction,
            llm=llm,
            browser=browser,
        )

        # Execute task
        result = await agent.run()
        return [{"type": "text", "text": str(result)}]

# Bind MCP to FastAPI via SSE
mcp_app = FastApiServer(mcp_server, app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)