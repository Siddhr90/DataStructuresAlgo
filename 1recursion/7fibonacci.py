#write a recursive function called fib which accepts a number and returns the nth number in the fibonacci sequence

def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)