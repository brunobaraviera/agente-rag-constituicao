from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from app.config import CHAT_MODEL, TEMPERATURE
from app.retriever import retrieve_documents

def build_agent(vectorstore):

  @dynamic_prompt
  def prompt_with_context(request: ModelRequest):
    
    last_query = request.state["messages"][-1].text

    retrieved_docs = retrieve_documents(vectorstore, last_query)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

    system_message = (
      "Você é um assistente jurídico especializado na Constituição Brasileira de 1988.\n"
      "Responda apenas com base no contexto abaixo.\n"
      "Sempre cite o artigo correspondente.\n\n"
      f"{docs_content}"
    )

    return system_message
  
  model = ChatOpenAI(
    model = CHAT_MODEL,
    temperature = TEMPERATURE
  )

  agent = create_agent(model, tools = [], middleware = [prompt_with_context])

  return agent