
from data_ingest import load_cases, extract_texts
from embedding import embed_texts
from vector_db import build_vector_db
from retrieval import retrieve
from prompt_processing import build_prompt
from llm_inference import load_mistral_model, generate_response
from guardrail import apply_guardrail
from postprocess import postprocess_response
from feedback import collect_feedback

def main():
    print("Loading data...")
    data = load_cases('과제용_원천데이터.json')
    texts = extract_texts(data)

    print("Embedding texts...")
    embeddings, embed_model = embed_texts(texts)
    import numpy as np
    embeddings = np.array(embeddings)
    index = build_vector_db(embeddings)

    user_query = input("Enter your compliance-related question: ")

    print("Retrieving relevant context...")
    retrieved = retrieve(user_query, embed_model, index, texts)
    prompt = build_prompt(user_query, retrieved)

    print("Loading Mistral 7B model (may take a few minutes)...")
    model, tokenizer = load_mistral_model(quantize=False)

    # Enable GPU if available
    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    print("Generating response...")
    llm_output = generate_response(prompt, model, tokenizer)

    print("Applying guardrails...")
    safe_output = apply_guardrail(llm_output)

    final_output = postprocess_response(safe_output)
    print("\nFinal AI Response:\n", final_output)

    # Collect feedback (optional)
    if collect_feedback(final_output):
        print("Thank you for your feedback! This will be used to improve the system.")

if __name__ == "__main__":
    main()