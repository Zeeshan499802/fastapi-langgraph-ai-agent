# Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List, Optional

class RequestModel(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Setup AI Agent from FrontEnd Request 
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
ALLOWED_MODEL_NAMES = ["gpt-4o-mini", "openai/gpt-oss-120b"]



app=FastAPI(title="LangGraph AI Agent", description="LangGraph AI Agent for LLMs", version="1.0")


@app.get("/")
def home():
    return {"message": "LangGraph AI Agent API is running"}


@app.post("/chat")
def agent_endpoint(request: RequestModel):
    """
    API Endpoint to interact with the chatbot using langGraph and search tools. It dynamically selects the model specified in the request. 
    """

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid model name. Kindly select a valid AI model"}

    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages[-1],
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider
    )
    return {"response": response}

