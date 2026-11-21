import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")
print(response.content)