from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model=MistralAIEmbeddings(
    model="mistral-embed"
)

vectorstore=Chroma(
    persist_directory="chroma_db1",
    embedding_function=embedding_model
)

retriever=vectorstore.as_retriever(
    search_type='mmr',
    serch_kwargs={
        "k":4,
        "fetch_k":10,
       " lambda_mult":0.5
    }
)
llm=ChatMistralAI(model="mistral-small-2506")


#prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)
print("Rag system created")

print("press 0 to exit ")
while True:
    query=input("You: ")
    if query=="0":
        break

    docs=retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt=prompt.invoke({
        "context":context,
        "question":query
    })
    response=llm.invoke(final_prompt)
    print(f"\n AI: {response.content}")






























# from dotenv import load_dotenv
# from langchain_community.document_loaders import TextLoader,PyPDFLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# load_dotenv()

# # Prompt
# template = ChatPromptTemplate.from_messages([
#     ("system", "You are an AI that summarizes the text."),
#     ("human", "{data}")
# ])



# # Model
# model = ChatMistralAI(
#     model="mistral-small-2506"
# )

# # # Format prompt
# # prompt = template.format_messages(
# #     data=docs[0].page_content
# # )

# # Format pdf prompt
# prompt = template.format_messages(
#     data=pdfdocs
# )


# # Invoke model
# result = model.invoke(prompt)

# print(result.content)