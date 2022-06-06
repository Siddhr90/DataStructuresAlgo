# queue using python list with no size limit

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == [] :
            return True
        else:
            return False

    def enqueue(self, value):               # Time complexity is amortized constant which means that when there are
                                            # many elements in the list, reallocation might be time consuming and can reach O(n) or O(n^2)
        self.items.append(value)
        return 'The item is successfully inserted at the end of the queue'

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            return self.items.pop(0)        # pop for lists without any argument removes the last element
                                            # and if you put (0) it removes the first element
                                            # takes O(n) time complexity, needs to shift all elements

    def peek(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            return self.items[0]            # O(1) time complexity

    def delete(self):
        self.items = None

customQueue = Queue()
print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)

print(customQueue)

print('*******')
print(customQueue.dequeue())
print(customQueue)
print('*******')
print(customQueue.peek())
customQueue.delete()



