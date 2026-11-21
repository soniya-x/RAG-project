from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
model=ChatMistralAI(model='mistral-small-2506')

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
class Movie(BaseModel):
    title:str
    release_year:Optional[int]
    genre:List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Information Extraction Assistant.

Your task is to analyze the given movie paragraph and extract the most useful information.

Guidelines:
- Extract only the information explicitly mentioned in the paragraph.
- Do not make assumptions or add extra information.
- If a field is not mentioned, write "Not Mentioned".
- Present the output in a neat and readable format.

Extract the following details:
- Movie Name
- Release Year
- Director
- Genre
- Main Cast
- Music Director/Composer
- IMDb Rating
- Duration
- Language
- Country
- Production Company
- Story/Plot
- Main Theme
- Important Keywords
- Critical Reception
- Awards (if mentioned)
- Box Office Collection (if mentioned)

Finally, write a Quick Summary in 2–3 sentences.
"""
        ),

        (
            "human",
            """
Extract the useful information from the following movie paragraph.

Paragraph:
{paragraph}
"""
        ),
    ]
)
para=input("Give your paragraph: ")
final_prompt=prompt.invoke(
    {"paragraph":para}
)


respose=model.invoke(final_prompt)
print(respose.content)
