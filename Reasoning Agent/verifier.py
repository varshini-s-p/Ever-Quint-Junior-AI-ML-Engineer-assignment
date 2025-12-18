import json
from prompts import VERIFIER_PROMPT

def verify_solution(question: str, solution: dict, llm) -> dict:
    prompt = VERIFIER_PROMPT.format(
        question=question,
        solution=solution
    )

    response = llm.generate(prompt)

    if "true" in response.lower():
        return {"passed": True, "issues": "Verified"}
    return {"passed": False, "issues": "Verification failed"}
