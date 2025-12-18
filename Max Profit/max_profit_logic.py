def max_profit(n):
    buildings = {
        "T": {"time": 5, "earn": 1500},
        "P": {"time": 4, "earn": 1000},
        "C": {"time": 10, "earn": 2000}
    }

    dp = [0] * (n + 1)
    choice = [None] * (n + 1)

    for t in range(1, n + 1):
        for b in buildings:
            bt = buildings[b]["time"]
            earn = buildings[b]["earn"]

            if t >= bt:
                profit = dp[t - bt] + (n - t) * earn
                if profit > dp[t]:
                    dp[t] = profit
                    choice[t] = b

    max_time = max(range(n + 1), key=lambda x: dp[x])

    count = {"T": 0, "P": 0, "C": 0}
    t = max_time
    while t > 0 and choice[t]:
        b = choice[t]
        count[b] += 1
        t -= buildings[b]["time"]

    return count, dp[max_time]
