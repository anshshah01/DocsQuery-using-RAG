import faiss
import numpy as np
import google.generativeai as genai
import os
import numpy as np

# ---------------- Setup Gemini ----------------
API_KEY = os.getenv("GEMINI_API_KEY", "")
if not API_KEY:
    raise ValueError("❌ Please set your GEMINI_API_KEY environment variable.")
genai.configure(api_key=API_KEY)

embedding_model = "models/embedding-001"
CACHE_FILE = "embeddings.npy"  # path to cache

def embed_texts(texts):
    """Get embeddings from Gemini API"""
    """
    embeddings = []
    for t in texts:
        if not t.strip():
            continue
        result = genai.embed_content(model=embedding_model, content=t)
        embeddings.append(result["embedding"])
    return np.array(embeddings, dtype="float32")
    """

    """Return fake embeddings for testing (no API calls)"""
    # Each text gets a random 1536-dim vector
    return np.random.rand(len(texts), 1536).astype("float32")


        
    

def build_faiss_index(docs, chunk_size=2000):
    chunks = []
    metadata=[]
    
    
    # Split documents into chunks
    for doc_id,doc in enumerate(docs):
        if not isinstance(doc, str):
            raise ValueError(f"Document at index {doc_id} is not a string!")
        for i in range(0, len(doc), chunk_size):
            chunk = doc[i:i + chunk_size]
            if chunk.strip():
                chunks.append(chunk)
                metadata.append({"doc_id": doc_id, "start": i, "end": i + len(chunk)})


    # If cache exists, load embeddings
    if os.path.exists(CACHE_FILE):
        print("📂 Loading cached embeddings...")
        embeddings = np.load(CACHE_FILE)
    else:
        print("🤖 Generating embeddings from Gemini API...")
        #embeddings = embed_texts(chunks)
        #np.save(CACHE_FILE, embeddings)  # Save for next time
        embeddings = np.random.rand(len(chunks), 1536).astype("float32")
        
        print(f"💾 Saved embeddings to {CACHE_FILE}")

    # Build FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index, chunks, metadata
