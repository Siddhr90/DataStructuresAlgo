myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}

# 1. pop()
print(myDict.pop('address1'))
print(myDict) # returns only value
myDict['address1'] = 'America'

# 2. popitem() # pops a random key value pair
print(myDict.popitem()) # returns key kalue

# print(myDict.pop()) # Error needs atleast one argument

# 3. clear() we can delete all pairs from a dict
myDict.clear()
print(myDict)

myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}
# 4. del
del myDict['name']
print(myDict)

del myDict
print(myDict) # NameError: name 'myDict' is not defined


# time Comlx : o(1) in average case and O(n) in amortized case
# space Complx : O(1)







