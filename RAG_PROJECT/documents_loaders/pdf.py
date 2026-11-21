from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter,RecursiveCharacterTextSplitter
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "GRU.pdf"
data=PyPDFLoader(str(file_path))
pdfdocs=data.load() 

# spliter=TokenTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=10
# )

spliter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=10
)

chunks=spliter.split_documents(pdfdocs)
for i in chunks:
  print(chunks[i].page_content)
  print()

# print(len(pdfdocs))
# print(pdfdocs[14])