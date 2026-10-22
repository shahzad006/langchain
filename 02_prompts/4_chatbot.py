from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import logging
logging.getLogger("langchain_google_genai").setLevel(logging.ERROR)

load_dotenv()




model = ChatGoogleGenerativeAI(model="gemini-3.8-flash",)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(("user", user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.text)
    print("AI: ",result.text)


print("Exiting the chat. Goodbye!")