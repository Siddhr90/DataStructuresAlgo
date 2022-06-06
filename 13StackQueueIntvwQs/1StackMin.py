# in addition to push and pop method, we should have a min method that can return the minimum element
# all these methods should operate in O(1) time complexity

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string

class Stack:
    def __init__(self):
        self.top = None         # top is equivalent to head here
        self.minNode = None     # basically you are maintaining two linkedlists, this one is for the min values
                                # as you push you will adjust the ll for min values accordingly

    def min(self):
        if not self.minNode:            # means that it is None
            return None
        return self.minNode.value

    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item

customStack = Stack()
customStack.push(5)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.push(3)
print(customStack.min())

customStack.pop()
print(customStack.min())













