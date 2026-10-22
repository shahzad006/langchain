from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import logging
logging.getLogger("langchain_google_genai").setLevel(logging.ERROR)

load_dotenv()




model = ChatGoogleGenerativeAI(model="gemini-3.8-flash",)

while True:
    user_input = input("Enter your question here: ")
    if user_input.lower() == "exit":
        break
    result = model.invoke(user_input)
    print("AI: ",result.text)
