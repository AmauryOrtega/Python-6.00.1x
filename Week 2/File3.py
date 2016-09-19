# -*- coding: utf-8 -*-
"""
Created on 17/06/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)


def printName(firstName, lastName, reverse=False):  # Default value for reverse
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)


printName('Amaury', 'Ortega', False)
printName('Amaury', 'Ortega', reverse=False)
printName('Amaury', lastName='Ortega', reverse=False)
printName(lastName='Ortega', firstName='Amaury', reverse=False)  # The order doesn't matter


# Iterative
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


# Recursive
# a*b = a+a+a+....+a = a+a*(b-1)
def mult(a, b):
    if b == 1:  # Base case
        return a
    else:
        return a + mult(a, b - 1)  # Recursive step


# n!= n * (n - 1) * (n - 2) * ... * 1 = n*(n-1)!
def factorial(n):
    if n == 1:
        return 1  # Base case
    else:
        return n * factorial(n - 1)


def factorial_iter(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod
