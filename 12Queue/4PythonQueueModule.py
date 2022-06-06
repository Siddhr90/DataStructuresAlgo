# Queue module

# especially useful in threaded programming where info needs to be exchanged safely between multiple threads

# 1. FIFO Queue
# 2. LIFO Queue
# 3. Priority Queue         # entries are sorted and first element is returned

# for FIFO queue we use constructor
# we will use only the following methods
# qsize(), empty() , full() , put() , get() , task_done() , join()

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.qsize())

customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())

print(customQueue.full())
print(customQueue.empty())
print(customQueue.get())
print(customQueue.qsize())


