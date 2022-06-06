# Inserting can be done :
# 1. at the beginning
# 2. After a node in the middle
# 3. At the end of the linkedlist

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in LinkedList
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    #traversal in SLL
    def traverseSLL(self):
        if self.head is None:
            print(" The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, nodeValue):
        if self.head is None:
            return 'the list does not exist'
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in the list"

    def deleteNode(self, location):
        if self.head is None:
            print ('the singly linked list doesnt exist')
        else:
            if location == 0:
                if self.head == self.tail:  # both referenceing to same node, which is only one node
                    self.head = None
                    self.tail = None
                else:                       # there are more than 1 nodes
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:  # both referenceing to same node, which is only one node
                    self.head = None
                    self.tail = None
                else:
                    node = self.head                    # temp node
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def delEntireSLL(self):
        if self.head is None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None            # O(1) time and space complxity

singlyLinkedList = SlinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)

singlyLinkedList.insertSLL(0,0)

singlyLinkedList.insertSLL(0,4)

print([node.value for node in singlyLinkedList])
#singlyLinkedList.traverseSLL()
#print("******************")
#print(singlyLinkedList.searchSLL(3))
#print(singlyLinkedList.searchSLL(33))


singlyLinkedList.deleteNode(3)
print([node.value for node in singlyLinkedList])

singlyLinkedList.deleteNode(-1)                     # time complxity  O(n), Space complexity O(1)
print([node.value for node in singlyLinkedList])

singlyLinkedList.delEntireSLL()
print([node.value for node in singlyLinkedList])
