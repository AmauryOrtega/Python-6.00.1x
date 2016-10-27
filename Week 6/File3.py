# -*- coding: utf-8 -*-
"""
Created on 26/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def h(n):
    """Assumes n an int >= 0"""
    answer = 0
    s = str(n)
    for c in s:  # Lineal O(len(s)) but what is the O in terms of n?
        answer += int(c)
    return answer
    # O(Log(n)) because the way n is divided by 10 when is n converted to a string


def fib_iter(n):
    """O(1) + O(n) + O(1) = O(n)"""
    if n == 0:
        # O(1)
        return 0
    elif n == 1:
        # O(1)
        return 1
    else:
        # O(1)
        fib_i = 0
        fib_ii = 1
        for i in range(n - 1):  # O(n)
            tmp = fib_i
            fib_i = fib_ii
            fib_ii += tmp
        # O(1)
        return fib_ii


def fib_recur(n):
    """Assumes n an int >= 0"""
    """O(2^n)"""
    if n == 0:
        # O(1)
        return 0
    elif n == 1:
        # O(1)
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)  # O(2^n)


def sum_list(l):
    """O(len(l))"""
    total = 0
    for element in l:
        total += element
    return total
