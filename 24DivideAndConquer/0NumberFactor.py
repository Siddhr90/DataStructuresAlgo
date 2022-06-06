# Number of ways to express n as a sum of 1, 3, and 4

def numberFactor(n):
    if n in (1,2,0):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1 + subP2 + subP3

print(numberFactor(5))