# # if you dont use pipenv uncomment the following:
# # from dotenv import load_dotenv
# # load_dotenv()


# #Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
# import streamlit as st

# st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
# st.title("AI Chatbot Agents")
# st.write("Create and Interact with the AI Agents!")

# system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

# MODEL_NAMES_GROQ = ["openai/gpt-oss-120b"]
# MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# provider=st.radio("Select Provider:", ("Groq"))

# if provider == "Groq":
#     selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
# elif provider == "OpenAI":
#     selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

# allow_web_search=st.checkbox("Allow Web Search")

# user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")


# API_URL="http://127.0.0.1:8000/chat"
# if st.button("Ask Agent!"):
#     if user_query.strip():
#         #Step2: Connect with backend via URL
#         import requests

#         payload={
#             "model_name": selected_model,
#             "model_provider": provider,
#             "system_prompt": system_prompt,
#             "messages": [user_query],
#             "allow_search": allow_web_search
#         }

#         response=requests.post(API_URL, json=payload)
#         if response.status_code == 200:
#             response_data = response.json()
#             if "error" in response_data:
#                 st.error(response_data["error"])
#             else:
#                 st.subheader("Agent Response")
#                 st.markdown(f"**Final Response:** {response_data}")




import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

# Step 1: UI Inputs
system_prompt = st.text_area(
    "Define your AI Agent:", 
    height=70, 
    placeholder="Type your system prompt here..."
)

# Active models list
MODEL_NAMES_GROQ = ["openai/gpt-oss-120b"]
# MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
# else:
#     selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything!")

API_URL = "http://127.0.0.1:8000/chat"

# Step 2: Trigger Backend
if st.button("Ask Agent!"):
    if not user_query.strip():
        st.warning("Please enter a query first!")
    else:
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt if system_prompt.strip() else "You are a helpful assistant.",
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        with st.spinner("Agent is thinking..."):
            try:
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    response_data = response.json()
                    
                    if "error" in response_data:
                        st.error(response_data["error"])
                    else:
                        st.subheader("Agent Response")
                        # FIX: Clean key access for formatted Markdown display
                        clean_answer = response_data.get("response", "")
                        st.markdown(clean_answer)
                else:
                    st.error(f"Server Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")