class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # create doubly linked list
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "DLL is created"

    # insertion at the end of doubly linked list
    def insertDLL(self,nodeValue, location):
        if self.head == None:
            print(' The linked list does not exist')
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location == -1:
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode

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

    def traverseDLL(self):
        if self.head is None:
            print('there are no elements to traverse')
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def reverseTraverseDLL(self):
        if self.head is None:
            print('there are no elements to traverse')
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def searchDLL(self, target):
        if self.head is None:
            print('there are no elements to search')
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == target:
                    return tempnode.value
                node = tempnode.next
            return 'Value not present'


    def deleteNodeDLL(self, location):
        if self.head is None:
            print('DLL not present')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:
                index = 0
                curNode = self.head
                while index < location-1:           # we are reaching the node before the one we want to delete
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print('the node has been successfully deleted')

    def deleteEntireDLL(self):
        if self.head is None:
            print('DLL not present')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None            # deleting head and tail links are not enough because the nodes are also linked to each other
            print( "The DLL has been successfully deleted")




doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)                   # O(1) time and space complexity

print([node.value for node in doublyLL])


doublyLL.insertDLL(0,0)
print([node.value for node in doublyLL])
doublyLL.insertDLL(1,0)
print([node.value for node in doublyLL])
doublyLL.insertDLL(2,2)
print([node.value for node in doublyLL])
doublyLL.insertDLL(3,-1)
print([node.value for node in doublyLL])
doublyLL.insertDLL(4,4)
print([node.value for node in doublyLL])

#doublyLL.traverseDLL()
#doublyLL.reverseTraverseDLL()

#print(doublyLL.searchDLL(1))


doublyLL.deleteNodeDLL(-1)
print([node.value for node in doublyLL])

doublyLL.deleteNodeDLL(0)
print([node.value for node in doublyLL])
doublyLL.deleteNodeDLL(2)
print([node.value for node in doublyLL])

doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])
