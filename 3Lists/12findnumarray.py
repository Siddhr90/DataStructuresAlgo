# find a number in a given list of arrays

# in python lists we have in operator to check if an element exists
# here we will use python arrays since interviewers might ask for array search algorithm

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# we will implement linear search here

def findNum(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i


print(findNum(myArray, 5))
