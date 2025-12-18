def solve(question: str) -> dict:
    ...
def empty_response():
    return {
        "answer": "",
        "status": "failed",
        "reasoning_visible_to_user": "",
        "metadata": {
            "plan": "",
            "checks": [],
            "retries": 0
        }
    }
from llm_client import LocalLLMClient
from planner import plan_question
from executor import execute_plan
from verifier import verify_solution

MAX_RETRIES = 2

def solve(question: str) -> dict:
    llm = LocalLLMClient()
    response = empty_response()
    retries = 0

    while retries <= MAX_RETRIES:
        plan = plan_question(question, llm)
        execution = execute_plan(question, plan, llm)
        verification = verify_solution(question, execution, llm)

        response["metadata"]["plan"] = plan
        response["metadata"]["checks"].append({
            "check_name": "verification",
            "passed": verification["passed"],
            "details": verification["issues"]
        })

        if verification["passed"]:
            response["answer"] = execution["final_answer"]
            response["status"] = "success"
            response["reasoning_visible_to_user"] = (
                "Solved the problem step by step and verified correctness."
            )
            response["metadata"]["retries"] = retries
            return response

        retries += 1

    response["metadata"]["retries"] = retries
    response["reasoning_visible_to_user"] = (
        "Unable to verify a correct solution after multiple attempts."
    )
    return response
if __name__ == "__main__":
    q = input("Enter question: ")
    result = solve(q)
    print(result)
