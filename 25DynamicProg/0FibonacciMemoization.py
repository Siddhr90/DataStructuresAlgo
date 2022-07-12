# fibonacci with memoization

def fibMemo(n, memo):                                   # we use a dictionary for memo          # top down
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

myDict = {}
print(fibMemo(6, myDict))

