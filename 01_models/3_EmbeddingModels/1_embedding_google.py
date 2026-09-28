from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)
text = "LangChain is a framework for building applications with LLMs."

vector = model.embed_query(text)

print(vector[:10])
print(len(vector))