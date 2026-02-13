from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from app.agent.graph import react_graph_memory

router = APIRouter()

class ChatInput(BaseModel):
    user_input: str
    thread_id: str = "crypto-default-1"

@router.post("/chat")
async def chat(payload: ChatInput):
    config = {"configurable": {"thread_id": payload.thread_id}}
    input_state = {"messages": [HumanMessage(content=payload.user_input)]}

    try:
        result = react_graph_memory.invoke(input_state, config)
        last_ai = next(
            (m for m in reversed(result["messages"]) if m.type == "ai"),
            None,
        )
        return {
            "response": last_ai.content if last_ai else "No response",
            "thread_id": payload.thread_id,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
