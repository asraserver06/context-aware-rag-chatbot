import streamlit as st
import os

# Set a dummy API key if none is provided, to prevent immediate crashes when importing
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "dummy_key")

from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory

st.title("Context-Aware Chatbot (RAG)")

@st.cache_resource
def load_knowledge_base():
    # Load document
    if not os.path.exists("knowledge_base.txt"):
        with open("knowledge_base.txt", "w") as f:
            f.write("DevelopersHub Corporation is a leading AI tech company.\n")
            f.write("Our main product is an automated ML platform.\n")
            f.write("The AI internship requires completing at least 3 advanced tasks.\n")
            f.write("The deadline for the internship tasks is 30th June, 2026.\n")
            
    loader = TextLoader("knowledge_base.txt")
    documents = loader.load()
    
    # Split text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    # Create embeddings and vector store
    # Note: Requires valid OPENAI_API_KEY to actually run
    try:
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(texts, embeddings)
        return vectorstore
    except Exception as e:
        st.error(f"Error initializing embeddings (Did you set OPENAI_API_KEY?): {e}")
        return None

vectorstore = load_knowledge_base()

if vectorstore:
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    try:
        llm = ChatOpenAI(temperature=0.7)
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=vectorstore.as_retriever(),
            memory=st.session_state.memory
        )
    except Exception as e:
        st.error(f"Error initializing LLM: {e}")
        qa_chain = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask a question about DevelopersHub:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if qa_chain:
            with st.chat_message("assistant"):
                try:
                    response = qa_chain({"question": prompt})
                    answer = response['answer']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error generating response: {e}")
