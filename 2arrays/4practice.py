from array import *

# 1. create an array and traverse
my_array = array('i', [1,2,3,4,5])

for i in my_array:
    print(i)

# 2. access individual elements via indices
print('step2')
print(my_array[3])

# 3. append new value to end of array
print('step3')
my_array.append(6)
print(my_array)

# 4. insert new value to array at given position
print('step4')
my_array.insert(4,9)
print(my_array)

# 5. extend array using extend method
print('step5')
my_array1 = array('i',[1,2,3,4])
my_array.extend(my_array1)
print(my_array)

# 6. add items from list to array using fromlist() method
print('step6')
tempList = [1,2,3,4,5]
my_array.fromlist(tempList)
print(my_array)

# 7. remove an element
my_array.remove(3) #removes the first value that it sees (here the first 3)
print(my_array)

# 8. remove last element using pop()
my_array.pop()
print(my_array)

# 9. Fetch the element from the given index
print(my_array.index(4)) # prints index of the first value(here 4) that it sees.

# 10. Reverse an array
my_array.reverse()
#print(my_array.reverse()) #does not print anything but reverses array
print(my_array)

# 11. buffer_info()
print(my_array.buffer_info()) #gives the start point in memory and number of elements after it

# 12. check number of instances using count()
print(my_array.count(4))

# 13. convert array to string using tostring() method
strng = my_array.tostring()
print(strng)

#14. fromstring()
ints = array('i')
ints.fromstring(strng)
print(ints)

#15 convert to list

print(my_array.tolist())

#16 slice elements from an array
print(my_array[2:4])
