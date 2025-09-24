from .embedder import build_faiss_index, embed_texts
from .llm_client import ask_gemini

def query_engine(question, index, chunks, metadata, top_k=3):
    # Get embeddings for the question
    q_emb = embed_texts([question])  # just call the function

    # Search FAISS index
    distances, indices = index.search(q_emb, top_k)

    context_parts = []
    used_sources = []

    for i in indices[0]:
        context_parts.append(chunks[i])
        used_sources.append(metadata[i])

    context = "\n\n".join(context_parts)

    prompt = f"""
You are DocuQuery, an AI assistant. Use the provided context to answer.

Context:
{context}

Question:
{question}

Answer only from the context. If not found, say "Not found in the documents."
"""

    answer = ask_gemini(prompt)
    return answer, used_sources
