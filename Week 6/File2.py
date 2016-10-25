# -*- coding: utf-8 -*-
"""
Created on 21/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def fact_inter(n):
    """Assumes n an int >= 0"""
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
    # number of steps = 1 + 5n + 1
    # ignore the 1s because with a big n, they don't matter
    # ignore 5 because no matter what value multiplies n, the growth is
    # because of n

    # O(n) -> lineal


"""
Examples
n^2 + 2n + 2            -> O(n^2)
n^2 + 100000n + 3^1000  -> O(n^2)
log(n) + n + 4          -> O(n)
0.0001*n*log(n) + 300n  -> O(n*log(n))
2n^30 + 3^n             -> O(3^n)
"""

"""
Classes
O(1)        constant
independent of input
can have loops or recursive calls but the numbers of iterations is
independent of the input
"""


def intToStr(i):
    """
    O(log n)    logarithm
    bisection search
    binary search of a list
    """
    # O(log(n))
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i //= 10
    return result


def addDigits(s):
    """
    O(n)        lineal
    searching a list in sequence if an element is present
    add characters of the digits from a string
    """
    # O(len(s))
    val = 0
    for c in s:
        val += int(c)
    return val


def fact_inter(n):
    """
    O(n) lineal
    """
    # O(n)
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def fact_recur(n):
    """ n >= 0"""
    # O(n)
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)


def isSubset(l1, l2):
    """
    O(n^C)    polynomial

    O(len(l1)*len(l2)) with the worst case when they're the same length
    O(n^2)
    """
    for e1 in l1:
        matched = False
        for e2 in l2:
            if e1 is e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(l1, l2):
    """
    :param l1: list
    :param l2: list
    :return: a list with each element appearing only once
    O(len(l1)*len(l2)) -> worst case when they're the same length
    O(n^2), the second loop gets overwhelm by the first one
    """

    tmp = []
    # len(l1)*len(l2)
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    # len(l1)
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res


def g(n):
    """ :param n: integer >= 0 """
    # O(n^2)
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x


"""
O(C^n)      exponential
"""

"""
O(n log n)  log lineal
"""


# LAWS
def test(n):
    #  Law of addition for O(), Only the strongest survive
    # O(n) + O(n*n) = O(n+n*n) = O(n*n) = O(n^2)
    for i in range(n):
        print('a')
    for j in range(n * n):
        print('b')


def test2(n):
    # Law of multiplication,
    # O(n)*O(n) = O(n*n) = O(n^2)
    for i in range(n):
        for j in range(n):
            print('a')
