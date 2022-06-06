# how to find sum of digits of a positive integer using 1recursion?

def findsum(n):
    #print(n)
    assert n>=0 and int(n)==n, 'n must be a positive integer'
    #base
    if n == 0:
        return 0
    #recursive
    else:
        return int(n%10) + findsum(int(n/10))

print(findsum(1002355))
