import faiss
import numpy as np

def build_vector_db(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search_vector_db(query_embedding, index, texts, top_k=3):
    D, I = index.search(np.array(query_embedding), top_k)
    return [texts[i] for i in I[0]]
