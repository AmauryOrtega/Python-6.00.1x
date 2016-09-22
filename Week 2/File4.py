# -*- coding: utf-8 -*-
"""
Created on 21/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# Tower of Hanoi
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)


print(Towers(3, 'P1', 'P2', 'P3'))


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        guess = b
    else:
        guess = a

    while not (a % guess == 0 and b % guess == 0):
        guess -= 1
    return guess


print('gcd:', gcdIter(117, 144))


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


def fib(x):
    '''
    x: integer >= 0
    returns Fibonacci of x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    else:
        guess = aStr[len(aStr) // 2]
        if (len(aStr) == 1 and guess != char):
            return False
        elif aStr == char:
            return True
        elif char == guess:
            return True
        else:
            if char > guess:
                return isIn(char, aStr[len(aStr) // 2:])
            else:
                return isIn(char, aStr[:len(aStr) // 2])


print(isIn('c', 'abcdef'))

'''
Modules:
import circle
    circle.fn()
    circle.var
from circle import * #Binds every circle have in the current scope
    fn()
    var
'''

# Handle files
# write mode
nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

# read mode
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()

import math


def polysum(n, s):
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi / n)
    perimeter = n * s
    return round(area + perimeter ** 2, 4)
