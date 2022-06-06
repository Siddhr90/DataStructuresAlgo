newTuple = ('a','b','c','d','e')

print('b' in newTuple)
# True

# another method linear search

def searchTuple(givenTuple, target):
    for i in givenTuple:
        if i == target:
            return givenTuple.index(i)
    return 'The element does not exist in the tuple'

print(searchTuple(newTuple, 'a'))

print(searchTuple(newTuple, 'p'))

# linear search takes o(n) time complexity




