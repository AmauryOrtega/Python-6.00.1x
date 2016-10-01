# -*- coding: utf-8 -*-
"""
Created on DATE

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# stuff ="iQ"
# stuff =( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
# stuff =[ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]

# stuff =["iQ"]
# stuff =("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
# stuff = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
for thing in stuff:
    if thing == 'iQ':
        print("Found it")


def Square(x):
    return SquareHelper(abs(x), abs(x))


def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n - 1, x) + x


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0

    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0
    minEpsilon = num
    while abs(base ** exponent - num) < minEpsilon:
        minEpsilon = abs(base ** exponent - num)
        exponent += 1
    return exponent - 1


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for i in range(len(listA)):
        sum += listA[i] * listB[i]
    return sum


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    L.reverse()
    for list in L:
        list.reverse()


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}
    for i in d1.keys():
        if (not inter.__contains__(i)) and d2.__contains__(i):
            inter[i] = f(d1[i], d2[i])
        elif (not diff.__contains__(i)) and (not d2.__contains__(i)):
            diff[i] = d1[i]
    for i in d2.keys():
        if (not inter.__contains__(i)) and d1.__contains__(i):
            inter[i] = f(d1[i], d2[i])
        elif (not diff.__contains__(i)) and (not d1.__contains__(i)):
            diff[i] = d2[i]
    return (inter, diff)


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    L_copy = L[:]
    for i in L_copy:
        if g(f(i)):
            L[L.index(i)] = i
        else:
            L.remove(i)
    if len(L) == 0:
        return -1
    else:
        max = L[0]
        for i in L:
            if i >= max:
                max = i
        return max


def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    t = []
    for i in aList:
        if not isinstance(i, list):
            t.append(i)
        else:
            t.extend(flatten(i))
    return t
