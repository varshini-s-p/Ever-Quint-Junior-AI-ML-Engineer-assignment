from prompts import EXECUTOR_PROMPT

def extract_final_answer(text: str) -> str:
    for line in text.splitlines():
        if "FINAL_ANSWER" in line:
            return line.split("FINAL_ANSWER:")[-1].strip()
    return ""

def execute_plan(question: str, plan: str, llm) -> dict:
    prompt = EXECUTOR_PROMPT.format(
        question=question,
        plan=plan
    )
    execution = llm.generate(prompt)

    return {
        "raw_execution": execution,
        "final_answer": extract_final_answer(execution)
    }
