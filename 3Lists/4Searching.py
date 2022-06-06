
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
# using 'in' operator
if 20 in myList:
    print(myList.index(20))
else:
    print('value doesnt exist')

'''

#LinearSearch
def searchL(myList , element ):
    for i in myList:
        if i == element:
            return myList.index(i)
    return 'the value is not in the list'

print(searchL(myList, 120))