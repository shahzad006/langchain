import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

search = TavilySearch(
    max_results=5,
    topic="general"
)

response = search.invoke("Who is the current Prime Minister of Pakistan?")


print("*"*50)
print(response)
print("*"*50)
