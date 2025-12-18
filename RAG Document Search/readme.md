# Document Search and Summarization using RAG

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system that enables
document search and summarization using hybrid retrieval and Large Language Models.

## Features
- PDF/Text document ingestion
- Hybrid retrieval (TF-IDF + semantic embeddings)
- Context-aware question answering
- Adjustable-length summarization
- Evaluation using Hit@K and ROUGE metrics
- Streamlit-based user interface

## Tech Stack
- Python
- Streamlit
- FAISS
- Scikit-learn (TF-IDF)
- Ollama (Phi-3 Mini)
- ROUGE Score

## Setup Instructions
```bash
pip install -r requirements.txt

Run the Application
streamlit run app.py

Evaluation
python evaluate_search.py
python evaluate_summary.py

## Notes
Lightweight models were used to optimize memory usage for local deployment.

## Interface
A Streamlit-based web interface is provided for interacting with the system.

### Features
- Document upload (PDF/Text)
- Context-aware question answering
- Adjustable-length document summarization

### Local Setup
The interface can be launched locally using:
```bash
streamlit run app.py
