# -*- coding: utf-8 -*-
"""
Created on 16/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# Basic function
def is_even(i):
    """
    Input: i, a positive int
    Return True if i is even, otherwise False
    """
    print("Hi")
    return i % 2 == 0


# function returned in a function
def func_a():
    print('inside func_a')


def func_b(y):
    print('inside func_b')
    return y


def func_c(z):
    print('inside func_c')
    return z()


print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
######################
"""
#no funciona por que crea x sin tener x en el scope de h
def h(y):
    x = x + 1
x = 5
h(x)
print(x)
#fnciona porque print busca x en todos los scope
def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)
"""


# function inside function
def g(x):
    def h():
        x = 'abc'

    x = x + 1
    print('in g(x): x =', x)
    h()
    return x


x = 3
z = g(x)
