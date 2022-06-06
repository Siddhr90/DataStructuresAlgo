# Binary Search Tree
import HelperQueueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)                         # O(1) Time C
        else:
            insertNode(rootNode.leftChild, nodeValue)                       # O(n/2) Time C
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"                        # O(logN) time and space C

def preOrderTraversal(rootNode):                                                # O(n) time and space C
    if not rootNode:
        return 'The BST does not have any elements'
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def levelOrderTraversal(rootNode):                                          # O(n) since we are visiting all elements
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:                                # do not forget this if condition!
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):                        # O(logN) space(recursive stack for queue) and time C
    if rootNode.data == nodeValue:
        print('value exists')                               # do not return 'value exists' it will go to the previous
                                                            # recursive call and None will be returned to call in main (unless root node is the value)
    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftChild, nodeValue)
    else:
        searchNode(rootNode.rightChild, nodeValue)

# delete node helper to find successor
def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)                          # O(n/2)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)                        # O(n/2)
    else:                                               # here rootNode.value ==  nodeValue
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)                                # O(logN) time C since we are calling it for right subtree only
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)        # O(logN) timne C
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The node has been successfully deleted'

# **********************************************

newBST = BSTNode(None) # we can initialize as none and while inserting we can put a value here, O(1) time and space C
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))


print(newBST.data)
print(newBST.leftChild.data)
print(newBST.rightChild.data)

print("*******************pre*********************")
preOrderTraversal(newBST)

print("*******************in*********************")
inOrderTraversal(newBST)

print("*******************post*********************")
postOrderTraversal(newBST)

print("*******************level*********************")
levelOrderTraversal(newBST)

print("*******************Search*********************")
searchNode(newBST, 60)

print("*******************Delete*********************")
deleteNode(newBST, 100)                                 # O(logN) time and Space complexity
levelOrderTraversal(newBST)

print(deleteBST(newBST))
levelOrderTraversal(newBST)


