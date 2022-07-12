
def LCSLength(S1, S2, m, n, lookup):
    for i in range(m + 1):
        lookup[i][0] = 0
    for j in range(n + 1):
        lookup[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])


# Function to display the differences between two Strings
def diff(S1, S2, m, n, dp):
    # TODO
    print('(m,n):(', m,n,')')
    # if m == 0 or n==0:                    # this was to print the longest sub sequence. here we check that m and n are
        #return ['']
    if m > 0 and n > 0 and S1[m-1] == S2[n-1]:
        diff(S1, S2, m-1, n-1, dp)                          # Note: order of the print and diff call makes a difference!
        print('', S1[m - 1], end=" ")

    elif m > 0 and (n == 0 or dp[m-1][n] > dp[m][n-1]):
        diff(S1, S2, m-1, n, dp)
        print(' -' + S1[m - 1], end=" ")

    elif n > 0 and (m == 0 or dp[m][n-1] >= dp[m-1][n]):
        diff(S1, S2, m, n-1, dp)
        print(' +' + S2[n - 1], end=" ")


S1 = "ABCDFGHJQZ"
S2 = "ABCDEFGIJKRXYZ"
lookup = [[0 for x in range(len(S2) + 1)] for y in range(len(S1) + 1)]

# fill lookup table
LCSLength(S1, S2, len(S1), len(S2), lookup)

# find difference

diff(S1, S2, len(S1), len(S2), lookup)