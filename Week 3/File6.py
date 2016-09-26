# -*- coding: utf-8 -*-
"""
Created on 26/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def fib(x):
    global numFibCalls
    numFibCalls += 1
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fib(x - 1) + fib(x - 2)


def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans


numFibCalls = 0
print(fib(34))
print('function calls', numFibCalls)

numFibCalls = 0
d = {1: 1, 2: 2}
print(fib_efficient(34, d))
print('function calls', numFibCalls)
