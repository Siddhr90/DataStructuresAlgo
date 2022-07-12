# zero Knapsack problem, cans take partial weights

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zOKnapsack(items, capacity, currentIndex) :
    if capacity<=0 or currentIndex<0 or currentIndex>=len(items):                              # Current index cannot be less than zero coz it its -ve it will cycle
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zOKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zOKnapsack(items, capacity, currentIndex+1)           # we dont include item and capacity doesn't change
        return max(profit1, profit2)
    else:                                                               # when weight is greater than capacity
        print(items[0].weight,items[1].weight,items[2].weight,items[3].weight,capacity,currentIndex)
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zOKnapsack(items, 7, 0))