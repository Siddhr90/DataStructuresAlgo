myDict = {'name':'Sid', 'age':20, 'address':'London'}
# linear search
# check if each element is the value you are looking for
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'

print(searchDict(myDict,20))
print(searchDict(myDict,'America'))

# time Comlx : o(n)
# space Complx : O(1)