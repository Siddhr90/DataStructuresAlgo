# Double Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.Prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:              # since last node points to the first node
                break

    # Creation of Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return 'The circular DL is created succesfully'

    def insertCDLL(self, nodeValue, location):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode

            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode             # do not forget this step

            else:
                index = 0
                tempNode = self.head
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                nextNode.prev = newNode

    def traverseCDLL(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next

    def reverseTraverseCDLL(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev
            if tempNode == self.tail:
                break

    def searchNodeCDLL(self, target):
        tempNode = self.head
        while tempNode:
            if tempNode.value == target:
                return target
            tempNode = tempNode.next
            if tempNode == self.head:
                return 'value not present'

    def deleteNode(self, location):
        if self.head is None:
            print('the CDLL does not exist')

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None

                else:
                    tempNode = self.head.next
                    self.tail.next = tempNode
                    tempNode.prev = self.tail
                    self.head.prev = None
                    self.head.next = None
                    self.head = tempNode

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.tail.prev
                    tempNode.next = self.head
                    self.head.prev = tempNode
                    self.tail.prev = None
                    self.tail.next = None
                    self.tail = tempNode

            else:
                index = 0
                tempNode = self.head
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode
                #nextNode.prev = None
                #nextNode.next = None


    def deleteAllCDLL(self):
        tempNode = self.head
        self.tail.next = None               # do not forget to delete that tail .next to head connection
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
            if tempNode == self.tail:
                break
        self.head = None
        self.tail = None








circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)               # space and time cmplxty O(1)
print([node.value for node in circularDLL])

circularDLL.insertCDLL(6,0)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(9,-1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(2,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(3,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(4,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(5,1)
print([node.value for node in circularDLL])

# circularDLL.traverseCDLL()
#circularDLL.reverseTraverseCDLL()

#print(circularDLL.searchNodeCDLL(15))

circularDLL.deleteNode(2)
print([node.value for node in circularDLL])

circularDLL.deleteAllCDLL()
print([node.value for node in circularDLL])
