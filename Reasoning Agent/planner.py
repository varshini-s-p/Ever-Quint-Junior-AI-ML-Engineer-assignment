from prompts import PLANNER_PROMPT

def plan_question(question: str, llm) -> str:
    prompt = PLANNER_PROMPT.format(question=question)
    plan = llm.generate(prompt)
    return plan.strip()
