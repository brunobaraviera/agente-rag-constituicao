from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import PDF_PATH

def load_and_split():

  loader = PyPDFLoader(PDF_PATH)
  docs = loader.load()

  if not docs:
    raise ValueError("Nenhum documento carregado do PDF.")
  
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    add_start_index = True
  )
  splits = text_splitter.split_documents(docs)

  return splits