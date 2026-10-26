from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")


# Structured output using TypedDict  (Simple TypedDict)
class Review(TypedDict):
    summary: str
    sentiment: str


structured_output = model.with_structured_output(Review)


result = structured_output.invoke(""" The hardware is great, but the software is a bit buggy. Overall, I am satisfied with the product. """)

print(result)   