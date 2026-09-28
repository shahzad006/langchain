from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()




model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.2, max_output_tokens=256)

result = model.invoke("What is the Capital of Pakistan")


print(result.content)



