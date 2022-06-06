import sys
sys.setrecursionlimit(10000)

def factorial(n):
    #3. unintentional case
    assert n>=0 and int(n)==n, 'The number n must be a positive integer'

    #2. base case:
    if n in [0,1]:
        return 1
    #1. recursive case:
    else:
        print(n)
        return n * factorial(n-1)

print(factorial(1.5))

