# Imagine a literal stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure set of stacks to mimic this.
# SetOfStacks should be composed of several stacks and should create a new stack once
# the previous one exceeds the capacity, Set of stacks push and pop should behave identical to the original stack

class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            print("this")
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None


customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)

print(customStack.pop_at(2))        # if you forget to put return in your pop function, this will always print 'None'
print(customStack.pop_at(2))
print(customStack.pop_at(1))
print(customStack.pop_at(1))
print(customStack.pop())





