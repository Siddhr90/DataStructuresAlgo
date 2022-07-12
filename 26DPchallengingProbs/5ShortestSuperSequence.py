def formString(str1, str2, index1, index2, dp):
    print(index1,index2)
    if index1 == 0 or index2 == 0:
        return ''

    if str1[index1 - 1] == str2[index2 - 1]:
        lcs = formString(str1, str2,index1-1, index2-1, dp)
        lcs = lcs + str1[index1-1]

        return lcs
    if dp[index1-1][index2] >= dp[index1][index2-1]:              # if you forget equal to the solution will exit!
        return formString(str1,str2, index1-1, index2, dp)
    if dp[index1][index2-1] > dp[index1-1][index2]:
        return formString(str1, str2, index1, index2-1, dp)



def minSuperSeq(str1, str2):
    m = len(str1)
    n = len(str2)

    # fill dp table
    dp = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            elif dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

    # 2. get the string

    lcs = formString(str1, str2, len(str1), len(str2), dp)


    # 3. use three pointers to find the shortest superstring
    print(lcs)
    index1, index2, index3 = 0,0,0
    print(index3)
    result = ''

    while index1 < len(str1) and index2 < len(str2) and index3 < len(lcs):      # remember this is 'and' not 'or'
        print(result, index1, index2, index3)
        if str1[index1] != lcs[index3]:
            result += str1[index1]
            index1 += 1
        elif str1[index1] == lcs[index3]:
            if str2[index2] != lcs[index3]:
                result += str2[index2]
                index2 += 1
            else:
                result += str2[index2]
                index1 += 1
                index2 += 1
                index3 += 1

    result += str1[index1:]
    result += str2[index2:]

    return result



X = "ABCBDAB"
Y = "BDCABA"
# BCBA

print(minSuperSeq(X,Y))

