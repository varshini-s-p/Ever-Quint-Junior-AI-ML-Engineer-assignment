"""
Algorithm: Max Profit Problem
As per EverQuint assignment

Problem Summary:
- Only one property can be built at a time.
- Each property takes fixed build time.
- After completion, it earns money for remaining time.
- Goal: maximize total earnings within n time units.

Properties:
T (Theatre): 5 units time, $1500 per unit time
P (Pub): 4 units time, $1000 per unit time
C (Commercial Park): 10 units time, $2000 per unit time
"""

def max_profit(n):
    # Property definitions
    buildings = {
        "T": {"time": 5, "earn": 1500},
        "P": {"time": 4, "earn": 1000},
        "C": {"time": 10, "earn": 2000}
    }

    # dp[t] = maximum earnings achievable using t units of time
    dp = [0] * (n + 1)

    # choice[t] = which building was completed at time t
    choice = [None] * (n + 1)

    # Build DP table
    for t in range(1, n + 1):
        for b in buildings:
            build_time = buildings[b]["time"]
            earn = buildings[b]["earn"]

            if t >= build_time:
                profit = dp[t - build_time] + (n - t) * earn
                if profit > dp[t]:
                    dp[t] = profit
                    choice[t] = b

    # Find time t with maximum profit
    max_time = max(range(n + 1), key=lambda x: dp[x])

    # Backtrack to count buildings
    count = {"T": 0, "P": 0, "C": 0}
    t = max_time

    while t > 0 and choice[t] is not None:
        b = choice[t]
        count[b] += 1
        t -= buildings[b]["time"]

    return count, dp[max_time]


# ---------------------- MAIN EXECUTION ----------------------
if __name__ == "__main__":
    # Input (change this value to test)
    n = int(input("Enter time units: "))

    result, earnings = max_profit(n)

    print("\nOptimal Property Mix:")
    print(f"T:{result['T']} P:{result['P']} C:{result['C']}")
    print(f"Total Earnings: ${earnings}")
