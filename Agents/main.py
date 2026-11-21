from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from pydantic import BaseModel

from agent import chat

app = FastAPI()

templates = Jinja2Templates(directory="template")

app.mount("/static", StaticFiles(directory="static"), name="static")


class UserInput(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
       return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
    


@app.post("/chat")
def chatbot(data: UserInput):

    response = chat(data.message)

    return {"response": response}