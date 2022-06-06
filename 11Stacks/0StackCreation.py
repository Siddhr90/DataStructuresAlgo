# creation of stack with basic operations using Lists where there is no limit on size of stack

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)         # time is amortized constant, so allocation might be towards O(n) time
        return 'The element has been successfully inserted'

    def pop(self):
        if self.isEmpty():
            return 'There are no elements in the stack'
        else:
            return self.list.pop()      # returns last element and removes that element

    def peek(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list[-1]

    def delete(self):
        self.list = None            # results in the deletion of the entire stack

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
#print(customStack)
print('*******')
print(customStack.pop())
print('*******')
print(customStack)
print('*******')
print(customStack.peek())
print('*******')
print(customStack)
print('*******')
customStack.delete()
#