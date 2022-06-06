# convert one string to another using delete, insert or replace operations. Find the min Count of edit operations

def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):                   # means we have reached the end of s1 and need to delete rest of the chars from s2
        return len(s2)-index2
    if index2 == len(s2):                   # means we need to add characters from s2 to s1, add chars from s1 to s2
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1,s2, index1+1, index2+1)             # we continue to next position
    else:
        # divide into 3 subproblems
        deleteOp = 1 + findMinOperation(s1,s2, index1, index2+1)
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)

print(findMinOperation("table","tbrlestt", 0, 0))

