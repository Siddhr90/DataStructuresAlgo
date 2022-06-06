# Collections module

from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)
# deque([], maxlen=3)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
customQueue.append(4)           # does not return is full, instead removes the first element
print(customQueue)

print(customQueue.popleft())    # removes the first element
print(customQueue)
print(customQueue.clear())      # all elements are deleted
