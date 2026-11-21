from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

# MOdel
model=ChatMistralAI(model='mistral-small-2506')

# output parser
parser=StrOutputParser()

#  two different prompt template
short_prompt=ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

long_prompt=ChatPromptTemplate.from_template(
    "Explain {topic} in details"
)

#input
topic="Machine learning"

# formatted_short=short_prompt.format_messages(topic=topic)
# response_short=model.invoke(formatted_short)
# str_out=parser.parse(response_short.content)

#create parellel runnable
chain=RunnableParallel({
     "short": RunnableLambda(lambda x :x ['short']) | short_prompt | model | parser,
     "long": RunnableLambda(lambda x :x ['long']) | long_prompt | model | parser


})
# result =chain.invoke({"topic":"Machine Learning"})
result=chain.invoke({
    "short":{"topic":"Machine learning"},
    "long":{"topic":"Deep learning"}
})
print(result['short'])
print()
print(result['long'])

