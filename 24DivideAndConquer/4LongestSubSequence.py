# Longest Common Subsequence

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        # Option1 : check char that is not matching in first string and conntinue to next character in 2nd string
        option1 = findLCS(s1, s2, index1, index2+1)
        # option2 : check char that is nor matching from 2nd string and continue to next char in 1st string
        option2 = findLCS(s1, s2, index1+1, index2)
        return max(option1,option2)

print(findLCS("elephant","eretpat",0,0))