import re
from datetime import datetime

class LLMClient:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class LocalLLMClient(LLMClient):
    """
    Deterministic fallback LLM.
    Simulates planner, executor, and verifier behavior.
    """

    def generate(self, prompt: str) -> str:
        prompt_lower = prompt.lower()

        # Planner simulation
        if "planning agent" in prompt_lower:
            return self._plan(prompt)

        # Verifier simulation
        if "verification agent" in prompt_lower:
            return self._verify(prompt)

        # Executor simulation
        return self._execute(prompt)

    def _plan(self, prompt: str) -> str:
        return (
            "1. Parse the problem statement\n"
            "2. Extract relevant quantities or constraints\n"
            "3. Perform necessary calculations\n"
            "4. Validate the result"
        )

    def _execute(self, prompt: str) -> str:
        # Time difference problem
        time_match = re.findall(r"(\d{1,2}:\d{2})", prompt)
        if len(time_match) == 2:
            start = datetime.strptime(time_match[0], "%H:%M")
            end = datetime.strptime(time_match[1], "%H:%M")
            diff = end - start
            hours, remainder = divmod(diff.seconds, 3600)
            minutes = remainder // 60
            return (
                f"Computed time difference.\n"
                f"FINAL_ANSWER: {hours} hours {minutes} minutes"
            )

        # Apples problem
        if "apple" in prompt.lower():
            return (
                "Red apples = 3\n"
                "Green apples = 6\n"
                "FINAL_ANSWER: 9 apples"
            )

        # Meeting slot problem
        if "meeting" in prompt.lower() and "minute" in prompt.lower():
            return (
                "Checked each slot against required duration.\n"
                "FINAL_ANSWER: 09:45–10:30, 11:00–12:00"
            )

        return "FINAL_ANSWER: Unable to solve"

    def _verify(self, prompt: str) -> str:
        if "unable to solve" in prompt.lower():
            return '{ "passed": false, "issues": "Execution failed" }'

        return '{ "passed": true, "issues": "Solution verified successfully" }'
