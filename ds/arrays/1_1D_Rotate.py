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


if __name__ == '__main__':
    test_arr = list(range(1, 15))
    d = 6
    rotate_arr(test_arr, d)
    print(test_arr)
