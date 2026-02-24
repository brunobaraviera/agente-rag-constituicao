import streamlit as st
import requests

def disable():
  st.session_state.loading = True

def reset():
  st.session_state.loading = False
  st.session_state.query = ""

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title = "Assistente Constituição 1988")

st.subheader("Assistente Jurídico - Constituição Federal de 1988", text_alignment = "center")

if not "query" in st.session_state:
  st.session_state.query = ""

if not "loading" in st.session_state:
  st.session_state.loading = False

with st.form("question"):
  query = st.text_input(
    "Faça uma pergunta sobre a Constituição Brasileira: ", 
    placeholder = "Ex.: Qual é a idade mínima para ser eleito Senador?", 
    disabled = st.session_state.loading, 
    key = "query"
  )
  ask_button = st.form_submit_button("Enviar pergunta", disabled = st.session_state.loading, on_click = disable)

if ask_button and query:
  with st.spinner("Por favor, aguarde..."):
    response = requests.post(
      API_URL,
      json = {"query": query}
    )

  if response.status_code == 200:
    answer = response.json()["answer"]
    st.markdown("### Resposta")
    st.write(answer)
  else:
    st.error("Erro ao consultar API")

  reset_button = st.button("Fazer uma nova pergunta", on_click = reset)