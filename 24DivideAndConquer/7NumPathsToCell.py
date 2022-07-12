def numOfPaths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numOfPaths(twoDArray, 0, col-1, cost - twoDArray[row][col])
    elif col == 0:
        return numOfPaths(twoDArray, row-1, 0, cost - twoDArray[row][col])
    else:
        option1 = numOfPaths(twoDArray, row-1, col, cost - twoDArray[row][col])
        option2 = numOfPaths(twoDArray, row, col-1, cost - twoDArray[row][col])
        return option2+option1

twoDList = [[4,7,1,6],
            [5,7,3,9],
            [3,2,1,2],
            [7,1,6,3]]

print(numOfPaths(twoDList,3,3,25))