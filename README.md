# Task 4: Context-Aware Chatbot Using LangChain or RAG

## Objective
Build a conversational chatbot that can remember context and retrieve external information during conversations using a Retrieval-Augmented Generation (RAG) approach.

## Methodology / Approach
1. **Document Loading & Vectorization**: Uses LangChain's `TextLoader` to load a custom corpus (`knowledge_base.txt`). The text is split into chunks and embedded using `OpenAIEmbeddings`, then stored in a `FAISS` vector database.
2. **Conversation Chain**: Implements `ConversationalRetrievalChain` with `ConversationBufferMemory` to maintain chat history and provide context-aware responses.
3. **Deployment**: The user interface is built using `Streamlit`, providing a clean, interactive chat experience.

## Key Results / Observations
- The chatbot successfully grounds its answers in the provided `knowledge_base.txt`.
- Memory effectively allows for follow-up questions referencing past interactions.
- Streamlit's chat elements make for a seamless frontend implementation.

*Note: Requires `OPENAI_API_KEY` environment variable to run properly.*
