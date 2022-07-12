
def zeroKnapsackBU(profits, weights, capacity):
    if capacity <= 0 or len(weights) != len(profits):
        return 0
    numberOfRows = len(profits) + 1
    dp = [[0 for i in range(capacity+1)] for j in range(numberOfRows)]

    for i in range(numberOfRows):
        for c in range(capacity+1):
            if i==0 or c==0:
                dp[i][c] = 0
            elif weights[i-1] <= c:
                dp[i][c] = max(profits[i-1] + dp[i-1][c-weights[i-1]], dp[i-1][c])
            else:
                dp[i][c] = dp[i-1][c]

    return dp[numberOfRows-1][capacity]


profits = [60, 100, 120]
weights = [10, 20, 30]
Capacity = 50
#)
print(zeroKnapsackBU(profits, weights, Capacity))
