
myList = [1,2,3,4,5,6]
print(myList)
# lists are mutable
# are ordered - means order will remain the same till we change them

myList[2] = 33

print(myList)

# List Methods: insert, append, extend

myList.insert(3,9) # O(n) number of elements to shift
print(myList)

myList.append(55)
print(myList)

newList = [11,12,13,14]
myList.extend(newList) # O(n) number of elements added
print(myList)

