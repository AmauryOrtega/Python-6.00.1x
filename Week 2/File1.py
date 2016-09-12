# -*- coding: utf-8 -*-
"""
Created on 09/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""
from builtins import print

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
