# how to create a tuple

newTuple = ('a', 'b', 'c', 'd', 'e') # paranthesis to identify easily in code

print(newTuple)

newTuple1 = ('a', )
print(newTuple1)

notTuple2 = ('a') # without the comma, python will treat this as a string
print(notTuple2) # not a tuple, just a string

newTuple2 = tuple('abcde') # therefore avoid using tuple as a variable name
print(newTuple2) # ('a', 'b', 'c', 'd', 'e')

# time complexity O(n)
# space complexity O(1)




