# House Robber problem

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):                                                     # recursion runs till one less than len
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)            # first option we include first house and jump to 3rd house
        skipFirstHouse = houseRobber(houses, currentIndex+1)                                    # skip first house and take 2nd house
        return max(stealFirstHouse, skipFirstHouse)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses,0))                # answer same as lecture