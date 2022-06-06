# find max product of two integers where all numbers are positive

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def maxProduct(array):
    maxP = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if (array[i] * array[j]) > maxP:
                maxP = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])

    print(pairs)
    print(maxP)

maxProduct(myArray)


