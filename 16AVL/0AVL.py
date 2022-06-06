
import HelperQueueLinkedList as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1                                                     # this is extra compared to BST


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

# helper1 for insertion
def getHeight(rootNode):
    if not rootNode:
        return 0            # since root node doesn't exist
    return rootNode.height

# helper2 for insertion
def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# helper3 for insertion
def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# helper4 for insertion
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)              # O(logN)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)            # O(logN)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    # case1: if left side is greater than right side and node to be inserted is on left side --> this will be a left-left condition
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    # case2 : left-right condition node value is greater than root node's left value
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # case3:
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    # case4:
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

# helper for delete to return successor
def getMinValueNode(rootNode):
    if not rootNode:
        return rootNode
    else:
        return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    if balance > 1 and getBalance(rootNode.leftChild) >= 0 :        # LL
        return rightRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) <= 0 :        # LR
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0 :        # RR
        return leftRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) >= 0 :        # RL
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)

