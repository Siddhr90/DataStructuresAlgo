# Sim between arrays and Lists:
# - Both are mutable
# - Both can be indexed and iterated through
# - Both can be sliced

# Diff:
# - Arrays are optimized for arithmetic operations. So if you are using arithmetic, use arrays


import numpy as np

myArray = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5,6]

print(myArray/2) # arrays are optimized for these
# print(myList/2) # not supported error

myArray = np.array([1,2,3,4,5,6,'a']) # all elements get converted to string
myList = [1,2,3,4,5,6,'a'] # elements can have different data types

print(myArray)
print(myList)
