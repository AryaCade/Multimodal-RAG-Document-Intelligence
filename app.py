import streamlit as st
import tempfile
import os

from pipeline import run_ingestion_pipeline
from rag.answer_generator import generate_final_answer

# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="Multi-Modal RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Multi-Modal RAG Chatbot")
st.caption("Supports text, tables & images using Unstructured + Gemini + Chroma")

# ---------------------- Session State ----------------------
if "db" not in st.session_state:
    st.session_state.db = None

if "uploaded_file_path" not in st.session_state:
    st.session_state.uploaded_file_path = None

# ---------------------- Sidebar ----------------------
with st.sidebar:
    st.header("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            st.session_state.uploaded_file_path = tmp.name

        st.success("PDF uploaded successfully")

    if st.button("🚀 Run Ingestion Pipeline"):
        if not st.session_state.uploaded_file_path:
            st.warning("Please upload a PDF first")
        else:
            with st.spinner("Processing document..."):
                st.session_state.db = run_ingestion_pipeline(
                    st.session_state.uploaded_file_path
                )
            st.success("Ingestion completed")

    st.divider()
    st.markdown("### ℹ️ Tech Stack")
    st.markdown("""
    - Unstructured.io  
    - Gemini Vision  
    - Chroma DB  
    - HuggingFace Embeddings  
    - Streamlit  
    """)

# ---------------------- Main Chat Area ----------------------
st.header("💬 Ask Questions")

query = st.text_input(
    "Enter your question",
    placeholder="e.g. What are the advantages of self-attention layers?"
)

if st.button("🔍 Get Answer"):
    if not st.session_state.db:
        st.warning("Please run ingestion first")
    elif not query.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Retrieving relevant chunks..."):
            retriever = st.session_state.db.as_retriever(search_kwargs={"k": 3})
            chunks = retriever.invoke(query)

        st.subheader("📌 Retrieved Chunks")
        for i, chunk in enumerate(chunks, 1):
            with st.expander(f"Chunk {i}"):
                st.write(chunk.page_content[:800] + "...")

        with st.spinner("Generating final answer..."):
            answer = generate_final_answer(chunks, query)

        st.subheader("✅ Final Answer")
        st.success(answer)

# ---------------------- Footer ----------------------
st.divider()
st.caption("Built as a Multimodal RAG System for AI Engineering Interviews")
