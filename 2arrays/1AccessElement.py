from array import *

arr1 = array('i',[1,2,3,4,5,6])

def accessEle(array,index):
    if index >= len(array):
        print('there is no element at this index')

    else:
        print(array[index])   #constant time operation O(1), we are not iterating, we are directly returning the value

accessEle(arr1,5)