from app.ingestion import load_and_split
from app.vectorstore import get_vectorstore

def run_ingestion():

  splits = load_and_split()
  vectorstore = get_vectorstore()
  vectorstore.add_documents(splits)

if __name__ == "__main__":
  run_ingestion()