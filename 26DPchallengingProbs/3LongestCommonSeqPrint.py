def LCS(S1, S2, m, n, dp):
    if m == 0 or n == 0:
        return ['']

    #print('(m,n)',m,n)

    if S1[m-1] == S2[n-1]:
        lcs = LCS(S1, S2, m-1, n-1, dp)
        for i in range(len(lcs)):
            lcs[i] = lcs[i] + (S1[m-1])
        return lcs
    if dp[m-1][n] > dp[m][n-1]:
        return LCS(S1, S2, m-1, n, dp)
    if dp[m][n-1] > dp[m-1][n]:
        return LCS(S1, S2, m, n-1, dp)

    # in case both are equal
    top = LCS(S1, S2, m-1, n, dp)
    left = LCS(S1, S2, m, n-1, dp)

    return top + left

def formDPtable(S1,S2):
    dp = [[0 for j in range(len(S2) + 1)] for i in range(len(S1) + 1)]

    for i in range(1, len(S1) + 1):
        for j in range(1, len(S2) + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp



def PrintAllLCS(S1, S2):
    # 1. form DP table for LCS
    dp = formDPtable(S1, S2)

    # 2. Collect all LCS sequences
    lcsSeq = LCS(S1, S2, len(S1), len(S2), dp)

    return lcsSeq


X = 'ABCBDAB'
Y = 'BDCABA'

print(PrintAllLCS(X,Y))









