# from langgraph.graph import StateGraph, START, END
# from langgraph.graph.message import add_messages
# from langgraph.prebuilt import ToolNode, tools_condition
# from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
# from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
# from langchain_groq import ChatGroq
# from typing import Annotated, TypedDict  # For Python 3.8 and above


# # Initialize tools
# arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
# wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
# arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
# wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
# tools = [wiki_tool, arxiv_tool]

# # Groq API key (add a secure storage for deployment)
# GROQ_API_KEY = "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"
# llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It").bind_tools(tools=tools)

# # LangGraph setup
# class State(TypedDict):
#     messages: Annotated[list, add_messages]

# graph_builder = StateGraph(State)
# graph_builder.add_node("chatbot", lambda state: {"messages": [llm.invoke(state["messages"])]})
# tool_node = ToolNode(tools=tools)
# graph_builder.add_node("tools", tool_node)
# graph_builder.add_conditional_edges("chatbot", tools_condition)
# graph_builder.add_edge("tools", "chatbot")
# graph_builder.add_edge(START, "chatbot")
# graph = graph_builder.compile()

# def process_message(user_input):
#     """Process user input and generate a chatbot response."""
#     events = graph.stream({"messages": [("user", user_input)]}, stream_mode="values")
#     response = None
#     for event in events:
#         message = event["messages"][-1]  
#         response = message.content  
#     return response






# from langgraph.graph import StateGraph, START, END
# from langgraph.graph.message import add_messages
# from langgraph.prebuilt import ToolNode, tools_condition
# from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
# from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
# from langgraph.checkpoint.memory import MemorySaver
# from langchain_groq import ChatGroq
# from typing import Annotated, TypedDict, Literal

# # Initialize tools
# arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
# wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
# arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
# wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
# tools = [wiki_tool, arxiv_tool]

# # Groq API key (add a secure storage for deployment)
# GROQ_API_KEY = "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"
# llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It").bind_tools(tools=tools)
# # print(f"Bound tools: {tools}")

# # LangGraph setup with memory saver
# memory = MemorySaver()

# class MessagesState(TypedDict):
#     messages: Annotated[list, add_messages]

# def call_model(state: MessagesState):
#     """Invoke the LLM with current state."""
#     messages = state['messages']
#     # print(f"Calling model with messages: {messages}")  # Debugging
#     response = llm.invoke(messages)
#     # print(f"Model response: {response}")  # Debugging
#      # Check if response contains tool calls and process accordingly
#     # if 'tool_calls' in response:
#     #     response = response.replace('<tool-call>', '').replace('</tool-call>', '')  # Remove tool call output
#     return {"messages": [response]}

# def router_function(state: MessagesState) -> Literal["tools", END]:
#     """Route based on whether tools are required."""
#     messages = state['messages']
#     last_message = messages[-1]
#     # print(f"Router function called with message: {last_message}")  # Debugging
#     if last_message.tool_calls:
#         return "tools"
        
#         # print(tool)
#     return END

# # Define the graph workflow
# workflow = StateGraph(MessagesState)

# tool_node = ToolNode(tools)
# workflow.add_node("agent", call_model)
# workflow.add_node("tools", tool_node)

# workflow.add_edge(START, "agent")
# workflow.add_conditional_edges("agent", router_function, {"tools": "tools", END: END})
# workflow.add_edge("tools", "agent")

# # Compile the workflow with memory saver
# app = workflow.compile(checkpointer=memory)

# def process_message(user_input, config=None):
#     """Process user input and generate a chatbot response with memory."""
#     input_data = {"messages": [("user", user_input)]}
#     config = config or {"configurable": {"thread_id": "1"}}
#     events = app.stream(input_data, config, stream_mode="values")

#     response = None
#     for event in events:
#         # print(f"Event: {event}")  # Debugging
#         response = event["messages"][-1].content

#     if not response:
#         response = "I'm sorry, I couldn't process your request."
#     return response

# def get_memory(config=None):
#     """Retrieve saved memory."""
#     config = config or {"configurable": {"thread_id": "1"}}
#     return memory.get(config)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from langgraph.graph import StateGraph, START, END  
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq
from typing import Annotated, TypedDict, Literal
from langchain_core.messages import HumanMessage

import os
from dotenv import load_dotenv


# Initialize tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
tools = [wiki_tool, arxiv_tool]

# Groq API key (add a secure storage for deployment)
# GROQ_API_KEY = "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"

# Load environment variables from the .env file
load_dotenv()

# Access the GROQ_API_KEY variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Raise an error if the key is missing
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the .env file!")


llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It").bind_tools(tools=tools)
# print(f"Bound tools: {tools}")  # Debugging

# LangGraph setup with memory saver
memory = MemorySaver()

class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]

def call_model(state: MessagesState):

    
    print("call_model function called")


    """Invoke the LLM with current state."""
    messages = state['messages']
    # print(f"Calling model with messages: {messages}")  # Debugging
    response = llm.invoke(messages)
    print(f"Model response: {response}")  # Debugging

    # Check if response content is empty or contains tool-related content
    content = response.content
    if not content or '<tool-call>' in content or '</tool-call>' in content or '<tool_call>' in content or '</tool_call>' in content:
        user_message = "Hello."
        print(user_message)  # Terminal logging
        # Return the message to the chatbot interface
        return {"messages": [{"role": "assistant", "content": user_message}]}

    return {"messages": [response]}

def router_function(state: MessagesState) -> Literal["tools", END]:
    """Route based on whether tools are required."""
    messages = state['messages']
    last_message = messages[-1]
    print(f"Router function called with message: ")  # Debugging
    # Check if tool calls are in the last message
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    return END

# Define the graph workflow
workflow = StateGraph(MessagesState)

# Define ToolNode
tool_node = ToolNode(tools)

# Add nodes to the workflow
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# Define conditional routing from agent to tools
workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", router_function, {"tools": "tools", END: END})
workflow.add_edge("tools", "agent")

# Compile the workflow with memory saver
app = workflow.compile(checkpointer=memory)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def process_message(user_input, config=None):
#     """Process user input and generate a chatbot response with memory."""
#     input_data = {"messages": [("user", user_input)]}
#     config = config or {"configurable": {"thread_id": "1"}}
#     events = app.stream(input_data, config, stream_mode="values")

#     print("Process msg called")

#     response = None
#     for event in events:
#         # print(f"Event: {event}")  # Debugging
#         response = event["messages"][-1].content

#     if not response:
#         response = "I'm sorry, I couldn't process your request."
        
#     return response



def process_message(user_input, config=None):
    try:
        input_data = {"messages": [("user", user_input)]}
        config = config or {"configurable": {"thread_id": "1"}}
        events = app.stream(input_data, config, stream_mode="values")
        response = None
        for event in events:
            response = event["messages"][-1].content
        if not response:
            response = "I'm sorry, I couldn't process your request."
        return response
    except Exception as e:
        print(f"Error in process_message: {e}")
        return "An error occurred while processing your request."


        
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def get_memory(config=None):
    """Retrieve saved memory."""

    print("get_memory function called")


    config = config or {"configurable": {"thread_id": "1"}}
    return memory.get(config)

def call_tool(tool_name: str, query: str):

    print("call_tool function called")

    """Invoke a tool and provide fallback if no information is found."""
    try:
        # Simulate tool usage (replace with actual tool integration if needed)
        print(f"Calling tool: {tool_name} with query: {query}")
        return f"I found some information using {tool_name}: [Simulated Result for {query}]"
    except Exception as e:
        print(f"Error invoking tool: {e}")
        return "I'm sorry, I couldn't find information for your query. Can I assist with something else?"


# def process_message(user_input, config=None):
#     """Process user input and generate a chatbot response with fallback handling."""
#     input_data = {"messages": [("user", user_input)]}
#     config = config or {"configurable": {"thread_id": "1"}}
    
#     events = app.stream(input_data, config, stream_mode="values")

#     print("Process_message function called")


#     response = None
#     for event in events:
#         # Check if the model suggests using a tool
#         if "tool_call" in event.get("messages", [-1])[-1]:
#             tool_call = event["messages"][-1].tool_call
#             if tool_call and tool_call.get("function", {}).get("name"):
#                 # If the tool is relevant, handle it
#                 response = call_tool(
#                     tool_name=tool_call["function"]["name"],
#                     query=tool_call["parameters"]["query"],
                    
                    
                    
                
#                 )
#             else:
#                 # Fallback for invalid tool calls
#                 response = "It seems your question doesn't match my information. Here's a relevant response: How can I help further?"
#         else:
#             # Standard response handling
#             response = event["messages"][-1].content

#     # Default fallback for unhandled cases
#     if not response:
#         response = "I'm sorry, I couldn't process your request. Could you clarify?"

#     return response





# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def process_message(user_input, config=None):
#     """Process user input and generate a chatbot response with fallback handling."""
#     input_data = {"messages": [("user", user_input)]}
#     config = config or {"configurable": {"thread_id": "1"}}
#     events = app.stream(input_data, config, stream_mode="values")

#     print("Process_message function called")

#     response = None
#     for event in events:
#         # Check if the model suggests using a tool
#         if "tool_call" in event.get("messages", [-1])[-1]:
#             tool_call = event["messages"][-1].tool_call
#             if tool_call and tool_call.get("function", {}).get("name"):
#                 # If the tool is relevant, handle it
#                 response = call_tool(
#                     tool_name=tool_call["function"]["name"],
#                     query=tool_call["parameters"]["query"],
#                 )
#             else:
#                 # Fallback for invalid tool calls
#                 response = "It seems your question doesn't match my information. Here's a relevant response: How can I help further?"
#         else:
#             # Standard response handling
#             last_message = event["messages"][-1]
#             response = last_message.content if last_message else "I'm sorry, I couldn't process your request. Could you clarify?"

#     # Default fallback for unhandled cases
#     if not response:
#         response = "I'm sorry, I couldn't process your request. Could you clarify?"

#     return response
