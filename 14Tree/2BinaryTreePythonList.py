class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return 'Success'
        return 'Not Found'

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:                  # timeComplexity O(1)
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)                 # timeComplexity O(n/2)
        self.preOrderTraversal(index*2+1)               # timeComplexity O(n/2)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:                  # timeComplexity O(1)
            return
        self.inOrderTraversal(index*2)                 # timeComplexity O(n/2)
        print(self.customList[index])
        self.preOrderTraversal(index*2+1)               # timeComplexity O(n/2)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:                  # timeComplexity O(1)
            return
        self.postOrderTraversal(index*2)                 # timeComplexity O(n/2)
        self.postOrderTraversal(index*2+1)               # timeComplexity O(n/2)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):

        if self.lastUsedIndex == 0:
            return 'There are no elements in the Tree'
        for i in range(1, self.lastUsedIndex+1):                                # O(n) time C
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return 'Node has been successfully'

    def deleteBT(self):
        self.customList = None
        return 'the binary tree has been successfully deleted'


# ***************************************

newBT = BinaryTree(8)                   # timeComplexity O(1) and Space C O(n)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))         # O(1) Time and Space C(since we are only adding to existing list
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
print(newBT.insertNode("Cola"))
print(newBT.searchNode("Pepsi"))          # O(1) Time and O(n) Space C
print(newBT.searchNode("Cold"))
print("********pre*********")
newBT.preOrderTraversal(1)                # Space C O(n) since recursive calls will use stack memory
print("********in*********")
newBT.inOrderTraversal(1)                 # C Same as preOrder
print("********post*********")
newBT.postOrderTraversal(1)               # C Same as preOrder
print("********level*********")
newBT.levelOrderTraversal(1)              # O(n) time C and O(1) space C

print("********deleteValue*********")
newBT.deleteNode('Tea')
newBT.levelOrderTraversal(1)

print("********deleteBT*********")
newBT.deleteBT()                          # O(1) time C and space C
print(newBT.levelOrderTraversal(1))

