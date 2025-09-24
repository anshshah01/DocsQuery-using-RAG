import os
import pdfplumber

def load_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
        
def load_pdf_file(path: str) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def load_documents(folder="data"):
    """Return a list of document texts"""
    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".txt"):
            docs.append(load_text_file(path))   # ONLY the text
        elif file.endswith(".pdf"):
            docs.append(load_pdf_file(path))    # ONLY the text
    return docs
