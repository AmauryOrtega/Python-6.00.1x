# -*- coding: utf-8 -*-
"""
Created on 03/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


hi = "Hello"
name = "Amaury"
greetings = hi + " " + name
print(greetings)

# Strings
print('ab' + 'cd')  # abcd
print(3 * "amaury")  # amauryamauryamaury
print(len("amaury"))
print("amaury"[0])
print("amaury"[1])  # Can give IndexError
print("amaury"[-1])  # -1 is last caracther 'y'

"""
[#1:#2:#3]
From #1 to (#2-1)
Default #1 = 0
Default #2 = last index
Only ':', makes a copy of string
"""
print("amaury"[1:3])
print("amaury"[:3])
print("amaury"[1:len("amaury")])
print("amaury"[:])
cls()

x = 1
x_str = str(x)
print("my number is", x, ".", "x = ", x)
print("my number is " + x_str + ". " + "x = " + x_str)
print("my number is {0}. x = {1}".format(x_str, x_str))
cls()

text = input("Enter text: ")
num = int(input("Enter an integer: "))
cls()

# Loops
n = 0
while n < 5:
    print(n)
    n += 1

# Replace <
n = 0
for n in range(5):
    print(n)

# Inf and Sup limits
n = 0
for i in range(7, 10):
    n += i
print(n)

# Increments
n = 0
for i in range(5, 11, 2):
    n += i
print(n)

# Break
n = 0
for i in range(5, 11, 2):
    n += i
    if n == 5:
        break
print(n)

cls()

# X^2
x = 3
answer = 0
steps = x
while steps != 0:
    answer += x
    steps -= 1
print(str(x) + "*" + str(x) + " = " + str(answer))

# Guess and check method
# Square Root
x = int(input("Enter an Integer: "))
answer = 0
while answer ** 3 < x:
    answer += 1
if answer ** 3 != x:
    print(str(x) + " is not a perfect cube")
else:
    print("Square root of " + str(x) + " is " + str(answer))

# Square root (+/-)
x = int(input("Enter an Integer: "))
answer = 0
while answer ** 3 < abs(x):
    answer += 1
if answer ** 3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x < 0:
        answer = - answer
    print("Square root of " + str(x) + " is " + str(answer))

# Guess and check using for
cube = 8
for guess in range(cube + 1):
    if guess ** 3 == cube:
        print("Square root of", cube, "is", guess)

# (+/-)
cube = 8
guess = 0
for guess in range(abs(cube + 1)):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Square root of", cube, "is", guess)
