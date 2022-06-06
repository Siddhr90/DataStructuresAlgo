# You have 2 numbers stored in lists. the digits are stored in reverse order
# write a function that adds the two numbers and returns the sum as a linkedlist

from LinkedListClass import LinkedList

def sumLists(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        carry = result / 10
        result = int(result%10)
        ll.add(result)

    if int(carry) != 0:
        ll.add(int(carry))
    return ll

customll1 = LinkedList()
customll1.generate(5, 0, 9)

customll2 = LinkedList()
customll2.generate(5, 0, 9)


print(customll1)
print(customll2)
print(sumLists(customll1,customll2))                # Time and Space complexity O(n)





