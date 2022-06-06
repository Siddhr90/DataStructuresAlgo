# circular Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:  # if break added to exit when compared to SLL
                break
            node = node.next

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"      # time and space complexity O(1)

    def insertCSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            return 'LinkedList has not been created'
        # 1. at beginning
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif location == -1:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        else:
            index = 0
            tempNode = self.head
            while index < location-1 :
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode
            # if tempNode == self.tail:
            #    self.tail = newNode
            return " the value has been successfully inserted"

    def traverseCSLL(self):
        if self.head is None:
            print('The CSLL is not present')
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break

    def searchCSLL(self, target):
        if self.head is None:
            return 'the CSLL is not created'
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == target:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'target value not present'

    def deleteNodeCSLL(self, location):
        if self.head is None:
            print("The linked list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:      # only one element
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    curNode = self.head
                    while curNode is not None:
                        if curNode.next == self.tail:
                            break
                        curNode = curNode.next
                    curNode.next = self.head
                    self.tail = curNode
            else:
                index = 0
                tempNode = self.head
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteall(self):
        self.head = None
        self.tail.next = None
        self.tail = None

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
print([node.value for node in circularSLL])
print('*********************************')
circularSLL.insertCSLL(4,0)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(3,-1)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(2,2)                 # insertion time cmplxty is O(n) and space Cmplxty is O(1)
print([node.value for node in circularSLL])

'''
print('*********************************')
circularSLL.traverseCSLL()

print('*********************************')
print(circularSLL.searchCSLL(2))
print(circularSLL.searchCSLL(9)) # O(n) time complexity , O(1) space cmplxty

print('*********************************')


circularSLL.deleteNodeCSLL(2)
print([node.value for node in circularSLL])
circularSLL.deleteNodeCSLL(-1)
print([node.value for node in circularSLL])
circularSLL.deleteNodeCSLL(-1)
print([node.value for node in circularSLL])
#circularSLL.createCSLL(0)

circularSLL.deleteNodeCSLL(0)
'''

circularSLL.deleteall()

print([node.value for node in circularSLL])