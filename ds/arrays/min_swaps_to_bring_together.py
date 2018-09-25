"""
Given an array and a number k, find minimum number of swaps required to bring all the elements less than
or equal to k together
"""

def find_min_swaps(l, k):
    # get window range = num elements <= k
    min_count = len([x for x in l if x <= k])
    num_greater = 0

    # calculate initial value for sliding window, we want to check for every window of size min_count , how many number
    # of elements are greater than k because those are what would be swapped to make them together
    for i in range(0, min_count):
        if l[i] > k:
            num_greater += 1

    # move forward with sliding window and get the window which has mininum number of elements > k ( minimum swaps will
    # be required

    i = 0
    j = min_count
    cur_num_greater = num_greater
    while j < len(l):
        if l[i] > k:
            cur_num_greater -= 1
        if l[j] > k:
            cur_num_greater += 1
        i += 1
        j += 1
        num_greater = min(num_greater, cur_num_greater)
    return num_greater

"""

Test:
print(find_min_swaps([2,7,9,5,8,7,4], 5))
Answer: 2 swaps

"""