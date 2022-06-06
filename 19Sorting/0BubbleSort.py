import numpy as np
import math

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    return customList

def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1,len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i],customList[min_index] = customList[min_index], customList[i]
    return customList

def insertionSort(customList):
    for i in range(1,len(customList)):                     # O(n) time C
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:                # O(n) time C
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

def bucketSort(customList):
    numBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numBuckets):
        arr.append([])

    for j in customList:
        index_b = math.ceil(j*numBuckets/maxValue)
        arr[index_b-1].append(j)

    for i in range(numBuckets):
        arr[i] = insertionSort(arr[i])                      # if we use quicksort here we get NlogN time complexity

    k = 0
    for i in range(numBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1

    return customList

# helper function merge
def merge(customList, l, m, r):
    n1 = m - l + 1                          # l,m r are indices   left, middle, right
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = customList[l+i]

    for j in range(0, n2):
        R[j] = customList[m+1+j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2                                # O(1)
        mergeSort(customList, l, m)                     # T(n/2)
        mergeSort(customList, m+1, r)                   # T(n/2)        combined logN
        merge(customList,l,m,r)                         # O(n)
    return customList                                                   # combined O(NlogN) time and O(N) space



cList = [2,1,9,8,7,6,5,4]
#bubbleSort(cList)                   # O(n^2) time C and O(1) space C
#selectionSort(cList)                 # O(n^2) time C and O(1) space C
#insertionSort(cList)
#print(bucketSort(cList))
print(mergeSort(cList,0,7))             # combined O(NlogN) time and O(N) space
