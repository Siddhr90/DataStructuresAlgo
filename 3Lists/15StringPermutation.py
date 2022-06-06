# given two strings, write a method to find if one is permutation of another
# here we check if two lists are permutation of the other

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort() # changes elements of the list1 in the sorted order
    list2.sort()

    if list1 == list2:
        return True

    else:
        return False


list1 = ['c','b','a']
list2 = ['a','b','c']

print(permutation(list1,list2))


