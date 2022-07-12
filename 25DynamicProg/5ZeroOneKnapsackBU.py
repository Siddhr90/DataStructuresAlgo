# topDown

class Item:
    def __init__(self, weight, profit):
        self.profit = profit
        self.weight = weight

def zOKnapsackTD(items, capacity, currentIndex, tempDict):
    dictKey = str(currentIndex) + str(capacity)
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[dictKey]
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zOKnapsackTD(items,capacity- items[currentIndex].weight,currentIndex+1,tempDict)
        profit2 = zOKnapsackTD(items,capacity,currentIndex+1,tempDict)
        tempDict[dictKey] = max(profit2,profit1)
        return tempDict[dictKey]
    else:
        return 0

item1 = Item(3,31)
item2 = Item(1,26)
item3 = Item(5,72)
item4 = Item(2,17)
items = [item1, item2, item3, item4]
capacity = 7

print(zOKnapsackTD(items, 7, 0, {}))