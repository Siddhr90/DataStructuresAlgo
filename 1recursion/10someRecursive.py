#write a recursive function which accepts an array and a callback. The function returns true is one of the array members is true
def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]) == True:
        return True
    else:
        return someRecursive(arr[1:], cb)

print(someRecursive([2,6,4],isOdd))