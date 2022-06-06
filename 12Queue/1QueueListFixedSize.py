# queue with circular capacity

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]           # O(n) time complexity , space complexity is O(n)
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            return 'full'
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1 :
                    self.start = 0
            self.items[self.top] = value
            return 'The element is added at the end of the queue'

    def deQueue(self):
        if self.top == -1:
            return 'the queue is empty'
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start = self.start + 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.top == -1:
            return 'No elements in the queue'
        else:
            return self.items[self.start]

    def delete(self):
        self.top = -1
        self.start = -1
        self.items = [None] * self.maxSize





customQueue = Queue(3)

print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
print(customQueue)
print(customQueue.isFull())
print(customQueue.deQueue())
print(customQueue)
print(customQueue.peek())
print(customQueue)
customQueue.delete()
print(customQueue)



