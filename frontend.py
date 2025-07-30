# Step 1: Setup UI with streamlit(model provider, model,system prompt, web search, query)
import streamlit as st

st.set_page_config(page_title = "LangGraph Agent UI", layout = "wide") # page configurature and layout wide hoga
st.title("AI Chatbot Agents") # Title
st.write("Create and interact with the AI Agents !") # Description

# User can ask 
system_prompt = st.text_area("Define Your AI Agent:", height = 70 ,placeholder = "Type your system prompt here....")

# Here , we just provide models of grok and openai
MODEL_NAME_GROQ = ["llama-3.3-70b-versatile","mixtral-8x7b-32768"]
MODEL_NAME_OPENAI = ["gpt-4o-mini"]

# Provide the option , which is select by the user 
provider = st.radio("Select Provider:", ("Groq" , "OpenAI"))

# models choose by the users
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAME_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAME_OPENAI)

 # Give a web search option
allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query:", height = 150 ,placeholder = "Ask Anything!")

API_URL = "http://127.0.0.1:8000/chat" # backend url

if st.button("Ask Agent!"):
    if user_query.strip():

# Step 2 : Connect with backend via URL
        import requests
# Made a payload , information capture from UI by a user and send it to backend url
        payload = {
            "model_name":selected_model,
            "model_provider":provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search":allow_web_search
        }

        response = requests.post(API_URL , json=payload)
        # Here we will call the function which will return the response from the model
        #response = "Hi, This is a fixed dummy response"
        if response.status_code == 200: # Successful execution
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data['response']}")
        
