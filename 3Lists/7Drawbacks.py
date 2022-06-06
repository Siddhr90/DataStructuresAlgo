# pitfalls and how to avoid them

myList = [2,4,3,1,5,6]

myList = myList.sort()
print(myList)
# Output: None
# Correct method is:
myList = [2,4,3,1,5,6]
orig = myList[:] # if you just put orig=myList , then orig is also going to change with the changes made to myList

myList.sort()
print(orig)
print(myList)

# In the case of sorting there is another function
sorted(orig)
print(myList)

# docs.python.org

myList.append(10)

print(myList)

myList = myList + [10]
print(myList)

myList.append([10]) #adds nested list
print(myList)