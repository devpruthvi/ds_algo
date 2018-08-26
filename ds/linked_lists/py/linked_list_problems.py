from sll_node import Node
from linked_list_utils import generateRandomLinkedListWithLoop

length = 10
loopAt = 5
ll = generateRandomLinkedListWithLoop(length,9)
head = ll.head

def detect_if_loop_is_present(ll):
    head = ll.head
    if head == None:
        return False
    slowptr = head
    fastptr = head

    while True:
        if fastptr.next == None or fastptr.next.next == None:
            return False
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        if slowptr == fastptr:
            return True
    return False

def length_of_loop_in_ll(ll):
    head = ll.head
    if head = None:
        return -1
    slowptr = head
    fastptr = head
    while fastptr != None:
        if fastptr.next is None:
            return -1
        fastptr = fastptr.next.next
        slowptr = slowptr.next
        if slowptr == fastptr:
            length = 1
            slowptr = slowptr.next
            while slowptr != fastptr:
                slowptr = slowptr.next
                length += 1
            return length
    return -1

def get_loop_start_index(ll):
    head = ll.head
    if head == None:
        return -1
    fastptr = head
    slowptr = head
    loop_found = False
    while fastptr != None:
        if fastptr.next == None:
            return -1
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        if slowptr == fastptr:
            slowptr = head
            idx = 0
            if slowptr == fastptr:
                return (idx, slowptr)
            while slowptr != fastptr:
                slowptr = slowptr.next
                fastptr = fastptr.next
                idx += 1
                if slowptr == fastptr:
                    return (idx, slowptr)

print(get_loop_start_index(ll))