from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings

retriever = FAISS.load_local("app/vectorstore", OpenAIEmbeddings()).as_retriever()
memory = ConversationBufferMemory(return_messages=True)
llm = ChatOpenAI(model="gpt-4")

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

def get_chat_response(query: str):
    return chain.run(query)