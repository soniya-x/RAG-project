from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



#1. prompt template
prompt=ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms"
)
#2. MOdel
model=ChatMistralAI(model='mistral-small-2506')

#3 output parser
parser=StrOutputParser()


'''# step by step mnuall flow
formatted_prompt=prompt.format_messages(topic ="Machine Learning")

# call the model
response=model.invoke(formatted_prompt)

# parser the output mannually
final_output=parser.parse(response.content)

print(final_output)'''

# create runnables : sequenceRunnable
chain=prompt | model | parser
result=chain.invoke("Deep learning")
print(result)

