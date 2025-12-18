import streamlit as st
import os
from utils import extract_text, chunk_text
from rag_pipeline import initialize_store, ask_question, summarize_documents

# -------------------- CONFIG --------------------
st.set_page_config(page_title="Simple RAG App")
st.title("📄 Knowledge-Based Chatbot (RAG)")

UPLOAD_DIR = "data/uploads"

# Ensure upload directory exists
if not os.path.isdir(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process document
    with st.spinner("Processing document and building knowledge base..."):
        text = extract_text(file_path)
        chunks = chunk_text(text)
        initialize_store(chunks)

    st.success("Document processed and knowledge base created.")
    st.subheader("📌 Document Summary")

summary_length = st.selectbox(
    "Select summary length",
    ["short", "medium", "long"]
)

if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        summary = summarize_documents(summary_length)
    st.write(summary)


    # -------------------- QUESTION INPUT --------------------
    question = st.text_input("Ask a question from the document")

    if question:
        with st.spinner("Generating answer..."):
            answer = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

else:
    st.info("Please upload a document to begin.")
