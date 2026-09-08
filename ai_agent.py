from dotenv import load_dotenv
import os
load_dotenv()

# Groq api key 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Tavily api key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# OpenAI api key
OPEN_API_KEY = os.getenv("OPEN_API_KEY")


# Setup Tools & LLM 

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


openai_llm = ChatOpenAI(model_name="gpt-4o-mini")
groq_llm = ChatGroq(model_name="openai/gpt-oss-120b")
search_tool = TavilySearchResults(max_results=2)


# Setup AI Agent with Search Tool Functionality 

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


system_prompt = "Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):

    if provider == "groq":
        llm = ChatGroq(model_name=llm_id)
    elif provider == "openai":
        llm = ChatOpenAI(model_name=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    
    agent = create_react_agent(model=groq_llm, tools=tools, prompt=system_prompt)


    state = {"messages": [("user", query)]}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages =[msg.content for msg in messages if isinstance(msg, AIMessage)]
    return ai_messages[-1]





