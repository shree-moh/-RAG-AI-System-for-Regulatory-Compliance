def build_prompt(query, retrieved_texts):
    context = "\n---\n".join(retrieved_texts)
    prompt = (
        f"User Query: {query}\n"
        f"Relevant Context:\n{context}\n\n"
        "Provide a compliance-aware, actionable response:"
    )
    return prompt
