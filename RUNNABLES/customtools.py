from langchain_core.tools import tool

@tool # decorator for creating tools
def get_greeting(name:str)->str: # type hints
    """
    Generate the greeting message for a user   #docstring
    """
    return f"hello {name} ,welcome to the AI world"


result=get_greeting.invoke({"name":"soniya"})
print(result)


# feature
# print(get_greeting.name)
# print(get_greeting.description)
# print(get_greeting.args)