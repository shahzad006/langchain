import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Get API Key
groq_api_key = os.getenv("GROQ_API_KEY")

print("API Key Loaded:", groq_api_key is not None)

# Groq Model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

response = llm.invoke("Hello, how are you?")

print(response.content)