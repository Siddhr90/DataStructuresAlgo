# for sharing data between processors

from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())

# all methods work similar to python queue module except task_done and join

