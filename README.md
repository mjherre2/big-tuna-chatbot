This is a chatbot that utilizes Ollama, local LLm, and RAG in order to answer questions and provide guidance regarding a web application.

In order to use this application you must install Ollama and run the llama3 LLM. This will use about 
- brew install ollama
- ollama pull llama3
- ollama run llama3

Start a venv and install requirements
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

Create the local knowledgebase
- python app/ingest.py

Start the UI part of the app!
- streamlit run app/main.py