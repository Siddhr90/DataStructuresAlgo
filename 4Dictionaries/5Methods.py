# Dictionary Methods()

# 1. clear() , deletes all pairs
myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}
myDict.clear()
print(myDict)

# 2. copy() , returns a shallow copy of the dictionary, with copy of references from original dictionary,
# does not modify original one

myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}
newDict = myDict.copy()
print(myDict)
print(newDict)

# 3. fromkeys() , creates a new dictionary from the given sequence of keys
# dictionary.fromkeys(sequence[],value) , value is optional
newDict = {}.fromkeys([1,2,3],0)
print(newDict) # {1: 0, 2: 0, 3: 0}

newDict = {}.fromkeys([1,2,3])
print(newDict) # {1: None, 2: None, 3: None}

# 4. get() , returns value of specified key if the key is in the dict
# dict.get(key,value) # value is optional, this is the value to be returned if the key is not present
myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}
print(myDict.get('age', 27)) # 20
print(myDict.get('height', 180)) # 180
print(myDict.get('city')) # None

# 5. items() , returns a view object that displays a list of key-vvalue tuple pairs
# dict.items()
print(myDict.items())
# dict_items([('name', 'Sid'), ('age', 20), ('address1', 'London'), ('address2', 'India')])

# 6. keys()
print(myDict.keys())
# dict_keys(['name', 'age', 'address1', 'address2'])

# 7. popitem()
print(myDict.popitem()) # removes random key-value pair
# ('address2', 'India')

# 8. setdefault() , returns value of key if key is in the dictionary, else inserts key with a value to the dict
# dict.setdefault(key, default_value)
myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}
print(myDict.setdefault('name','Kid')) # Sid
print(myDict.setdefault('name1','Kid')) # Kid
print(myDict) # {'name': 'Sid', 'age': 20, 'address1': 'London', 'address2': 'India', 'name1': 'Kid'}

# 9. pop() , rewmoves and returns an element
# dict.pop(key,default_value)
print(myDict.pop('name1', 'apple'))
print(myDict)
print(myDict.pop('name2', 'apple'))

# 10. values() , returns a view object with all values, takes no arguments
print(myDict.values())
# dict_values(['Sid', 20, 'London', 'India'])

# 11. update(), updates the dictionary with the elements froms another dictionary or from an iterable
# of key value pairs or a tuple
# adds if the key is not in the dictionary or updates if the key is already in the dictionary
# dictionary.update(other_dictionary)

myDict = {'name':'Sid', 'age':20, 'address1':'London', 'address2':'India'}
newDict = {'class':'MS', 'area':'cs', 'branch': 'natSci'}

myDict.update(newDict)
print(myDict)
# {'name': 'Sid', 'age': 20, 'address1': 'London', 'address2': 'India', 'class': 'MS', 'area': 'cs', 'branch': 'natSci'}






