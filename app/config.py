import os
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = "./data/constituicao-1988.pdf"
CHROMA_DIR = "./chroma_langchain_db"
COLLECTION_NAME = "constituicao_1988"

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-5-nano"

TOP_K = 4
TEMPERATURE = 0.2