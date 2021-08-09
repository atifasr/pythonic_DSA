# from math from *
import tree_meth as bin_
from random import *
import array_reverse as arr_rev
import warshall_algo as wrshl
import binary_fact_recur as bin_srch
from math import *


def curv(x):
    return (e**-x)-x


def secant_meth():
    """Root finding using secant algorithm"""

    x = 0
    ea = 0
    curr = 1
    prev = 0
    x_old = 0
    x_curr = 0

    for val in range(15):
        # secant logic
        x = round(curr-(curv(curr)*(prev-curr)/curv(prev)-curv(curr)), 2)
        x_curr = curr = x

        if curr != 0:
            ea = abs(round((x_curr-x_old)/curr, 2))

        print(x, 'error estimate'.title(), ea)
        x_old = prev = curr

        if ea < 0.56:
            break


secant_meth()
