from sll_node import SinglyLinkedList, Node
import random

def generateRandomLinkedList(length=10):
    head = Node(random.randint(1, 1000))
    temp = head
    for i in range(1, length):
        temp.next = Node(random.randint(1, 1000))
        temp = temp.next
    return SinglyLinkedList(head)

def generateRandomLinkedListWithLoop(length=10, loopAt=None):
    if loopAt is None:
        loopAt = random.randint(0, length)
    loopAt = loopAt % length
    l = generateRandomLinkedList(length)
    temp = l.head
    for i in range(0, loopAt):
        temp = temp.next
    loop_start = temp
    while temp.next != None:
        temp = temp.next
    tail = temp
    tail.next = loop_start
    return l