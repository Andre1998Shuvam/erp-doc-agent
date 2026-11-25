import faiss
import pickle
import requests

def search(query, k=3):
    index = faiss.read_index("erp.index")
    with open("chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    
    query_embedding = vectorizer.transform([query]).toarray().astype("float32")
    _, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]

def ask(query):
    chunks = search(query)
    context = "\n\n".join([
        f"[Source: {c['source']}, Page {c['page']}]\n{c['text']}"
        for c in chunks
    ])
    prompt = f"""You are an ERP expert. Answer ONLY from the context below.
If you don't know, say "Not found in docs".

Context:
{context}

Question: {query}

Answer with citations like [Source: file, Page X]"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.1:8b", "prompt": prompt, "stream": False}
    )
    return response.json()["response"], chunks