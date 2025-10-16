from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
#from langchain_ollama import OllamaLLM as Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Load API key from .env file (optional)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Create the FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server for LangChain + Ollama"
)

# Create model instances
openai_model = ChatOpenAI()
ollama_model = Ollama(model="llama3.2:3b")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 200 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 7-year-old child with 200 words.")

# Add routes
add_routes(app, prompt1 | openai_model, path="/essay")
add_routes(app, prompt2 | ollama_model, path="/poem")

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
