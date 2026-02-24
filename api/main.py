from fastapi import FastAPI
from pydantic import BaseModel
from app.vectorstore import get_vectorstore
from app.agent import build_agent

app = FastAPI(title = "Assistente Jurídico API")

vectorstore = get_vectorstore()
agent = build_agent(vectorstore)

class Question(BaseModel):
  query: str

@app.post("/ask")
async def ask_question(question: Question):
  response = agent.invoke(
    {
      "messages": [
        {
          "role": "user", 
          "content": question.query
        }
      ]
    }
  )

  answer = {"answer": response["messages"][-1].content}

  return answer