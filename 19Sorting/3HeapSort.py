# helper
def heapify(customList, n, i):
    smallest = i
    l = 2*i + 1                 # since index starts from 0 in this case
    r = 2*1 + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r

    if smallest != i :
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList,n,smallest)

def heapSort(customList):
    n = len(customList)
    # building heap tree
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
    print(customList)

    # extracting each element at ith index
    for i in range(n-1, 0, -1):
        print(i)
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
        print(customList)
    customList.reverse()


cList = [2,1,9,8,7,6,5,4]
heapSort(cList)
#print(cList)

