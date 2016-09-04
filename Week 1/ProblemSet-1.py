# -*- coding: utf-8 -*-
"""
Created on 04/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# 1 Problem - Number of vowels in s
s = 'ohwibinxspsamauytiltxug'
aux = 0
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        aux += 1
print("Number of vowels:", aux)

# 2 Problem - Number of bob occurences in s
s = "oobobwnloboboqobobobobobyobobobobb"


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


print("Number of times bob occurs is:", occurrences(s, "bob"))

# 3 Problem
s = 'azcbobobegghakl'

maxLen = 0
current = s[0]
longest = s[0]

# step through s indices
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
        # if current length is bigger update
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current = s[i + 1]
    i += 1

print('Longest substring in alphabetical order is: ' + longest)
