import streamlit as st
import requests

st.title("🧠 Local Llama Chatbot (LangChain + FastAPI)")

# FastAPI backend URL
BACKEND_URL = "http://localhost:8000"

# ---------- Helper functions ----------

def get_openai_response(topic):
    try:
        response = requests.post(f"{BACKEND_URL}/essay/invoke", json={"input": {"topic": topic}}, timeout=30)
        if response.status_code == 200:
            return response.json()["output"]
        else:
            st.error(f"❌ Server returned {response.status_code}")
            st.text(response.text)
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Connection error: {e}")
        return None


def get_ollama_response(topic):
    try:
        response = requests.post(f"{BACKEND_URL}/poem/invoke", json={"input": {"topic": topic}}, timeout=30)
        if response.status_code == 200:
            return response.json()["output"]
        else:
            st.error(f"❌ Server returned {response.status_code}")
            st.text(response.text)
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Connection error: {e}")
        return None

# ---------- Streamlit UI ----------

tab1, tab2 = st.tabs(["Essay (OpenAI)", "Poem (Ollama)"])

with tab1:
    topic = st.text_input("Enter a topic for the essay:")
    if st.button("Generate Essay"):
        output = get_openai_response(topic)
        if output:
            st.success(output)

with tab2:
    topic2 = st.text_input("Enter a topic for the poem:")
    if st.button("Generate Poem"):
        output2 = get_ollama_response(topic2)
        if output2:
            st.success(output2)
