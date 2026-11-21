from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "notes.txt"
splitter=CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)



data = TextLoader(str(file_path))

docs = data.load()
chunks=splitter.split_documents(docs)
for i in chunks:
    print(i.page_content)
    print()
  


print(len(chunks))
# print(docs[0].page_content)
# print(len(docs))
