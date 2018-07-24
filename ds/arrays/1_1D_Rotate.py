#!/usr/bin/python3
"""

Given an array, rotate it d times

arr = 1,2,3,4,5
d = 3

result: 4,5,1,2,3

"""


def gcd(a, b):  # might as well use math.gcd
    if a == 0 or b == 0:
        return 0
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b


def rotate_arr(arr, d):
    length = len(arr)
    partition_size = gcd(length, d)
    for i in range(partition_size):
        j = i
        temp = arr[i]
        while True:
            k = j + d
            if k >= length:
                k -= length
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def reverse_arr(arr, start_inclusive=0, end_exclusive=None):
    if end_exclusive is None:
        end_exclusive = len(arr)
    upto = (end_exclusive - start_inclusive) // 2
    for i in range(0, upto):
        other_ind = end_exclusive - i - 1
        temp = arr[start_inclusive + i]
        arr[start_inclusive + i] = arr[other_ind]
        arr[other_ind] = temp


def rotate_arr_by_reversal(arr, d):
    length = len(arr)
    d = d % length
    reverse_arr(arr)
    reverse_arr(arr, 0, length - d)
    reverse_arr(arr, length - d, length)


if __name__ == '__main__':
    test_arr = list(range(1, 15))
    d = 6
    rotate_arr(test_arr, d)
    print(test_arr)
    test_arr2 = list(range(1, 15))
    rotate_arr_by_reversal(test_arr2, d)
    print(test_arr2)
