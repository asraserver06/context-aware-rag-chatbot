# 🤖 Context-Aware RAG Chatbot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)

A powerful Retrieval-Augmented Generation (RAG) chatbot designed for the **DevelopersHub AI/ML Engineering Internship**. This application leverages large language models and a custom vector database to provide highly accurate, context-aware responses to user queries.

## 🚀 Project Overview

Standard LLMs lack knowledge of private or highly specific company data. This project solves that by implementing a RAG architecture using LangChain, allowing the chatbot to read a custom knowledge base, remember conversation history, and synthesize precise answers.

### Key Features
- **Retrieval-Augmented Generation**: Uses `FAISS` for fast similarity search across embedded document chunks.
- **Contextual Memory**: Integrates `ConversationBufferMemory` so the bot remembers previous questions and answers during the chat session.
- **Sleek UI**: Built entirely with `Streamlit` for a seamless, interactive, chat-like frontend.
- **Dynamic Chunking**: Uses LangChain's `CharacterTextSplitter` to optimize long documents for LLM context windows.

## 📂 Repository Structure

```text
context-aware-rag-chatbot/
├── app.py                 # Streamlit UI and LangChain RAG architecture
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/asraserver06/context-aware-rag-chatbot.git
cd context-aware-rag-chatbot
```
2. Install the necessary packages:
```bash
pip install -r requirements.txt
```
3. Export your OpenAI API Key (required for embeddings and the LLM):
```bash
# On Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

## 💻 Usage Instructions

To launch the chatbot interface, simply run:

```bash
streamlit run app.py
```
This will open a new browser tab where you can interact directly with the context-aware assistant!

## 🤝 Acknowledgments
Completed as part of the **DevelopersHub Corporation AI/ML Engineering Advanced Internship Tasks** (Task 4).
