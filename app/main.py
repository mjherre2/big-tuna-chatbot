import streamlit as st
from logic import answer_question

st.title("🧠 App Support Chatbot")
st.write("Ask me anything about using the web app!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.chat_input("Ask a question...")
if query:
    response = answer_question(query)
    st.session_state.chat_history.append((query, response))

for q, r in st.session_state.chat_history:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {r}")