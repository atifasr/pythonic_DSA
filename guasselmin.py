# guass elmination using partial pivoting

from math import *


def display_coeff(a, v):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j], v[j])


def display_vec(v):
    n = len(v)
    for i in range(n):
        print(f'x{i}'.title(), v[i])


def pivot(a, b, k):
    """function for partial pivoting"""
    large, temp, n = 0, 0, len(a)
    p = k
    large = abs(a[k][k])
    for i in range(k+1, n):
        if abs(a[i][k] > large):
            large = abs(a[i][k])
            p = i
    if p != k:
        for j in range(n):
            temp = a[p][j]
            a[p][j] = a[k][j]
            a[k][j] = temp

        temp = b[p]
        b[p] = b[k]
        b[k] = temp
    return


def elim(a, b):
    """elmination function"""
    factor = 0
    n = len(a)
    for k in range(n):
        # pivot function using partial pivoting
        pivot(a, b, k)

        for i in range(k+1, n):
            factor = a[i][k]/a[k][k]
            for j in range(k+1, n):
                a[i][j] = a[i][j] - factor * a[k][j]
            b[i] = b[i] - factor * b[k]
    return


def back_sub(a, b, v):
    """back substitution"""
    sum = 0
    n = len(a)
    v[n-1] = b[n-1]/a[n-1][n-1]

    k = n-1
    while k >= 0:
        sum = 0.0
        for j in range(k+1, n):
            sum += a[k][j] * v[j]
        v[k] = (b[k] - sum)/a[k][k]
        k -= 1
    return


def guass(a, v, b):
    """function for guass elmination"""
    elim(a, b)
    back_sub(a, b, v)


# driver function
a = [[2, 2, 1], [4, 2, 3], [1, -1, 1]]
v = ['x1', 'x2', 'x3']
b = [6, 4, 0]

guass(a, v, b)
display_vec(v)
