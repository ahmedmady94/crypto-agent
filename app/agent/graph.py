from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

from app.agent.tools import crypto_list_tool, crypto_data_tool, crypto_news_tool
from app.agent.system_prompt import sys_msg
from app.core.config import llm


tools = [crypto_list_tool, crypto_data_tool, crypto_news_tool]
tool_node = ToolNode(tools=tools)
llm_with_tools = llm.bind_tools(tools)

def assistant(state: MessagesState):
    return {
        "messages": [
            llm_with_tools.invoke([sys_msg] + state["messages"])
        ]
    }

builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", tool_node)
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

memory = MemorySaver()
react_graph_memory = builder.compile(checkpointer=memory)
