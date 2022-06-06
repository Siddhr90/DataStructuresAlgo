# Built in func and operators

# 1. in operator, wherther a key exists or not

myDict ={'one':'uno', 'two':'dos', 'three':'trses', 'four':'cuarto'}
print(myDict)

print('one' in myDict) # True
print('uno' in myDict) # False
print('uno' in myDict.values()) # True
# NOTE: in operator uses linear search traversal algorithm for Lists and
# Hash-table for Dictionaries therefor3e O(1) time complexity

# 2. for
for key in myDict:
    print(key)
for key in myDict:
    print(key,myDict[key])
# O(N) time complxity

# 3. all() # based on the condition if all KEYS are true
print('**** all() ****')
myDict ={1: 'True', 2: 'True'}
print(all(myDict)) # True

myDict1 ={0: False, 2:False}
print(all(myDict1)) # False

# Some elements of dictionary are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d))

# Empty dictionary
d = {}
print(all(d))

# 4. any(), returns true if atleast one of the keys is true
print('**** any() ****')
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(any(d))
d = {}
print(any(d)) # false
d = {0: True, False:0}
print(any(d)) #False

# 5. len()
d = {0: "Salut", 1: "Hello", 2: "Hi"} # returns no of pairs
print(len(d)) #3

# 6. sorted(), sorted(iterable, reverse, key)
print('**** sorted() ****')
myDict = {'e':1, 'a': 2, 'u':3, 'o':4, 'i':5}
print(sorted(myDict)) # ['a', 'e', 'i', 'o', 'u']
print(sorted(myDict, reverse=True)) # ['u', 'o', 'i', 'e', 'a']

myDict = {'aee':1, 'ba': 2, 'xyqu':3, 'mo':4, 'aiaaaa':5,  'ba': 6}
print(sorted(myDict, key = len)) # ['ba', 'mo', 'aee', 'xyqu', 'aiaaaa']

myDict = {'aee':1, 'ba': 2, 'xyqu':3, 'mo':4, 'aiaaaa':5,  'ba': 6}
# if you use the same key again it will rewqrite with the latest value
print(myDict)




