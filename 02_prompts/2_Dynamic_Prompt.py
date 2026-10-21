
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Tool")

user_input = st.text_input("Enter your research topic:")

# Dynamic Prompt Template
prompt = PromptTemplate.from_template(
    "You are a research assistant. "
    "Summarize the following topic in simple English "
    f"using clear bullet points:\n\n{user_input}"
)

if st.button("Summarize"):
    if user_input:
        model = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash"
        )

        chain = prompt | model

        result = chain.invoke({
            "topic": user_input
        })

        st.write(result.content)
    else:
        st.warning("Please enter a research topic.")
