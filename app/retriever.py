from app.config import TOP_K

def retrieve_documents(vectorstore, query):
  
  if not query.strip():
    raise ValueError("Consulta vazia.")
  
  retrieved_docs = vectorstore.similarity_search(query, k = TOP_K)

  return retrieved_docs