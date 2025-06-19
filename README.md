Clush AI Compliance RAG System
This repository contains a Retrieval Augmented Generation (RAG) system for regulatory compliance automation, developed for the Clush AI Modeler/Data Scientist assignment (2025.06.19).

📚 Project Overview
This project demonstrates an end-to-end RAG pipeline that:

Ingests and processes enterprise compliance data (regulator chat logs, meeting minutes, law texts) from a JSON file.

Embeds all texts for semantic search.

Retrieves relevant cases for any user query.

Generates context-aware, compliance-focused answers using a Large Language Model (LLM, e.g., Mistral 7B).

Applies guardrails and collects user feedback for continuous improvement.


![RAG Architecture️ Data

Source: gwajeyong_weonceondeiteo-1.json

Content: Simulated regulatory chat logs, internal meetings, and legal documents (all in Korean, anonymized for assignment use).

Note: All data is AI-generated and for assignment purposes only.

🏗️ System Architecture
Enterprise Data:
JSON file with all compliance records.

Ingest/Data Processing:
Loads and cleans data for downstream modules.

Embedding Model:
Converts texts to embeddings using Sentence Transformers.

Index/Vector Database:
Stores embeddings for fast semantic search (using FAISS).

Retrieval/Rank:
Finds the most relevant records for a user query.

Prompt Processing:
Combines query and retrieved context for the LLM.

LLM Inference:
Generates answers with Mistral 7B or similar.

Guardrail:
Filters/flags risky or non-compliant output.

Post-processing:
Formats and finalizes the response.

User Feedback & Fine-tuning:
Collects feedback for future model improvement (LoRA/QLoRA fine-tuning supported).

🚀 Getting Started
1. Clone the repository
bash
git clone
2. Install dependencies
bash
pip install -r requirements.txt
3. Add the dataset
Place gwajeyong_weonceondeiteo-1.json.

4. Run the main pipeline
bash
python main.py
5. (Optional) Fine-tune the LLM
See finetune_mistral.py for instructions.



