from loader import load_documents
from embedder import build_faiss_index
from retriever import query_engine

def main():
    print("📄 Loading documents...")
    docs = load_documents("data")
    
    print("Loaded documents:", docs)
    print("Document types:", [type(d) for d in docs])

    index, chunks, metadata = build_faiss_index(docs)

    print(f"✅ Loaded {len(docs)} documents, {len(chunks)} chunks.")

    while True:
        q = input("\nAsk a question (:quit to exit): ")
        if q.lower() in [":quit", "quit", "exit"]:
            break
        answer, sources = query_engine(q, index, chunks, metadata)
        print("\nAnswer:", answer)
        print("\nSources:", sources)

if __name__ == "__main__":
    main()
