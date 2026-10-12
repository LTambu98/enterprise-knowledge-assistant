from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

from chunking import chunk_markdown

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
DB_PATH = "chroma_db"
COLLECTION_NAME = "documenti_aziendali"


def build_index():
    # 1. carico il modello di embedding
    model = SentenceTransformer(MODEL_NAME)

    # 2. spezzo tutti i documenti in chunk
    chunks = []
    for file in Path("documenti").glob("*.md"):
        chunks.extend(chunk_markdown(file))

    # 3. trasformo ogni chunk in un vettore
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts).tolist()

    # 4. salvo tutto nel vector database
    client = chromadb.PersistentClient(path=DB_PATH)
    try:
        client.delete_collection(COLLECTION_NAME)  # riparto da zero, niente duplicati
    except Exception:
        pass
    collection = client.create_collection(
        COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )
    collection.add(
        ids=[f"{c['source']}::{c['section']}" for c in chunks],
        documents=texts,
        embeddings=embeddings,
        metadatas=[{"source": c["source"], "section": c["section"]} for c in chunks],
    )

    print(f"Indicizzati {len(chunks)} chunk. Dimensione dei vettori: {len(embeddings[0])}")


if __name__ == "__main__":
    build_index()