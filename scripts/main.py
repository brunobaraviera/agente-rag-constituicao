from app.ingestion import load_and_split
from app.vectorstore import get_vectorstore
from app.agent import build_agent

def main():

  vectorstore = get_vectorstore()
  agent = build_agent(vectorstore)

  while True:
    query = input("\nFaça uma pergunta sobre a Constituição Brasileira de 1988 (ou digite 'sair' para sair): ")

    if query.lower() == "sair":
      break

    try:
      for step in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode = "values"
      ):
        step["messages"][-1].pretty_print()

    except Exception as e:
      print(f"Erro ao executar o agente: {e}")

if __name__ == "__main__":
  main()