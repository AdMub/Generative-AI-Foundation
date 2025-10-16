import streamlit as st
import requests

# Local backend URL
BASE_URL = "http://localhost:8000"

# Functions to call local endpoints
def generate_text(endpoint, topic):
    url = f"{BASE_URL}/{endpoint}/invoke"
    payload = {"input": {"topic": topic}}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get("output", "No output received.")
    else:
        return f"Error {response.status_code}: {response.text}"

# Streamlit UI
st.set_page_config(page_title="Local Llama Chatbot", page_icon="🦙", layout="centered")

st.title("🦙 Local Llama Chatbot (Offline)")
st.write("Powered by **Ollama + LangChain + Streamlit** — runs fully offline!")

# Sidebar mode selection
mode = st.sidebar.selectbox("Select Mode", ["Essay", "Poem"])
st.sidebar.markdown("---")
st.sidebar.info("Ensure your FastAPI app is running at `http://localhost:8000`.")

# Input area
topic = st.text_area("Enter a topic or question:", placeholder="e.g., Climate Change in Nigeria")

if st.button("Generate"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")
    else:
        with st.spinner("Generating with Local Llama..."):
            endpoint = "essay" if mode == "Essay" else "poem"
            result = generate_text(endpoint, topic)
            st.success("✅ Done!")
            st.markdown(f"### ✨ {mode} on: *{topic}*")
            st.write(result)

# Footer
st.markdown("---")
st.caption("Built by Mubarak • Runs entirely offline 🚀")
