# list is mutable, tuple is immutable

list1 = [0,1,2,3,4,5,6,7]

# change a value
list1[1] = 3
print(list1)

# reassign entire list
list1 = [4,5,6,9,8,7,1,2,3]
print(list1)

# delete an element
del list1[0]
print(list1)

# now trying these operations on tuples

tuple1 = (1,2,3,4,5,6,7)

# tuple1[1] = 0
# TypeError: 'tuple' object does not support item assignment

# but we can reassign entire tuple
tuple1 = (1,2,3,4)
print(tuple1)

# del wont work
#del tuple[1]
# TypeError: 'type' object does not support item deletion

# Built-in functions that can be used both for lists are tuples:
# len(), max(), min(), sum(), all(), any(), sorted()

# Methods that can be used both with tuples and lists:
# - count()
# - index()

# Methods that cannot be used for tuples:
#  append(), insert(), remove(), pop(), clear(), sort(), reverse()

# Tuples can be stored in lists
list1 = [(1,2), (3,4)]
print(list1)

# similarly lists can be stored in tuples
tuple3 = ([1,2],[3,4],[5,6])
print(tuple3)
# both tuples and lists can be nested

# advantages of usding tuples over Lists
# we generally use tuples for different data types and Lists for similar data types
# iterating through tuple is faster than list ( since tuples are immutable)
# Tuples that contain immutable elements can be used as a key for a dictionary
# if you have data that doesnt change tuples will guarantee that the it remains write protected
