class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1                         # we are taking size+1 because the zero index will not be used

def peekofHeap(rootNode):                               # O(1) time and space C
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):                               # returns size of filled elements
    if not rootNode:                                    # O(1) time and space C
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])

#helper to insert node
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)                      # O(logN)
    elif heapType == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)                      # O(logN) time and space C

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return " The binary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1                                                      # O(logN)
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return 'The value has been successfully inserted'

# helper to extract
def heapifyTreeExtract(rootNode, index, heapType):
    # we are comparing an index to it's children everytime, index is updated in every recurrence
    leftChildIndex = index*2
    rightChildIndex = index*2 + 1
    swapChild = 0

    # check if rootNode has children
    if rootNode.heapSize < leftChildIndex:
        return
    # if only one child, which is left child
    elif rootNode.heapSize == leftChildIndex:
        if heapType == 'Min':
            if rootNode.customList[index] > rootNode.customList[leftChildIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftChildIndex]
                rootNode.customList[leftChildIndex] = temp
            return

        if heapType == 'Max':
            if rootNode.customList[index] < rootNode.customList[leftChildIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftChildIndex]
                rootNode.customList[leftChildIndex] = temp
            return
    # both children exist
    else:
        if heapType == 'Min':
            if rootNode.customList[leftChildIndex] < rootNode.customList[rightChildIndex]:
                swapChild = leftChildIndex
            else:
                swapChild = rightChildIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftChildIndex]
                rootNode.customList[leftChildIndex] = temp
        else:
            if rootNode.customList[leftChildIndex] > rootNode.customList[rightChildIndex]:
                swapChild = leftChildIndex
            else:
                swapChild = rightChildIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftChildIndex]
                rootNode.customList[leftChildIndex] = temp
        # run it for the swap child
        heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)                       # O(logN) time and space
        return extractedNode

def deleteEntireBP(rootNode):
    rootNode.customList = None




# **********************
newBHeap = Heap(5)                             # time C = O(1) and space C O(N)

insertNode(newBHeap,4,'Max')
insertNode(newBHeap,5,'Max')
insertNode(newBHeap,2,'Max')
insertNode(newBHeap,1,'Max')
print(extractNode(newBHeap, "Max"))
print('*********')
levelOrderTraversal(newBHeap)
print('*********')
deleteEntireBP(newBHeap)
levelOrderTraversal(newBHeap)
