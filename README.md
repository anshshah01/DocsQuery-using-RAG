docuquery/
│── data/                  # put your .pdf and .txt documents here
│   ├── sample1.pdf
│   ├── sample2.txt
│
│── src/
│   ├── __init__.py
│   ├── loader.py          # handles loading PDFs & text files
│   ├── embedder.py        # embeddings + FAISS index
│   ├── retriever.py       # retrieval + RAG pipeline
│   ├── llm_client.py      # Gemini API wrapper
│   ├── main.py            # entry point (CLI)
│
│── requirements.txt
│── README.md
