from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
from langchain_mistralai import ChatMistralAI
model=ChatMistralAI(model='mistral-small-2506')

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
 {format_instructions}


"""
        ),

        (
            "human",
            """Paragraph: {paragraph}
         """
        ),
    ]
)


para=input("Give your paragraph: ")

final_prompt=prompt.invoke(
    {"paragraph":para,
     "format_instructions":parser.get_format_instructions()
     }
)


respose=model.invoke(final_prompt)
print(respose.content)
