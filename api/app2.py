from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM as Ollama
from langserve import add_routes
import uvicorn

# Create the FastAPI app
app = FastAPI(
    title="Offline LangChain Server with Ollama",
    version="1.0",
    description="Runs entirely offline using Ollama + Llama 3.2"
)

# Initialize the local model
llm = Ollama(model="llama3.2:3b")

# Define prompts
essay_prompt = ChatPromptTemplate.from_template(
    "Write a clear 200-word essay about {topic}."
)
poem_prompt = ChatPromptTemplate.from_template(
    "Write a 200-word rhyming poem about {topic} suitable for a 7-year-old child."
)   

# Add routes
add_routes(app, essay_prompt | llm, path="/essay")
add_routes(app, poem_prompt | llm, path="/poem")

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
