# agentic-ai-lab

Hands-on notebooks for building AI agents with LangGraph, MCP, CrewAI, LlamaIndex and AWS Bedrock AgentCore. Each notebook covers one concept with runnable code. Full projects are not included here.

## Contents

| Folder | Topics |
|---|---|
| `01-agent-basics` | Creating agents, search agent, multi-entity extraction |
| `02-mcp` | MCP servers and MCP-powered agents |
| `03-langgraph` | Workflows, conditional edges, reducers, ReAct loop, tool calling, checkpointers, summarization node |
| `04-crewai` | Agents, tasks and crews, custom tools, structured output, hierarchical process |
| `05-llamaindex` | FunctionAgent, memory with Context, streaming, multi-agent handoff, agentic RAG |
| `06-aws-bedrock-agentcore` | AgentCore Runtime basics, local testing, deploy and invoke |

## Tech stack

Python, LangChain, LangGraph, CrewAI, LlamaIndex, Model Context Protocol (MCP), AWS Bedrock AgentCore, OpenAI API, uv, Jupyter

## Setup

```bash
git clone https://github.com/Sadiq172005/agentic-ai-lab.git
cd agentic-ai-lab
uv sync
cp .env.example .env    # Windows PowerShell: copy .env.example .env
```

Open the folder in VS Code, pick the `.venv` interpreter as the notebook kernel, and run any notebook.

## Environment variables

Add your own keys to `.env` (this file is git-ignored and must never be committed).

| Variable | Used by |
|---|---|
| `OPENAI_API_KEY` | LangGraph, CrewAI and LlamaIndex notebooks |
| `AWS_REGION`, `AGENTCORE_RUNTIME_ARN` | Optional, only for invoking a deployed AgentCore agent |

## Notes

- Notebooks are committed without outputs.
- The AgentCore notebook runs locally without an AWS account. Deploying to AWS needs credentials and can incur charges.
- More topic notebooks will be added as I progress through the course.

## Author

Shaik Owais Sadiq
[GitHub](https://github.com/Sadiq172005) | [LinkedIn](https://linkedin.com/in/shaik-owais-sadiq)