from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import logging
logging.getLogger("langchain_google_genai").setLevel(logging.ERROR)

load_dotenv()




model = ChatGoogleGenerativeAI(model="gemini-3.8-flash",)

chat_history = [
    SystemMessage(content="You are a helpful assistant."),

]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)


print("Exiting the chat. Goodbye!")