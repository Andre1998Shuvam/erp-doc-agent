import fitz
import os
import pickle
import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def load_pdfs(folder="docs"):
    chunks = []
    for file in os.listdir(folder):
        if not file.endswith(".pdf"):
            continue
        doc = fitz.open(os.path.join(folder, file))
        for page_num, page in enumerate(doc):
            text = page.get_text()
            for i in range(0, len(text), 500):
                chunk = text[i:i+500]
                if len(chunk.strip()) > 100:
                    chunks.append({
                        "text": chunk,
                        "source": file,
                        "page": page_num + 1
                    })
    return chunks

def build_index():
    chunks = load_pdfs()
    print(f"Found {len(chunks)} chunks")
    texts = [c["text"] for c in chunks]
    
    vectorizer = TfidfVectorizer(max_features=1000)
    embeddings = vectorizer.fit_transform(texts).toarray().astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, "erp.index")
    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)
    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    print("Index built.")

if __name__ == "__main__":
    build_index()