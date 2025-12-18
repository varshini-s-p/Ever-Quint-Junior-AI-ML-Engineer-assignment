# Ever-Quint-Junior-AI-ML-Engineer-assignment
Complete AI/ML engineering assignment for EverQuint featuring algorithmic problem solving, optimization, RAG-based document search, and a multi-step reasoning agent with self-verification and LangChain orchestration.

Overview

This repository contains the complete technical assignment submission for EverQuint as part of the Junior AI/ML Engineer hiring process.
The repository includes four independent tasks, covering:
Algorithmic problem solving
Optimization and dynamic programming
Frontend visualization
Retrieval-Augmented Generation (RAG)
Multi-step reasoning agents with self-verification
Each task is implemented in a modular, production-style manner, follows the constraints provided in the problem statements, and includes clear documentation for evaluation.

Repository Structure
everquint-ai-engineering-assignment/
│
├── README.md                         # Common overview (this file)
│
├── task-1-water-tank/
│   ├── README.md
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│
├── task-2-max-profit/
│   ├── README.md
│   ├── max_profit.py
│   ├── max_profit_logic.py
│   ├── app.py
│   ├── requirements.txt
│
├── task-3-rag-document-search/
│   ├── README.md
│   ├── app.py
│   ├── evaluate_search.py
│   ├── evaluate_summary.py
│   ├── requirements.txt
│
├── task-4-reasoning-agent/
│   ├── README.md
│   ├── agent.py
│   ├── langchain_agent.py
│   ├── planner.py
│   ├── executor.py
│   ├── verifier.py
│   ├── prompts.py
│   ├── llm_client.py
│   ├── tests.py
│   └── logs/
│       └── example_runs.txt
│
└── .gitignore


Each task folder contains:

Its own README.md
Source code
Execution instructions
Assumptions and limitations
Tasks can be evaluated independently.

Task Summary
Task 1 – Water Tank (Trapping Rain Water)

Focus
Algorithmic reasoning
Frontend visualization
Edge case handling

Description
A frontend implementation of the classic Trapping Rain Water problem using Vanilla HTML, CSS, and JavaScript, including an SVG-based visualization of blocks and trapped water.

Key Highlights
Left Max – Right Max algorithm
Real-time visualization
No external dependencies

📁 Folder: task-1-water-tank/

Task 2 – Max Profit Problem

Focus
Optimization
Dynamic programming
Constraint-based reasoning

Description
Solves the Max Profit problem by determining the optimal mix of properties (Theatre, Pub, Commercial Park) to maximize earnings within a given time constraint.

Key Highlights
Dynamic Programming approach
Command-line and Streamlit implementations
Validated against all sample inputs from the problem statement

📁 Folder: task-2-max-profit/

Task 3 – Document Search & Summarization using RAG

Focus
Retrieval-Augmented Generation
NLP and evaluation metrics
Practical GenAI system design

Description
A RAG-based system that enables document ingestion, semantic search, and summarization using hybrid retrieval techniques and lightweight local LLMs.

Key Highlights
Hybrid retrieval (TF-IDF + embeddings)
FAISS indexing
ROUGE and Hit@K evaluation
Streamlit user interface

📁 Folder: task-3-rag-document-search/

Task 4 – Multi-Step Reasoning Agent with Self-Checking
Focus
Agentic reasoning
Planner–Executor–Verifier architecture
Safe AI behavior

Description
A reasoning agent that solves structured word problems using explicit multi-step planning, execution, and verification. The agent retries on failure and only returns verified answers.

Key Highlights
Planner → Executor → Verifier loop
Retry and safe-failure handling
Hidden chain-of-thought
LangChain-compatible orchestration
Deterministic local LLM stub (no billing required)

📁 Folder: task-4-reasoning-agent/

Technologies Used
Python
JavaScript (Vanilla)
HTML5 / CSS3
Streamlit
LangChain (lightweight orchestration)
FAISS
Scikit-learn (TF-IDF)
Ollama (Phi-3 Mini)
SVG for visualization

Notes & Assumptions
No paid APIs or billing dependencies are required
Lightweight local models are used where applicable
Emphasis is placed on correctness, verification, and clarity
Safe failure is preferred over unverified outputs

How to Evaluate
Each task folder contains a dedicated README.md with:
How to run the task
Design choices
Validation details
Known limitations
Reviewers can clone the repository and evaluate tasks individually.

Author
Varshini
Junior AI / ML Engineer Candidate
EverQuint Technical Assessment Submission

Final Confidence Statement
This repository demonstrates:
Strong problem-solving skills
Practical GenAI system design
Clean, modular engineering
Safe and verifiable reasoning behavior
