# implement an alg to determine if a list has all unique characters using python list
# in strings or in arrays,
# imp q


myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16]

# my approach
def isUnique(List):
    for i in range(len(List)):
        for j in range(i+1, len(List)):
            if List[i] == List[j]:
                return False
    return True


print(isUnique(myList))

# another approach
def isUnique2(list):
    a = []
    for i in list:
        if i in a:
            return False
        else:
            a.append(i)
    return True

print(isUnique2(myList))