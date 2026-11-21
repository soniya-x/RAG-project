# load pdf
# split into chunks 
# create the embeddiing 
# store into chroma 

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader,PyPDFLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
load_dotenv()



#load PDF file
pdfloader=PyPDFLoader("documents_loaders/deeplearning.pdf")
pdfdocs=pdfloader.load()


# text-splitter
splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks=splitter.split_documents(pdfdocs)


# create embedding models
embedding_model= MistralAIEmbeddings(
    model="mistral-embed",
)

#create vector store
vectorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db1"

)


