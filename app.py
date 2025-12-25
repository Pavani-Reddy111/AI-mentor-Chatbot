import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# ------------------ BASIC SETUP ------------------
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not API_KEY:
    st.error("GOOGLE_API_KEY not found. Please add it to Streamlit Secrets.")
    st.stop()

st.set_page_config(page_title="AI Chatbot Mentor", page_icon="🤖")

# ------------------ SESSION STATE INIT ------------------
if "module" not in st.session_state:
    st.session_state.module = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = []

# ------------------ MODEL INIT (ONCE) ------------------
model = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=API_KEY,
    temperature=0.3
)

# ------------------ WELCOME SCREEN ------------------
if st.session_state.module is None:
    st.title("👋 Welcome to AI Chatbot Mentor")
    st.write("Your personalized AI learning assistant.")
    st.write("Please select a learning module to begin your mentoring session.")

    module = st.selectbox(
        "📌 Select a Module",
        [
            "Python",
            "SQL",
            "Power BI",
            "Exploratory Data Analysis (EDA)",
            "Machine Learning (ML)",
            "Deep Learning (DL)",
            "Generative AI (Gen AI)",
            "Agentic AI"
        ]
    )

    if st.button("Start Mentoring"):
        st.session_state.module = module

        system_prompt = f"""
You are an AI Mentor dedicated ONLY to the learning module: {module}.

Rules:
- Answer ONLY questions related to {module}.
- If the question is outside {module}, reply EXACTLY with:
"Sorry, I don’t know about this question. Please ask something related to the selected module."
- Be clear, structured, and beginner-friendly.
"""

        st.session_state.messages = [SystemMessage(content=system_prompt)]
        st.session_state.chat = []

        st.rerun()

# ------------------ MODULE CHAT INTERFACE ------------------
else:
    st.title(f"Welcome to {st.session_state.module} AI Mentor 🎯")
    st.write(f"I am your dedicated mentor for **{st.session_state.module}**.")
    st.write("How can I help you today?")

    # Display chat history
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask your question here")

    if user_input:
        # Show user message
        st.session_state.chat.append({"role": "user", "content": user_input})
        st.session_state.messages.append(HumanMessage(content=user_input))

        with st.chat_message("user"):
            st.write(user_input)

        # Invoke Gemini correctly
        response = model.invoke(st.session_state.messages)

        # Store AI response
        st.session_state.chat.append({"role": "ai", "content": response.content})
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("ai"):
            st.write(response.content)

    # ------------------ DOWNLOAD CHAT FEATURE ------------------
    if st.session_state.chat:
        conversation_text = ""
        for msg in st.session_state.chat:
            role = "User" if msg["role"] == "user" else "AI"
            conversation_text += f"{role}: {msg['content']}\n\n"

        st.download_button(
            label="📥 Download Conversation",
            data=conversation_text,
            file_name=f"{st.session_state.module}_Chat_History.txt",
            mime="text/plain"
        )
