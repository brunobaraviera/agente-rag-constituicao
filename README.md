# 📜 Assistente Jurídico com RAG -- Constituição Brasileira de 1988

Sistema de Perguntas e Respostas baseado em **RAG (Retrieval-Augmented
Generation)** utilizando a Constituição Federal de 1988 como base de
conhecimento.

O projeto foi construído com arquitetura modular separando:

- Ingestão de dados
- Backend (API REST com FastAPI)
- Frontend (Interface Web com Streamlit)
- Banco vetorial (ChromaDB)
- LLM (OpenAI)

---

## 🎯 Objetivo

Demonstrar conhecimento em:

- Arquitetura de sistemas com LLM
- Implementação de RAG
- Separação frontend/backend
- Criação de API REST
- Persistência vetorial
- Boas práticas de organização de projeto

---

## 🧠 Como funciona

1.  O PDF da Constituição é carregado.
2.  O texto é dividido em chunks.
3.  São gerados embeddings.
4.  Os embeddings são armazenados no ChromaDB.
5.  O usuário faz uma pergunta via interface web.
6.  O backend:
    - Recupera trechos semanticamente relevantes.
    - Constrói um prompt dinâmico.
    - Consulta o modelo da OpenAI.
7.  A resposta é retornada para o frontend.

---

## 🏗️ Arquitetura

Usuário\
↓\
Streamlit (Frontend)\
↓ HTTP\
FastAPI (Backend)\
↓\
RAG Agent\
↓\
ChromaDB (Vector Store)\
↓\
OpenAI API

---

## 📂 Estrutura do Projeto

    agente-rag-constituicao/
    │
    ├── app/                 # Lógica principal do RAG
    │   ├── agent.py
    │   ├── retriever.py
    │   ├── vectorstore.py
    │   ├── ingestion.py
    │   └── config.py
    │
    ├── api/
    │   └── main.py          # Backend FastAPI
    │
    ├── frontend/
    │   └── app.py           # Interface Streamlit
    │
    ├── scripts/
    │   ├── run_ingestion.py # Script de indexação
    │   └── main.py          # Script CLI
    │
    ├── chroma_langchain_db/ # Banco vetorial persistido (não versionado)
    ├── requirements.txt
    └── README.md

---

## 🚀 Como Executar Localmente

### 1️⃣ Clone o repositório

    git clone https://github.com/brunobaraviera/agente-rag-constituicao.git
    cd agente-rag-constituicao

### 2️⃣ Crie e ative um ambiente virtual

Windows:

    python -m venv venv
    venv\Scripts\activate

Linux/Mac:

    python -m venv venv
    source venv/bin/activate

### 3️⃣ Instale as dependências

    pip install -r requirements.txt

### 4️⃣ Configure sua chave da OpenAI

Crie um arquivo `.env` na raiz do projeto:

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

### 5️⃣ Execute a ingestão dos dados

    python -m scripts.run_ingestion

Isso irá: - Carregar o PDF - Dividir o texto - Gerar embeddings -
Persistir no ChromaDB

### 6️⃣ Inicie o Backend (FastAPI)

    uvicorn api.main:app --reload

### 7️⃣ Inicie o Frontend (Streamlit)

Em outro terminal:

    streamlit run frontend/app.py

Abra no navegador:

http://localhost:8501

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13
- FastAPI
- Streamlit
- LangChain
- ChromaDB
- OpenAI API
- Pydantic
- Uvicorn

---

## 🧩 Principais Conceitos Aplicados

- Retrieval-Augmented Generation (RAG)
- Prompt Dinâmico
- Persistência Vetorial
- API REST
- Separação de Camadas
- Modularização
- Variáveis de Ambiente para Segurança

---

## 📎 Observações

Este projeto tem finalidade educacional e demonstrativa, com foco em arquitetura de sistemas com LLM e integração entre backend e frontend.

---

## 👨‍💻 Autor

Bruno Baraviera\
Desenvolvedor focado em IA, RAG e aplicações com LLM.
