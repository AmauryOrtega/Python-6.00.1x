# -*- coding: utf-8 -*-
"""
Created on 09/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

ans = 0
negation_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    negation_flag = True
while ans ** 2 < x:
    ans = ans + 1
if ans ** 2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if negation_flag:
        print("Just checking... did you mean", -x, "?")

s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Entender a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess ** 3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)

# Square Root using bisection search
x = 25
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num_guesses = ' + str(num_guesses))
print(str(ans) + ' is close to square root of ' + str(x))

# Cube Root using bisection search
cube = 125
epsilon = 0.01
num_guesses = 0
low = 0.0
high = cube
ans = (high + low) / 2.0

while abs(ans ** 3 - cube) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    num_guesses += 1
    if ans ** 3 < cube:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num_guesses = ' + str(num_guesses))
print(str(ans) + ' is close to cube root of ' + str(cube))

# Guessing secret number using bisection search
high = 100
low = 0
text = ' '
print('Please think of a number between ' + str(low) + ' and ' + str(high) + '!')
while text != 'c':
    ans = (high + low) // 2
    print('Is your secret number', str(ans), '?')
    text = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if text == 'h':
        high = ans
    elif text == 'l':
        low = ans
    elif text == 'c':
        print('Game over. Your secret number was:', str(ans))
    else:
        print(
            "Please Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        continue

# Dec to bin
num = int(input("Integer number to be converted to binary: "))
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
if isNeg:
    result = '-' + result
print('bin: ' + str(result))

# Float Dec to bin
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2 ** p) * x) % 1 != 0:
    print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))
    p += 1

num = int(x * (2 ** p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + result)

# Square root using Newton-Raphson
'''
For any polynomial in one variable
wanted to find r such f(r)=0
g is an aproximate root of f if
g-f(g)/f'(g)
'''
epsilon = 0.01
y = 24.0
guess = y / 2.0
num_guesses = 0

while abs(guess ** 2 - y) >= epsilon:
    num_guesses += 1
    guess -= ((guess ** 2) - y) / (2 * guess)
print('num_guesses = ' + str(num_guesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
