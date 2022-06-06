# Binary Tree implementation using LinkedList

import HelperQueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')              # Time and Space Complexity = O(1)
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode("tea")
coffee = TreeNode('coffee')
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = tea
leftChild.rightChild = coffee


def preOrderTraversal(rootNode):
    if not rootNode:                                #..............O(1) time c
        return
    print(rootNode.data)                            #..............O(1) time c
    preOrderTraversal(rootNode.leftChild)           #..............O(n/2) time c
    preOrderTraversal(rootNode.rightChild)          #..............O(n/2) time c

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)           #..............O(n/2) time c
    print(rootNode.data)                            #..............O(1) time c
    inOrderTraversal(rootNode.rightChild)           #..............O(n/2) time c

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# In case of level order traversal, we will use Queue based on linkedList
def levelOrderTraversal(rootNode):
    if not rootNode:                                            #..............O(1) time c
        return
    else:
        customQueue = queue.Queue()                             #..............O(1) time c
        customQueue.enqueue(rootNode)                           #..............O(1) time c
        while not(customQueue.isEmpty()):                       #..............O(n) time c
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):              #..............O(1) time c
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):             #..............O(1) time c
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 'The BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)                           #..............O(n) time C
        while not(customQueue.isEmpty()):                       # .............O(n) time C
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return 'Success, node exists'
            if root.value.leftChild is not None :
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None :
                customQueue.enqueue(root.value.rightChild)
        return 'Not found'

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is None:
                root.value.leftChild = newNode
                return 'node added'
            else:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is None:
                root.value.rightChild = newNode
                return 'node added'
            else:
                customQueue.enqueue(root.value.rightChild)

# This is a helper function to delete Node.
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode

# This is a helper function to delete Node.
def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value is deepestNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

            if root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, Node):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()                                                         #..............O(1) time c
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():                                                    #..............O(n) time c
            root = customQueue.dequeue()
            if root.value.data == Node:
                dNode = getDeepestNode(rootNode)                                            #..............O(n) time c
                root.value.data = dNode.data                                                #..............O(n) time c
                deleteDeepestNode(rootNode,dNode)
                return "The ndoe has been successfully deleted"

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)                                   #..............O(n) space c
        return 'failed to delete message'

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'The BT has been deleted'                                                         #..............O(1) time c


print('*****************')
preOrderTraversal(newBT)                                        #..............O(n) Space c
print('*****************')
inOrderTraversal(newBT)                                         #..............O(n) Space c (when we call a function recursively,
                                                                # we need to store the last value of recursion
print('*****************')                                                                                # in the stack)
postOrderTraversal(newBT)

print('*****************')
levelOrderTraversal(newBT)                                      #..............O(n) Space c (since we need to create queue which takes the elements)


print(searchBT(newBT,"tea"))

newNode = TreeNode("Cola")
print(insertNodeBT(newBT, newNode))                             # O(n) time and space C since its similar to level order traversal,
levelOrderTraversal(newBT)


# Checking working of helper functions to delete node
# ************************************
print("***************")
deepestNode = getDeepestNode(newBT)
print(deepestNode.data)

print("***************")
newNode= getDeepestNode(newBT)
deleteDeepestNode(newBT,newNode)
levelOrderTraversal(newBT)
# *************************************

deleteNodeBT(newBT, 'Hot')
levelOrderTraversal(newBT)

print("***************")
deleteBT(newBT)
levelOrderTraversal(newBT)




