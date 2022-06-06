# practice

from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

# python's default function, called when print or str function is invoked
    def __str__(self):
        return str(self.value) # we are setting that when print is called it prints the value

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    # making function iterable
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    # next we modify the len() function
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count +=1
            node = node.next
        return count

    # we ll create an add function to add value at end
    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        return self.tail

    # generate n random numbers located between the min and max values
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self

#customLL = LinkedList()
#customLL.generate(10,0,99)
#print(customLL)
#print(len(customLL))









