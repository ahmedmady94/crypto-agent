# Crypto Market AI Agent (LangGraph + ReAct)

A production-style AI agent built using **LangGraph** and **FastAPI**, following a **ReAct (Reason–Act–Observe)** architecture to answer cryptocurrency-related questions using live data and news.

---

## 🚀 Live Demo

- **Swagger API Docs**  
  https://crypto-agent-haf1.onrender.com/docs

- **Example LangSmith Trace (Public, Read-only)**  
  https://smith.langchain.com/public/5f7964c4-4415-454a-a5f8-97ae8d49cf36/r

---

## 🧠 Architecture Overview

This agent is implemented as a **LangGraph state machine** using a ReAct-style loop:

1. **Reason** – The LLM analyzes the user query
2. **Act** – The agent decides whether to call a tool
3. **Observe** – Tool outputs are fed back into the reasoning loop
4. **Respond** – The agent produces a final answer

### Tools
- Crypto list retrieval
- Crypto market data lookup
- Crypto news retrieval

The system is intentionally designed as a **single-agent architecture** to keep:
- Reasoning transparent
- Tool usage explicit
- Debugging and observability simple

---

## 🔍 Observability with LangSmith

The agent is instrumented with **LangSmith tracing** to capture:
- Agent reasoning steps
- Tool invocations
- Execution timing
- Graph transitions

A sample **public trace** is shared above to demonstrate how the agent behaves during a real production run.

> Note: Public traces are shared selectively for demonstration purposes only.

---

## 🛠 Tech Stack

- **LangGraph** – agent orchestration
- **LangChain** – LLM + tool abstractions
- **FastAPI** – API layer
- **Docker** – containerization
- **Render** – cloud deployment
- **LangSmith** – tracing & observability

---

## 📦 Project Structure

app/
├── agent/

│   ├── graph.py          # LangGraph state machine definition

│   ├── system_prompt.py  # Centralized LLM instructions

│   └── tools.py          # Custom tool implementations
├── api/
│   └── routes.py         # FastAPI endpoint definitions
├── core/
│   └── config.py         # Global settings & LLM configuration

└── main.py               # Application entry point

---

## 🧪 Running Locally

```bash
docker build -t crypto-agent .
docker run -p 8000:8000 --env-file .env crypto-agent

## 🧪 Then open:
http://localhost:8000/docs


