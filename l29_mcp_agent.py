import os
import asyncio
import time

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "Math-mcp": {
                "transport": "stdio",
                "command": "python",
                "args": [r"C:\Users\hp\Desktop\genai python\Agentic_class\mcp_servers\math_mcp.py"],
            },
            "weather": {
                "transport": "http",
                "url": "http://127.0.0.1:8000/mcp",
            }
        }
    )

    tools = await client.get_tools()
    print(tools)

    agent = create_agent(
        "openai:gpt-5.4-nano",
        tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    for message in math_response["messages"]:
        message.pretty_print()

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    for message in weather_response["messages"]:
        message.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())

