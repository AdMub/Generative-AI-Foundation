# ========================================
# LangChain + Hugging Face + Streamlit Chatbot (Beginner Friendly)
# ========================================

# Import all necessary libraries
from langchain import HuggingFaceHub  # Simpler for beginners than HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os

# ========================================
# STEP 1: Load Hugging Face API Key
# ========================================
load_dotenv()  # Load your .env file (must contain HUGGINGFACEHUB_API_TOKEN)
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# ========================================
# STEP 2: Streamlit User Interface
# ========================================
st.title("🤖 Simple LangChain + Hugging Face Chatbot")

# Input box for user's question
user_input = st.text_input("Ask me anything:")

# ========================================
# STEP 3: Only run when user types something
# ========================================
if user_input:

    # Create a structured prompt (system + user)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful and friendly AI assistant."),
        ("user", "{question}")
    ])

    # ========================================
    # STEP 4: Connect to a text-generation model on Hugging Face
    # ========================================
    # We'll use a smaller and supported model for your 16GB system
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-v0.3",  # ✅ works for text-generation
        model_kwargs={
            "temperature": 0.6,   # Creativity
            "max_new_tokens": 512 # Max length of response
        },
        huggingfacehub_api_token=HUGGINGFACE_TOKEN
    )

    # ========================================
    # STEP 5: Create the output parser
    # ========================================
    output_parser = StrOutputParser()

    # ========================================
    # STEP 6: Combine all parts into a chain
    # ========================================
    chain = prompt | llm | output_parser

    # ========================================
    # STEP 7: Generate and display the response
    # ========================================
    response = chain.invoke({"question": user_input})

    st.write("### 🤖 Response:")
    st.write(response)
