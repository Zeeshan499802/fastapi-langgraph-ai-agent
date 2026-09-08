# 🤖 LangGraph & FastAPI Provider AI Agent

A full-stack, customizable AI Agent application built with **LangGraph**, **LangChain**, **FastAPI**, and **Streamlit**. 

This system supports dynamic LLM selection (Groq and OpenAI), configurable system prompts, real-time web search integration via **Tavily Search API**, and serves a clean REST API backend with an interactive web UI.

---

## 🌟 Key Features

* **Multi-Provider Support:** Switch dynamically between Groq (`llama-3.3-70b-versatile`, `llama3-8b-8192`) and OpenAI (`gpt-4o-mini`).
* **Autonomous Web Search:** Real-time web capabilities using **Tavily Search** for live information retrieval.
* **LangGraph Orchestration:** Utilizes stateful ReAct agent workflow (`create_react_agent`) for tool calling and reasoning.
* **FastAPI Backend:** Lightweight, fast RESTful API endpoints with Pydantic schema validation.
* **Streamlit UI:** Clean interactive interface allowing users to define agent behavior, choose LLM models, toggle search, and view formatted Markdown responses.

---

## 🏗️ Architecture

┌─────────────────┐       HTTP / JSON       ┌───────────────────┐
│   Streamlit     │ ──────────────────────> │    FastAPI        │
│   Frontend      │ <────────────────────── │    Backend        │
└─────────────────┘                         └─────────┬─────────┘
│
▼
┌───────────────────┐
│  LangGraph Agent  │
└─────────┬─────────┘
│
┌─────────────┴─────────────┐
▼                           ▼
┌───────────────────┐       ┌───────────────────┐
│     Groq /        │       │   Tavily Web      │
│   OpenAI LLMs     │       │   Search Tool     │
└───────────────────┘       └───────────────────┘


---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frameworks:** LangGraph, LangChain, FastAPI, Streamlit
* **LLM Providers:** Groq API, OpenAI API
* **Search Engine:** Tavily Search API
* **Server:** Uvicorn

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python installed and API keys for the services:
* [Groq API Key](https://console.groq.com/)
* [OpenAI API Key](https://platform.openai.com/)
* [Tavily API Key](https://tavily.com/)

### 2. Environment Setup

Clone the repository and set up a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

