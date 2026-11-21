from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from rich import print

# creating tool
@tool
def get_text_length(text:str)->int:
    """
    Return the number of character in a give text
    : 'hello how are you'
    """
    return len(text)


tools={
    "get_text_length":get_text_length
}

#model
llm=ChatMistralAI(model='mistral-small-2506')


# tool-binding : llm decides tool
llm_with_tool=llm.bind_tools([get_text_length])

messages=[]
prompt=input("You:")

query=HumanMessage(prompt)
messages.append(query)
# print(messages)

result= llm_with_tool.invoke(messages)
# print(result)
messages.append(result)  # human +AI message

if result.tool_calls:
    # print(result.tool_calls[0])
    tool_name=result.tool_calls[0]['name']
    tool_message=tools[tool_name].invoke(result.tool_calls[0])
    # print(tool_message)
    messages.append(tool_message)
    # print(messages)
    
result=llm_with_tool.invoke(messages)
print(result.content)


'''




Why are there two invoke() calls?

You can answer:

"The first invoke() allows the LLM to analyze the user's query and decide whether a tool is required. 
If a tool is needed, LangChain executes the tool. 
The second invoke() sends the tool's result back to the LLM so that 
it can generate a complete, user-friendly response.



1-Minute Interview Summary

"This code demonstrates manual tool calling in LangChain. 
First, a custom tool is created using the @tool decorator. 
Then the tool is registered with the Mistral model using bind_tools(). 
When the user asks a question, the LLM decides whether a tool is required.
if needed, it generates a tool call instead of a direct answer. 
LangChain executes the corresponding Python function, 
gets the result, and sends it back to the LLM. Finally, 
the LLM uses that result to generate a natural-language response.
This example helps us understand the internal working of tool calling before using agents, 
hich automate the same process."
'''






























































# # result=llm.invoke("Return the number of character in a give text: 'hello how are you' ")
# result2=llm_with_tool.invoke("Return the number of character in a give text: 'hello how are you' ")  # in nu,ber of token increases


# # print(result2.tool_calls)

# if result2.tool_calls:
#     tool_call=result2.tool_calls[0]

# # extracting tool agruments step 2-4
# tool_name=tool_call['name']
# tool_args=tool_call['args']


# tool_result=get_text_length.invoke(tool_args)

# # step 5: send result back to llm
# final_response=llm_with_tool.invoke(f'the lenght of  text  is {tool_result}')


# print(final_response.content)

# #tool-calling: the llm only suggestion the tool 



#  # tool-execution

 





# print("[red]Error[/red] ❌")
# print("[green]Success[/green] ✅")
# print("[blue]Information[/blue] ℹ️")





