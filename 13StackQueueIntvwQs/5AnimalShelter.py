# An animal shelter which holds only dogs and cats, operates strictly on FIFO
# People must adopt either the oldest (based on arrival time) of all animals at the shelter
# or they can select whether they like a dog or a cat( and will receive the oldest animal of that type)
# They cannot select which specific animal they would like
# Create DS to maintain this system and implement operations such as enQueue, dequeueAny, dequeueDog and dequeueCat

class AnimalShelter:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [x for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.list.append(item)

    def dequeueAny(self):
        if self.isEmpty():
            return 'The list is Empty'
        else:
            return self.list.pop(0)

    def dequeueCat(self):
        if self.isEmpty():
            return 'The list is Empty'
        else:
            i = 0
            while self.list[i] != 'c':
                i += 1
            return self.list.pop(i)

    def dequeueDog(self):
        if self.isEmpty():
            return 'The list is Empty'
        else:
            i = 0
            while self.list[i] != 'd':
                i += 1
            return self.list.pop(i)

customStack = AnimalShelter()
customStack.enqueue('d')
customStack.enqueue('d')
customStack.enqueue('c')
customStack.enqueue('d')
customStack.enqueue('c')
print(customStack)
print(customStack.dequeueCat())
print(customStack)








