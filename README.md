# AI-Agent-Chatbot
This is a full-stack AI chatbot using LangGraph, FastAPI, and Streamlit. It supports Groq and OpenAI models, allows web search via Tavily, and offers a user-friendly interface to chat with an intelligent agent using custom prompts, dynamic model selection, and real time responses.

Users can define system prompts, select models dynamically, and interact with the AI in a friendly chat interface. It’s a great starting point for anyone exploring agentic AI, ReAct-style workflows, and lightweight LLM integrations.

## 🚀 Features
1. Choose between Groq (LLaMA3, Mixtral) and OpenAI (GPT-4o-mini) models
2. Use LangGraph to create ReAct-style AI agents
3. Optional web search powered by Tavily for up to date answers
4. Define your own system prompts to control agent behavior
5. Clean and responsive Streamlit frontend
6. FastAPI backend that connects the frontend to the agent logic

📁 Project Structure
File	Description
ai_agent.py	Core logic for LangGraph-based AI agent
backend.py	FastAPI app that receives requests and returns responses
frontend.py	Streamlit app for user interaction
requirements.txt	Python dependencies

⚙️ Installation

Navigate into the folder: cd langgraph-ai-chatbot

Install the dependencies: pip install -r requirements.txt

Set your API keys: 
OPENAI_API_KEY
GROQ_API_KEY
TAVILY_API_KEY (optional for web search)
You can set them using environment variables or in Streamlit secrets if deploying online.

▶️ Running the App Locally
Step 1: Start the FastAPI backend: python backend.py
Step 2: Launch the Streamlit frontend: streamlit run frontend.py
Visit http://localhost:8501 in your browser to use the chatbot.

🌐 Deployment
You can deploy the frontend on Streamlit Cloud and the backend on Render or Railway. For Streamlit-only deployment, include secrets in the app settings for your API keys.

🔐 API Keys Required
OpenAI (for GPT-4o-mini)
Groq (for LLaMA3, Mixtral models)
Tavily (optional, for real-time web search)

💡 Future Enhancements (Ideas)
Add chat memory (multi-turn context)
Support vector search or document-based RAG
User authentication for secure usage
Logging and analytics dashboard

