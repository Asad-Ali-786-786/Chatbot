from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_groq import ChatGroq
from typing import Annotated, TypedDict  # For Python 3.8 and above


# Initialize tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
tools = [wiki_tool, arxiv_tool]

# Groq API key (add a secure storage for deployment)
GROQ_API_KEY = "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"
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It").bind_tools(tools=tools)

# LangGraph setup
class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", lambda state: {"messages": [llm.invoke(state["messages"])]})
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile()

def process_message(user_input):
    """Process user input and generate a chatbot response."""
    events = graph.stream({"messages": [("user", user_input)]}, stream_mode="values")
    response = None
    for event in events:
        message = event["messages"][-1]  
        response = message.content  
    return response

# def process_message(user_input):
#     """Process user input and generate a chatbot response."""
#     if not user_input or not isinstance(user_input, str):
#         raise ValueError("Input must be a non-empty string.")

#     events = graph.stream({"messages": [("user", user_input)]}, stream_mode="values")
#     response = None
#     for event in events:
#         message = event["messages"][-1]
#         response = message.content
#     return response
