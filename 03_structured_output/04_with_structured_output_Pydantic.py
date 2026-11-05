from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel , Field


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")



class Review(BaseModel):
    key_themes: list[str] = Field(description="A list of key themes or topics mentioned in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: str = Field(description="The overall sentiment of the review (positive, negative, neutral)")
    pros: Optional[list[str]] = Field(description="A list of positive aspects or pros mentioned in the review")
    cons : Optional[list[str]] = Field(description="A list of negative aspects or cons mentioned in the review")

structured_output = model.with_structured_output(Review)


result = structured_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.""")

print(result)