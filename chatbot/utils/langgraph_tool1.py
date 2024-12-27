from typing import Annotated

from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage, ToolMessage
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langgraph.graph import StateGraph, START, END  

# NOTE: you must use langchain-core >= 0.3 with Pydantic v2
from pydantic import BaseModel

from typing_extensions import TypedDict # ----> Annotated, Literal


from langchain_groq import ChatGroq

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


class State(TypedDict):
    messages: Annotated[list, add_messages]
    # This flag is new
    ask_human: bool


class RequestAssistance(BaseModel):
    """Escalate the conversation to an expert. Use this if you are unable to assist directly or if the user requires support beyond your permissions.

    To use this function, relay the user's 'request' so the expert can provide the right guidance.
    """

    request: str

# Initialize tools
arxiv_wrapper = ArxivAPIWrapper(max_results=2, doc_content_chars_max=300)
wiki_wrapper = WikipediaAPIWrapper(max_results=2, doc_content_chars_max=300)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)
tools = [wiki_tool, arxiv_tool]


# Groq API key (add a secure storage for deployment)
GROQ_API_KEY = "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"
# llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It").bind_tools(tools=tools)
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It").bind_tools (tools + [RequestAssistance])

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    ask_human = False
    if (
        response.tool_calls
        and response.tool_calls[0]["name"] == RequestAssistance.__name__
    ):
        ask_human = True
    return {"messages": [response], "ask_human": ask_human}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools=tools))


def create_response(response: str, ai_message: AIMessage):
    return ToolMessage(
        content=response,
        tool_call_id=ai_message.tool_calls[0]["id"],
    )


def human_node(state: State):
    new_messages = []
    if not isinstance(state["messages"][-1], ToolMessage):
        # Typically, the user will have updated the state during the interrupt.
        # If they choose not to, we will include a placeholder ToolMessage to
        # let the LLM continue.
        new_messages.append(
            create_response("No response from human.", state["messages"][-1])
        )
    return {
        # Append the new messages
        "messages": new_messages,
        # Unset the flag
        "ask_human": False,
    }


graph_builder.add_node("human", human_node)

def select_next_node(state: State):
    if state["ask_human"]:
        return "human"
    # Otherwise, we can route as before
    return tools_condition(state)


graph_builder.add_conditional_edges(
    "chatbot",
    select_next_node,
    {"human": "human", "tools": "tools", END: END},
)

# The rest is the same
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("human", "chatbot")
graph_builder.add_edge(START, "chatbot")
memory = MemorySaver()
graph = graph_builder.compile(
    checkpointer=memory,
    # We interrupt before 'human' here instead.
    interrupt_before=["human"],
)



config = {"configurable": {"thread_id": "1"}}
events = graph.stream(
    {
        "messages": [
            ("user", "What is my name?")
            # ("user", "I'm learning LangGraph. Could you do some research on it for me?"),
            # ("user", "hillliouytgtdwdjwqhwd?")
        ]
    },
    config,
    stream_mode="values",
)
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()


# # from IPython.display import Image, display

# # try:
# #     display(Image(graph.get_graph().draw_mermaid_png()))
# # except Exception:
# #     # This requires some extra dependencies and is optional
# #     pass







# user_input = "I need some expert guidance for building this AI agent. Could you request assistance for me?"
# config = {"configurable": {"thread_id": "1"}}
# # The config is the **second positional argument** to stream() or invoke()!
# events = graph.stream(
#     {"messages": [("user", user_input)]}, config, stream_mode="values"
# )
# for event in events:
#     if "messages" in event:        event["messages"][-1].pretty_print()


