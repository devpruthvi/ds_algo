#!/usr/bin/python
from sll_node import Node, SinglyLinkedList
from linked_list_utils import generateRandomLinkedListWithLoop, generateRandomLinkedList

length = 10
ll = generateRandomLinkedListWithLoop(length, 9)
l = generateRandomLinkedList(length)
head = ll.head


def detect_if_loop_is_present(ll):
    head = ll.head
    if head == None:
        return False
    slowptr = head
    fastptr = head

    # floyd warshall cycle finding algo, if fast and slowptr meet at some point, loop is present
    while True:
        if fastptr.next == None or fastptr.next.next == None:
            return False
        slowptr = slowptr.next
        fastptr = fastptr.next.next
        if slowptr == fastptr:
            return True
    # else no loop
    return False


def length_of_loop_in_ll(ll):
    head = ll.head
    if head == None:
        return -1
    slowptr = head
    fastptr = head

    # keep oneptr at intersection point & move one of them to start then keep forwarding them until they meet that'd
    # be the length of the loop, mathematical proof with modulo arithmetic exists to prove this

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

    # same as above algorithm instead of length, calculate start index of loop in same way as explained above

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


def get_middle_node(ll):

    # slowptr, fastptr, by the time fastptr reached end, slowptr will reach middle node

    head = ll.head
    if head == None:
        return head
    slowptr = head
    fastptr = head
    while fastptr != None:
        if fastptr.next == None or fastptr.next.next == None:
            break
        slowptr = slowptr.next
        fastptr = fastptr.next.next
    return slowptr


def check_palindrome(ll):
    # Test:
    # palind_l = SinglyLinkedList.create_from_array([1,2,3,4,5,4,3,1,1])
    # check_palindrome(palind_l)

    # get middle node, reverse the rest half as we move forward , keep one ptr to head , other to end
    # forward end ptr until it meets mid

    head = ll.head
    if head == None:
        return
    mid = get_middle_node(ll)
    temp = mid
    prev = mid
    temp = temp.next
    i = 0
    while temp != None:
        prev, temp.next, temp = temp, prev, temp.next
    temp = head
    while prev != mid:
        if temp.val != prev.val:
            return False
        temp = temp.next
        prev = prev.next
    return True

def check_palindrome_recursive(ll):
    """
    Test:
    palind_l = SinglyLinkedList.create_from_array([1,2,3,4,5,4,3,2,1])
    print(check_palindrome_recursive(palind_l))
    """
    # push all values onto stack & compare both stack & data at hand

    head = left = ll.head
    if head == None:
        return

    def check_palindrome_helper(right):
        nonlocal  left
        if right == None:
            return True
        x = check_palindrome_helper(right.next)

        print(x, left, right)

        if not x:
            return False
        
        retval = False
        if left.val == right.val:
            retval = True
        left = left.next
        return retval

    return check_palindrome_helper(head)