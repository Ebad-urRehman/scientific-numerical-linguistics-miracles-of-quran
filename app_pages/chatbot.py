import streamlit as st
from langchain_openai import OpenAI, OpenAIEmbeddings
import os
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import json
from datetime import datetime

def display_chatbot():
    # Set up OpenAI client and embeddings
    api_key = os.getenv("OPENAI_KEY")
    client = OpenAI(openai_api_key=api_key)
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    
    # Load FAISS vector index
    saved_library = FAISS.load_local("faiss_index_mathematics_quran", embeddings, allow_dangerous_deserialization=True)

    # # Display preview of documents
    # for i, doc in enumerate(saved_library.docstore._dict.values()):
    #     st.info(f"Document {i+1}: {doc.page_content[:100]}")
    #     if i >= 8:
    #         break
    
    st.markdown("### Specialized Chatbot RAG trained on Quranic books")
    st.info("- This is a specialized rag model trained on 10+ books, and articles on scientific, and mathematical study of Quran")
    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input from user
    query = st.chat_input("Ask a question about the Numerical Patterns in Qur'an:")

    if query:
        # Create retriever and QA chain
        retriever = saved_library.as_retriever()
        qna = RetrievalQA.from_chain_type(llm=client, chain_type="stuff", retriever=retriever)
        result = qna.invoke(query)

        # Save interaction in session history
        st.session_state.chat_history.append({
            "timestamp": datetime.now().isoformat(),
            "question": query,
            "answer": result["result"]
        })

        # Display result
        st.chat_message("user").write(query)
        st.chat_message("assistant").write(result["result"])

        # Optional: Save to a JSON file
        with open("chat_history.json", "w") as f:
            json.dump(st.session_state.chat_history, f, indent=2)

    # Display previous chat history
    for message in st.session_state.chat_history:
        st.chat_message("user").write(message["question"])
        st.chat_message("assistant").write(message["answer"])

display_chatbot()