# How to convert a number from decimal system to binary using 1recursion

def DtoB(n):
    assert int(n)==b, 'the parameter must be integer'
    if n==0:
        return 0
    else:
        return n%2 + 10 * DtoB(int(n/2))

print(DtoB(-13.5))