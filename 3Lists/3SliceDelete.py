myList = ['a', 'b', 'c', 'd', 'e', 'f']

# slice operator [:]
# to print first 2 elements
print(myList[0:2]) #lst index is not included
print(myList[1:])
print(myList[:])

myList[0:2] = ['x', 'y']
print(myList[:])

# deletion - pop() , delete() , remove()
'''
myList.pop(1) # removes the element at the given index, O(n) operation
print(myList)

myList.pop() # removes the last element if no index, O(1) operation
print(myList)

print(myList.pop(2)) # if you want to use the element that is popped
print(myList)

del myList[1]
print(myList)
'''

del myList[2:4]
print(myList)

myList.remove('e') # very useful when you want to remove the element itself
print(myList)


