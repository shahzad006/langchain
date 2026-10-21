
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()

# st.header("Research Tool")

# user_input = st.text_input("Enter your research topic:")

# # Dynamic Prompt Template
# prompt = PromptTemplate.from_template(
#     "You are a research assistant. "
#     "Summarize the following topic in simple English "
#     f"using clear bullet points:\n\n{user_input}"
# )

# if st.button("Summarize"):
#     if user_input:
#         model = ChatGoogleGenerativeAI(
#             model="gemini-3.8-flash"
#         )

#         chain = prompt | model

#         result = chain.invoke({
#             "topic": user_input
#         })

#         st.write(result.content)
#     else:
#         st.warning("Please enter a research topic.")




# ---------------------------------------------------------------------------- #




from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate , load_prompt
from dotenv import load_dotenv
import streamlit as st


load_dotenv()


st.header("Research Tool")

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2
)


# Variable paper selection
paper_input = st.selectbox(
"Select a research paper:",
[
"Paper 1: The Impact of AI on Healthcare",
"Paper 2: Climate Change and Its Effects on Agriculture",
"Paper 3: Quantum Computing: The Next Frontier",
],
)




# Variable style
style_input = st.selectbox(
"Select a summary style:",
[
"Beginner-friendly",
"Technical",
"Concise",
]
)

# Variable length
length_input = st.selectbox(
"Select a summary length:",
[
"Short",
"Medium",
"Long",
]
)



# Load template

template = load_prompt("template.json")
    

# Fill the placeholders in the prompt template with the selected options
prompt = template.invoke(
{
"paper_input": paper_input,
"style_input": style_input,
"length_input": length_input
}
)









# LlM invocation and display the result
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.subheader("Research Summary")
    # st.write(result.content)
    st.markdown(result.content)