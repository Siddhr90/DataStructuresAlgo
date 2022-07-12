def numFactorTopDown(n, tempDict):
    if n in (0,1,2):
        return 1
    elif n == 3:                        # {3} and {1,1,1}
        return 2
    else:
        if n not in tempDict:
            subP1 = numFactorTopDown(n-1, tempDict)
            subP2 = numFactorTopDown(n-3, tempDict)
            subP3 = numFactorTopDown(n-4, tempDict)
            tempDict[n] = subP1 + subP3 + subP3
        return tempDict[n]

# Bottom Up

def numberFactorBU(n):
    tempArr = [1,1,1,2]
    for i in range(4,n+1):
        tempArr.append(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
    return tempArr[n]

print(numFactorTopDown(5,{}))
print(numberFactorBU(5))