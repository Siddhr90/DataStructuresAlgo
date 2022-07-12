# palindromic subsequence

def lps(parameter):
    rev = parameter[::-1]
    m = len(parameter)
    print(rev)

    dp = [[0 for i in range(m+1)] for j in range(m+1)]

    for i in range(1,m+1):
        for j in range(1, m+1):
            print(parameter[i-1], rev[j-1])
            if parameter[i-1] == rev[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)

    return dp[m][m]

string1 = "malayalam"
print(lps(string1))