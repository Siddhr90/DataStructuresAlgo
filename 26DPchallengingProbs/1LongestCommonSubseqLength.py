# length of longest common subsequence among two strings

def LCSLength(S1, S2, lenS1, lenS2):
    dp = [[0 for i in range(lenS2+1)] for j in range(lenS1+1)]

    for i in range(1,lenS1+1):
        for j in range(1,lenS2+1):

            if S1[i-1] == S2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[lenS1][lenS2]

S1 = 'ABCBDAB'
S2 = "BDCABA"

print(LCSLength(S1, S2, len(S1), len(S2)))
