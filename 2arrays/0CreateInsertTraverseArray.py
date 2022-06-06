from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.4,1.5,1.9])

#array creation is a constant time operation

print(arr1)
print(arr2)

arr1.insert(6,7)
print(arr1)
arr1.insert(2,9) # at position 2, insert 9 #shifts all elements by one position to next cell o(n) operation

print(arr1)

def traversal(array):
    for i in array:
        print(i)

traversal(arr1)

