# we need to return the node at which intersection happens
# we could just check if the tail is same for both lls for intersection, we we need the node at which they intersect

from LinkedListClass import LinkedList, Node

def intersectCheck(llA,llB) :
    if llA.tail != llB.tail:        # we are checking if the nodes are intersecting or not by looking at the last node
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenB > lenA else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        longerNode = longerNode.next
        shorterNode = shorterNode.next

    return longerNode

# helper addition method

def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0, 10)

llB = LinkedList()
llB.generate(4,0, 10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,14)

print(llA)
print(llB)

print(intersectCheck(llA,llB))
