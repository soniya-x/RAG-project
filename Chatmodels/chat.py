from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model

# model=init_chat_model("groq:openai/gpt-oss-120b")
# response=model.invoke("Give me a paragraph on machine learning ?")
# print(response.content)






# model = init_chat_model(
#     "llama-3.3-70b-versatile",
#     model_provider="groq"
# )
# response = model.invoke("What is cricket?")
# print(response.content)



# from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# response = model.invoke("What is AI?")
# print(response.content)


# MODEL CLASS
# from langchain_groq import ChatGroq
# model = ChatGroq(
#     model="llama-3.3-70b-versatile"
# )
# response = model.invoke("What is cricket?")
# print(response.content)

from langchain_mistralai import ChatMistralAI
model=ChatMistralAI(
      model= "mistral-small-latest",
      temperature=0.9,
      max_tokens=20
      
)
response=model.invoke("right a poem of ai in hienglish")
print(response.content)