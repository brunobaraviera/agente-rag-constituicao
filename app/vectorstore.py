from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from app.config import EMBEDDING_MODEL, CHROMA_DIR, COLLECTION_NAME

def get_vectorstore():

  embeddings = OpenAIEmbeddings(model = EMBEDDING_MODEL)

  vectorstore = Chroma(
    collection_name = COLLECTION_NAME,
    embedding_function = embeddings,
    persist_directory = CHROMA_DIR
  )

  return vectorstore