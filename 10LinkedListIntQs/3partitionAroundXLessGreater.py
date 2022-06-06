# write a code to partition around x such that nodes less than x come before all nodes greater than or equal to x

from LinkedListClass import LinkedList

def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL,30)
print(customLL)






