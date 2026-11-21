from dotenv import load_dotenv
load_dotenv()
from langchain_core.runnables import RunnablePassthrough,RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI


# Model
model=ChatMistralAI(model='mistral-small-2506')

# Parser
parser = StrOutputParser()

# Prompt
code_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a code generator"),
    ("human","{topic}")
])

explain_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpfu; assistent who explains code in simple "),
    ("human","explain the following code in simple worrd :\n{code}")
])


# AI Pipeline
# seq_chain = code_prompt | model | parser | explain_prompt | model |parser
# result=seq_chain.invoke({"topic":"write a code of palindrome in python"})
# print(result)

seq= code_prompt | model | parser 

seq2=RunnableParallel(
    {"code":RunnablePassthrough(),
     "explanation":explain_prompt | model | parser
     }
)
chain=seq | seq2

result=chain.invoke({"topic": "Please write a code of palindroe in python"})
print(result['code'])
print(result['explanation'])




# # RunnablePassthrough
# chain = (
#     RunnablePassthrough.assign(
#         answer=answer_chain
#     )
# )

# result = chain.invoke({
#     "question": "What is Machine Learning?"
# })

# print(result)