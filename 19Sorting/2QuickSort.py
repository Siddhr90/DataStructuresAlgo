# helper function
# puts all lesser elements to left of pivot and greater elemets to the right of pivot
def partition( customList, low, high):
    i = low-1
    pivot = customList[high]
    for j in range(low,high):                               # O(n) time C
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)                # returns partition index

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)           # O(n) timeC
        quickSort(customList, low, pi -1)               # T(n/2)
        quickSort(customList, pi+1, high)               # T(n/2)
    return customList                                                        # combined N(logN) time C and O(n) space C


cList = [2,1,9,8,7,6,5,4]
print(quickSort(cList, 0, 7))                      # avoid when you want a stable sort
#print(cList)