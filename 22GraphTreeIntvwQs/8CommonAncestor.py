# find common ancestor

def findNodeInTree(target, rootNode):
    if not rootNode:
        return False
    if rootNode == target:
        return True
    else:
        return findNodeInTree(target,rootNode.left) or findNodeInTree(target, rootNode.right)

def findFirstCommonAncestor(n1, n2, root):
    n1onLeft = findNodeInTree(n1, root.left)
    n2onLeft = findNodeInTree(n2, root.left)

    if n1onLeft ^ n2onLeft:                                                # xor operator
        return root
    else:                                                                  # means both are true
        if n1onLeft:
            return findFirstCommonAncestor(n1,n2, root.left)
        else:
            return findFirstCommonAncestor(n1, n2, root.right)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
rootNode = Node(55, node44, node77)

commonAncestor = findFirstCommonAncestor(node88, node33, rootNode)
print(commonAncestor.value)

