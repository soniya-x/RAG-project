from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage,HumanMessage

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates=Jinja2Templates(directory="templates")

model=ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.9
)

class Chat(BaseModel):
    message:str
    mode:str

@app.get("/",response_class=HTMLResponse)
async def home(request:Request):

   return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={}
)

@app.post("/chat")
async def chat(data:Chat):

    prompts={

        "angry":"You are an angry AI assistant.",

        "funny":"You are a funny AI assistant.",

        "sad":"You are a sad AI assistant.",

        "helpful":"You are a helpful AI assistant."

    }

    messages=[

        SystemMessage(content=prompts[data.mode]),

        HumanMessage(content=data.message)

    ]

    response=model.invoke(messages)

    return {

        "reply":response.content

    }