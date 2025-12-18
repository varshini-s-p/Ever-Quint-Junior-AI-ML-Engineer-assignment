from agent import solve

TEST_QUESTIONS = [
    "If a train leaves at 14:30 and arrives at 18:05, how long is the journey?",
    "Alice has 3 red apples and twice as many green apples. How many apples total?",
    "A meeting needs 60 minutes. Slots: 09:00–09:30, 09:45–10:30, 11:00–12:00.",
    "If a train leaves at 23:50 and arrives at 01:20, how long is the journey?",
    "A meeting needs 45 minutes. Slots: 09:00–09:45, 10:00–10:30, 11:00–11:45. Which slots can fit the meeting?",
    "Bob has 5 blue balls. He has 3 more red balls than blue balls, and twice as many green balls as red balls. How many balls does he have in total?"
]

for q in TEST_QUESTIONS:
    result = solve(q)
    print("Q:", q)
    print("Result:", result)
    print("-" * 40)
