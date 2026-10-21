from langchain_core.prompts import PromptTemplate


# Template for dynamic prompt
template = PromptTemplate(


template=(
    """
"You are a research assistant. 
Summarize the following research paper in {style_input} style 
and provide a {length_input} summary:\n\n{paper_input}
"""
),
input_variables=["paper_input", "style_input", "length_input"] ,
validate_template=True


)


template.save("template.json")