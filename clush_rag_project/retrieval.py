def retrieve(query, model, index, texts, top_k=3):
    q_emb = model.encode([query])
    from vector_db import search_vector_db
    return search_vector_db(q_emb, index, texts, top_k)
