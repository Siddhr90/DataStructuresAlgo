# stack implementation with SinglyLinkedList

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # makes the LL iterable
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)


    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return 'no elements to pop'
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return 'no elements to pop'
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print('***********')
print(customStack.pop())
print('***********')
print(customStack)

print('***********')
print(customStack.peek())




