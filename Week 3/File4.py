# -*- coding: utf-8 -*-
"""
Created on 25/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def applyToEach(L, f):
    '''
    :param L: list
    :param f: a function
    :return: mutates L using f in each element of L
    '''
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]
print('L:', L)
applyToEach(L, abs)
print('L:', L)
applyToEach(L, int)
print('L:', L)


def applyFuns(L, x):
    '''
    :param L: list of functions
    :param x: a number
    '''
    for f in L:
        print(f(x))


def applyEachTo(L, x):
    '''
    :param L: list of functions
    :param x: value
    :return: list of [f1(x), f2(x), ..., fn(x)]
    '''
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


applyFuns([abs, int], -4.3)

# one function to a data structure
# gives back a new iterable, not a list
map(abs, [1, -2, 3, -4])

for elt in map(abs, [1, -2, 3, -4]):
    print(elt)

# If the function takes multiple arguments
L1 = [1, 28, 36]
L2 = [2, 57, 9]
for elt in map(min, L1, L2):
    print(elt)
