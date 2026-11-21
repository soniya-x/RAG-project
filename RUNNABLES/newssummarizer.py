from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# tools are runnables:invoke
search_tool=TavilySearchResults(max_result=5)

#model
llm_model=ChatMistralAI(model="mistral-small-2506")

#prompt
prompt=ChatPromptTemplate.from_template(
    """
You are a helpfull assistant
summrize the following news into clear bullet point
{news}
"""
)

chain= prompt| llm_model |StrOutputParser()

news_result=search_tool.run("Latest AI news of 2026")
result=chain.invoke({"news":news_result})
print(result)


print(search_tool.name)
print(search_tool.description)
print(search_tool.args)














