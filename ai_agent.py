# Step 1: Setup API keys for Groq and Tavily
import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

# Set your API keys
os.environ["OPENAI_API_KEY"] = "Enter Your OPENAI API KEY"
os.environ["TAVILY_API_KEY"] = "Enter Your TAVILY API KEY"
os.environ["GROQ_API_KEY"] = "Enter Your GROQ API KEY"

# Step 2: Initialize models and tools
openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama3-70b-8192")
search_tool = TavilySearch(k=2)  # 'k' instead of 'max_results' in latest versions

# Step 3: Define function to get response from AI agent
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    # Add tools if search is allowed
    tools = [TavilySearch(k=2)] if allow_search else []

    # Create agent (no 'state_modifier' — not a valid param)
    agent = create_react_agent(model=llm, tools=tools)

    # Initial state with prompt + query
    initial_state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
    }

    # Call the agent
    response = agent.invoke(initial_state)

    # Extract AI messages
    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    return ai_messages[-1] if ai_messages else "No AI response"


# Example usage:
get_response_from_ai_agent(
    llm_id="llama3-70b-8192",
    query="Tell me about the trends in crypto markets",
    allow_search=True,
    system_prompt="Act as a smart and friendly AI assistant.",
    provider="Groq"
)
