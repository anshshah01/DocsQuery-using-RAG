import streamlit as st
from src.loader import load_documents
from src.embedder import build_faiss_index, embed_texts
from src.retriever import query_engine
import os

st.set_page_config(page_title="DocuQuery", layout="wide")

st.title("📄 DocuQuery - Smart Document Q&A")

# ---------------- Upload Documents ----------------
uploaded_files = st.file_uploader(
    "Upload PDF or TXT files", type=["pdf", "txt"], accept_multiple_files=True
)

# Save uploaded files to `data` folder
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(DATA_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success(f"Saved {len(uploaded_files)} file(s) to '{DATA_FOLDER}' folder")

# ---------------- Load & Index ----------------
if st.button("Load Documents and Build Index"):
    with st.spinner("📄 Loading documents..."):
        docs = load_documents(DATA_FOLDER)
        st.success(f"Loaded {len(docs)} document(s)")

    with st.spinner("🧠 Building FAISS index..."):
        index, chunks, metadata = build_faiss_index(docs)
        st.success("✅ Index built successfully!")

    st.session_state["index"] = index
    st.session_state["chunks"] = chunks
    st.session_state["metadata"] = metadata

# ---------------- Ask Questions ----------------
if "index" in st.session_state:
    question = st.text_input("Ask a question about your documents:")

    if st.button("Get Answer") and question.strip():
        with st.spinner("🤖 Searching..."):
            answer, sources = query_engine(
                question,
                st.session_state["index"],
                st.session_state["chunks"],
                st.session_state["metadata"],
            )
        st.subheader("Answer:")
        st.write(answer)

        st.subheader("Source Chunks:")
        for i, src in enumerate(sources):
            st.write(f"Chunk {i+1}:")
            st.text(src[:500] + "..." if len(src) > 500 else src)
