# logic is same as that of array

shoppingList = ['milk', 'Cheese', 'Butter']
print(shoppingList[1])
# we can think of list as a mapping relationship between indices and elements.
# This relationship is called mapping

# print(shoppingList[3]) #out of range

# using 'in' operator we can check if an element exists in a list or not
print('milk' in shoppingList)
print('bread' in shoppingList)

# What if we give a negative value as index
print(shoppingList[-1])
print(shoppingList[-2])
# print(shoppingList[-4]) #out of range

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

empty = []
for i in empty:
    print("i am empty") # nothing happens