from agent import solve

class LangChainReasoningAgent:
    """
    LangChain-style wrapper around the core reasoning agent.
    """
    def run(self, question: str) -> dict:
        return solve(question)
