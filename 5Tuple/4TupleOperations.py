myTuple = (1,2,3,4,5,6,2,1,2)

myTuple1 = (1,2,6,9,8,7)

# 1. concatenation
print('********** concatenation *********')
print(myTuple + myTuple1)
# (1, 2, 3, 4, 5, 6, 1, 2, 6, 9, 8, 7)

# 2. repetition
print('********** repetition *********')
print(myTuple * 4)
# (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

# 3. 'in' operator
print('********** in *********')
print( 4 in myTuple1)

# 4. count()
print('********** count *********')
print( myTuple.count(2))

# 5. index()
print('********** index *********')
print(myTuple.index(3))

# 6. index()
print('********** index *********')
print(myTuple.index(3))


# Built-in functions for tuple
# 7. len()
print('********** len *********')
print(len(myTuple))

# 8. max()
print('********** max() min() *********')
print(max(myTuple))
print(min(myTuple))

# 9. tuple # tuple method can be used to convert a list into a tuple
print('********** tuple() *********')
print(tuple([1,2,3,4,5]))

