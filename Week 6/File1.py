# -*- coding: utf-8 -*-
"""
Created on 13/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# Using time
"""
Y time varies between algorithms
N time varies between implementations
N time varies between computers
N time is not predictable based on small inputs, too much tests are needed
"""
import time


def c_to_f(c):
    return c * 9 / 5 + 32


t0 = time.clock()
c_to_f(1000)
t1 = time.clock() - t0

print("t =", t0, ":", t1, "s,")

# Counting operations
# Mathematical operations, comparisons, assignments, accessing data in memory
"""
Y depends on algorithm
N depends on implementations
Y independent of computers
N which operations you should count
"""


def c_to_f(c):
    return c * 9.0 / 5 + 32  # 3 operations


def my_sum(x):
    total = 0  # 1 Op = 1 Operation
    for i in range(x + 1):  # 1 Op
        total += 1  # 2 Op, sum and assignment
    return total
    # Total Op = 1+3X Ops


"""
Express efficiency in terms of input
You must decide what the input is: integer, length of list

in search of element
BEST CASE = e is the first element
WORST CASE = e is not in the list
AVERAGE CASE = e is about half of the list
"""


def search_for_element(l, e):
    for e in l:
        if e is e:
            return True
    return False


"""
Types of orders of growth
Constant
logarithmic
linear
n log n
quadratic
exponential
"""
