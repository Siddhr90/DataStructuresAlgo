# How to calculate power of number using 1recursion?

def powerof(n,p):
    assert int(p)==p and p>=0, 'p must be positive integer'
    #base:
    if  p==1:
        return n
    #recursive case:
    else:
        return n * powerof(n, p-1)


print(powerof(3.23,1.2))