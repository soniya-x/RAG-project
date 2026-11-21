

from dotenv import load_dotenv
load_dotenv()

import os
import requests
from tavily import TavilyClient
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

# ---------- Weather Tool ----------
@tool
def get_wheather(city: str) -> str:
    """Get current weather of a city."""

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(
        url,
        params={
            "q": city,
            "appid": API_KEY,
            "units": "metric",
        },
    )

    data = response.json()

    if int(data.get("cod", 0)) != 200:
        return data.get("message")

    return f"{city}: {data['weather'][0]['description']} {data['main']['temp']}°C"


# ---------- News Tool ----------
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def get_news(city: str):
    """Get latest city news"""

    response = tavily_client.search(
        query=f"Latest news about {city}",
        max_results=3,
    )

    results = response.get("results", [])

    if not results:
        return "No news found."

    output = ""

    for item in results:
        output += (
            f"{item['title']}\n"
            f"{item['content']}\n"
            f"{item['url']}\n\n"
        )

    return output


llm = ChatMistralAI(model="mistral-small-2506")

tools = {
    "get_wheather": get_wheather,
    "get_news": get_news,
}

llm = llm.bind_tools([get_wheather, get_news])


def chat(user_message):

    messages = [HumanMessage(content=user_message)]

    while True:

        ai = llm.invoke(messages)

        messages.append(ai)

        if ai.tool_calls:

            for tool_call in ai.tool_calls:

                tool = tools[tool_call["name"]]

                result = tool.invoke(tool_call["args"])

                messages.append(
                    ToolMessage(
                        content=result,
                        tool_call_id=tool_call["id"],
                    )
                )

        else:

            return ai.content






















# from dotenv import load_dotenv
# load_dotenv()

# import os
# import requests
# from langchain_mistralai import ChatMistralAI
# from langchain_core.tools import tool
# from langchain_core.messages import HumanMessage,SystemMessage,AIMessage ,ToolMessage
# from tavily import TavilyClient
# from rich import print


# #nows lets create some tools
# # weather tool
# @tool
# def get_wheather(city: str) -> str:
#     """Get current weather of a city."""

#     API_KEY = os.getenv("OPENWEATHER_API_KEY")

#     url = "https://api.openweathermap.org/data/2.5/weather"

#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric"
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     print(response.status_code)
#     print(data)

#     if int(data.get("cod", 0)) != 200:
#         return f"Error: {data.get('message')}"

#     temp = data["main"]["temp"]
#     desc = data["weather"][0]["description"]

#     return f"Weather in {city}: {desc}, {temp}°C"

# # print(get_wheather.invoke("bhopal"))

# # tavily new tools
# tavily_client=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# @tool
# def get_news(city:str)->str:
#     """ Get latest news about the city"""


#     response = tavily_client.search(
#         query=f"Latest news about {city}",
#         search_depth="basic",
#         max_results=3
#     )

#     results=response.get('results',[])

#     if not results:
#         return f"No recent news found for {city}."



#     news_list=[]

#     for r in results:
#         title=r.get("title",'No title')
#         url=r.get("url","")
#         snippet=r.get("content","")


#         news_list.append(
#             f'--{title}\n {url}\n {snippet[:100]}...'
#         )

#     return f"Latest news in {city} :\n\n" + "\n\n".join(news_list)

# # print(get_news.invoke("Dewas"))



# llm=ChatMistralAI(model='mistral-small-2506')

# tools={
#     'get_wheather':get_wheather,
#     'get_news':get_news
# }

# llm_with_tool=llm.bind_tools([get_wheather,get_news])

# #Agent loop -very important
# messages = []

# print("City Intelligence System")
# print("Type 'exit' to quit")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     # Add user message
#     messages.append(HumanMessage(content=user_input))

#     while True:

#         # Ask LLM
#         result = llm_with_tool.invoke(messages)

#         # Save AI response
#         messages.append(result)

#         # If tool call exists
#         if result.tool_calls:

#             for tool_call in result.tool_calls:

#                 tool_name = tool_call["name"]

#                 confirm = input(
#                     f"Agent wants to call '{tool_name}'. Approve? (yes/no): "
#                 )

#                 if confirm.lower() != "yes":
#                     print("Tool execution denied.")
#                     break

#                 # Execute tool
#                 tool_result = tools[tool_name].invoke(tool_call["args"])

#                 # Add tool output
#                 messages.append(
#                     ToolMessage(
#                         content=tool_result,
#                         tool_call_id=tool_call["id"]
#                     )
#                 )

#             # Call LLM again after tool execution
#             continue

#         # Final response
#         else:
#             print("\nAssistant:", result.content)
#             break      # <-- VERY IMPORTANT







