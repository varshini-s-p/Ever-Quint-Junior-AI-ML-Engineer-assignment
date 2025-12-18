Multi-Step Reasoning Agent with Self-Checking
Overview

This project implements a multi-step reasoning agent that solves structured word problems using an explicit Planner → Executor → Verifier architecture.
The agent performs internal reasoning, verifies correctness, retries on failure, and only exposes a concise explanation and final answer to the user.

The design follows the interview assignment requirements and demonstrates safe, verifiable reasoning behavior.

How to Run
1. Install dependencies
pip install langchain langchain-core


(No paid APIs or billing required.)

2. Run the test suite
python tests.py


This executes predefined example questions and prints the final JSON output for each.

Project Structure
reasoning_agent/
│
├── agent.py              # Core planner–executor–verifier loop
├── langchain_agent.py    # LangChain-compatible wrapper
├── planner.py            # Planner logic
├── executor.py           # Execution logic
├── verifier.py           # Verification logic
├── llm_client.py         # Swappable LLM abstraction (local stub)
├── prompts.py            # Centralized prompts
├── tests.py              # Test cases
├── README.md
└── logs/
    └── example_runs.txt

Where Prompts Live

All prompts are centralized in:

prompts.py

This includes:

Planner prompt
Executor prompt
Verifier prompt

Prompts are not hard-coded inside logic files, making them easy to modify or replace.

Assumptions

A deterministic local LLM stub is used instead of a paid API (explicitly allowed in the assignment)

The agent prioritizes verification correctness over forced success

If verification fails after limited retries, the agent safely returns "status": "failed"

The architecture is designed to be easily extended with real LLM providers

Framework Usage (LangChain)

LangChain is used as a lightweight orchestration layer.

Core reasoning logic remains framework-agnostic in agent.py

langchain_agent.py demonstrates LangChain-style invocation

This ensures modularity and easy replacement with real LangChain-supported LLMs

Known Limitations

The fallback executor handles:
Arithmetic
Time calculations
Scheduling constraints
Some multi-dependency word problems may fail verification.
In such cases, the agent intentionally returns "failed" rather than producing an unverified answer.

Prompt Design Documentation
Prompt 1 — Planner Prompt

Purpose
To convert a natural language question into a concise, ordered reasoning plan.

Design Choice
Forces step-by-step decomposition
Prevents skipping reasoning steps
Keeps planning separate from execution

Why this works
Improves consistency across problem types
Makes verification easier

Prompt 2 — Executor Prompt
Purpose
To execute the plan and compute intermediate results.

Design Choice
Explicitly follows the planner’s steps
Produces intermediate values internally
Avoids generating user-facing explanations

What didn’t work well
Allowing free-form reasoning led to inconsistent outputs
Overly verbose execution reduced reliability

Prompt 3 — Verifier Prompt
Purpose
To independently validate the solution.

Design Choice
Re-checks constraints and calculations
Outputs structured pass/fail feedback
Drives retry or failure logic

Why this is critical
Prevents hallucinated answers
Demonstrates safe reasoning behavior

What I Would Improve with More Time
Integrate a real LLM backend
Improve handling of multi-dependency arithmetic
Expand constraint validation rules
Add more robust natural language parsing