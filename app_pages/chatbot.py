# import streamlit as st
# from langchain_openai import OpenAI, OpenAIEmbeddings
# import os
# from langchain_community.vectorstores import FAISS
# from langchain.chains import RetrievalQA
# import json
# from datetime import datetime

# def display_chatbot():
#     # Set up OpenAI client and embeddings
#     api_key = st.secrets["api_key"]["openai"] 

#     client = OpenAI(openai_api_key=api_key)
#     embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    
#     # Load FAISS vector index
#     saved_library = FAISS.load_local("faiss_index_mathematics_quran", embeddings, allow_dangerous_deserialization=True)

#     # # Display preview of documents
#     # for i, doc in enumerate(saved_library.docstore._dict.values()):
#     #     st.info(f"Document {i+1}: {doc.page_content[:100]}")
#     #     if i >= 8:
#     #         break
    
#     st.markdown("### Specialized Chatbot RAG trained on Quranic books")
#     st.info("- This is a specialized rag model trained on 10+ books, and articles on scientific, and mathematical study of Quran")
#     # Initialize session state for chat history
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     # Input from user
#     query = st.chat_input("Ask a question about the Numerical Patterns in Qur'an:")

#     if query:
#         # Create retriever and QA chain
#         retriever = saved_library.as_retriever()
#         qna = RetrievalQA.from_chain_type(llm=client, chain_type="stuff", retriever=retriever)
#         result = qna.invoke(query)

#         # Save interaction in session history
#         st.session_state.chat_history.append({
#             "timestamp": datetime.now().isoformat(),
#             "question": query,
#             "answer": result["result"]
#         })

#         # Display result
#         st.chat_message("user").write(query)
#         st.chat_message("assistant").write(result["result"])

#         # Optional: Save to a JSON file
#         with open("chat_history.json", "w") as f:
#             json.dump(st.session_state.chat_history, f, indent=2)

#     # Display previous chat history
#     for message in st.session_state.chat_history:
#         st.chat_message("user").write(message["question"])
#         st.chat_message("assistant").write(message["answer"])

# display_chatbot()


import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import json
from datetime import datetime

# Load FAISS index and document chunks
index = faiss.read_index("models/quran_math_index.faiss")
with open("models/quran_math_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load SentenceTransformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize OpenAI client
api_key = st.secrets["api_key"]["openai"]
client = OpenAI(api_key=api_key)

# Function to retrieve context from vector index
def retrieve_context(query, top_k=10):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), top_k)
    return [chunks[i] for i in I[0]]

# Function to generate answer from OpenAI
def ask_gpt(query, context):
    context_text = "\n\n".join(context)
    system_prompt = (
        "You are an expert assistant in Qur'anic mathematics, "
        "Islamic studies, and educational content creation. "
        "Your task is to explain concepts clearly, like a teacher."
    )

    user_prompt = f"""
Use the following context from books related to the Qur'an and mathematics to answer the user's question.

- Be thorough, detailed, and clear.
- Break down the answer into sections with headings.
- Include bullet points, examples, and references from the context if possible.
- If applicable, show information in tables using Markdown format.
- Ensure explanations are easy for high school or college students to understand.

Context:
{context_text}

Question: {query}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        temperature=0.3,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit chatbot UI
st.title("📘 Qur'an and Mathematics QA Chatbot")
st.info("- This is a specialized model trained on Qur'anic books and mathematical studies.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
query = st.chat_input("Ask a question about the Numerical Patterns in Qur'an:")

if query:
    # Retrieve and respond
    with st.spinner("🔍 Retrieving context and generating answer..."):
        context = retrieve_context(query)
        answer = ask_gpt(query, context)

    # Save chat interaction
    st.session_state.chat_history.append({
        "timestamp": datetime.now().isoformat(),
        "question": query,
        "answer": answer
    })

    # Display current chat exchange
    st.chat_message("user").write(query)
    st.chat_message("assistant").write(answer)

    # Optional: Save to file
    with open("chat_history.json", "w") as f:
        json.dump(st.session_state.chat_history, f, indent=2)

# Display previous chat history
for message in st.session_state.chat_history:
    st.chat_message("user").write(message["question"])
    st.chat_message("assistant").write(message["answer"])
