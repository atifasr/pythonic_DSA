from math import *


def array_reverse(arr):
    size = len(arr)-1

    for i in range(size):

        temp = arr[i]
        arr[i] = arr[size-i]
        arr[size-i] = temp
        mid = floor(0 + size / 2)
        if i == mid:
            break
