#write a recursive function which accepts an array of 2arrays and returns a new array with all vales flattened
# flatten([1,2,3,[4,5]]) = [1,2,3,4,5]

def flatten(arr):
    if len(arr)==0:
        return arr
    if type(arr[0]) == list:
        return flatten(arr[0]) + flatten(arr[1:])
    else:
        return [arr[0]] + flatten(arr[1:])


#nestedList = [[['A', 'B', 'C']], ['D', 'E', 'F'],[[['G']]]]


print(flatten(nestedList))







#understanding extend and append
'''

>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]

arr1 = [1,2,3,4]
arr2 = [4,5,6,7]

arr1.extend(arr2)
print(arr1)
#[1, 2, 3, 3, 4, 5]

arr1.append(arr2)
print(arr1)
#[1, 2, 3, 3, 4, 5, [3, 4, 5]]
'''