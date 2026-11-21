from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings=OpenAIEmbeddings(
 model="text=embedding-3-large",
 dimensions=44
)

vector = embeddings.embed_query("What is AI?")
print(vector)

#--------------------------------------------------------------------------------------------

# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001"
# )

# vector = embeddings.embed_query("What is AI?")

#----------------------------------------------

# from langchain_mistralai import MistralAIEmbeddings

# embeddings = MistralAIEmbeddings(
#     model="mistral-embed"
# )
# vector = embeddings.embed_query("What is AI?")

#-------------------------------------------------------

