# prereq Longest common subsequence

def LRSLength(X, m, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == X[j-1] and i != j :
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


print(LRSLength('ATAKTKGGA', 9, 9))
