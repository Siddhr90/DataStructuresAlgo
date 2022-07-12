# bottom up

def fibonacciTab(n):
    tb = [0,1]                                      # tb - table for tabulation
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]                                  # because index starts from zero

print(fibonacciTab(6))                              # O(n) time and space C