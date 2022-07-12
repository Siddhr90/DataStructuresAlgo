# top
# we are avoiding the calling of subproblems repeatedly

def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            firstHouse = houses[currentIndex] + houseRobberTD(houses, currentIndex+2, tempDict)
            secondHouse = houseRobberTD(houses, currentIndex+1,tempDict)
            tempDict[currentIndex] = max(firstHouse, secondHouse)

        # if it is in temp dict, we have already calculated the value once, just return the value in that case
        return tempDict[currentIndex]

houses = [6,7,1,30,8,2,4]
print(houseRobberTD(houses,0, {}))

# Bottom Up approach

def houseRobberBU(houses, currentIndex):
    tempArr = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):                  # (-1) so that it includes 0 index also
        tempArr[i] = max(houses[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]

print(houseRobberBU(houses, 0))







