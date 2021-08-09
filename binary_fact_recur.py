from math import *


def binary_srch_recur(data, st, end):

    if st < end:
        mid = floor(st+end/2)
        binary_srch_recur(data, st, mid)
        binary_srch_recur(data, mid+1, end)
        print(st, ' ', end)
