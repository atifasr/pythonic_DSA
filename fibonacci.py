
from math import *


def fibo(n):
    """fibonacci series"""
    # Enter number of terms needed                   #0,1,1,2,3,5....
    a = n
    f = 0  # first element of series
    s = 1  # second element of series
    if a <= 0:
        print("The requested series is", f)
    else:
        print(f, s, end=" ")
        for x in range(2, a):
            next = f+s
            print(next, end=" ")
            f = s
            s = next


# main func
temp = 0
print('fibonacci series'.title(), fibo(50))
