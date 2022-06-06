
# day1 - 11, 15, 10, 6
# day2 - 10, 14, 11, 5
# day3 - 12, 17, 12, 8
# day4 - 15, 18, 14, 9

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]) #O(1) operation
# if we were adding values one by one it would be O(n*n)
print(twoDArray)

newTwoArray = np.insert(twoDArray, 4, [[1,2,3,4]], axis=0)
print(twoDArray)

newTwoDarray = np.append(twoDArray, [[1,2,3,4]], axis=0) #axis=0 is row and axis=1 is column
print(newTwoDarray)

newTwoDarray = np.append(twoDArray, [[1],[2],[3],[4]], axis=1) #axis=0 is row and axis=1 is column
print(newTwoDarray)
