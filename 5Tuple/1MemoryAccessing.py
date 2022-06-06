newTuple = ('a', 'b', 'c', 'd', 'e')

print(newTuple[2])
print(newTuple[-1])

print(newTuple[-2])


# slice opeartor
# make NOTE that the last index is not printed while using slice operator

print(newTuple[1:3]) # ('b', 'c')   #  prints indixes 1 and 2, no 3

print(newTuple[1:]) # prints till the end

# slicing is same as lists but we cannot modify the elements of the tuple!

newTuple[0] = 'm'
# TypeError: 'tuple' object does not support item assignment



