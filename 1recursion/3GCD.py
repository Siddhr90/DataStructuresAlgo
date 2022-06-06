# find GCD of two numbers using 1recursion

def GCD(n1,n2):
    assert int(n1)==n1 and int(n2)==n2, 'n1 and n2 must be integers'
    if n1<0:
        n1 = -1 * n1
    if n2<0:
        n2 = -1*n2

    if n2 == 0:
        return n1

    else:
        return GCD(n2,n1%n2)


print(GCD(18,48))
