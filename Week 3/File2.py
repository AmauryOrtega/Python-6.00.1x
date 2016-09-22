# -*- coding: utf-8 -*-
"""
Created on 22/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# List, Just like tuple can be modified
a_list = []
b_list = [2, 'a', 4, True]
L = [1, 2, 3]

L[1] = 5

# List are indexed from 0 to len(list)-1
# range(n) goes from 0 to n-1
total = 0
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L:
    total += i
print(total)

# add elements at the end of list
L.append(4)

# Concatenate lists
L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # L3 = [2, 1, 3, 4, 5, 6]
L1.extend([0, 6])  # L1 = [2, 1, 3, 0, 6]

# Remove elements from lists
L = [2, 1, 3, 6, 3, 7, 0]
L.remove(2)  # Removes the first appearance of 2
L.remove(3)
del (L[1])
L.pop()  # Removes the last element of the list by default

# String to list
list('string')
# Split the string removing white spaces returning a list
print('string of something'.split())
# Turns a list into a string
''.join(L)

# Example of before
s = 'I <3 CS'
print(list(s))
print(s.split('<'))
L = ['a', 'b', 'c']
print(''.join(L))
print('_'.join(L))

# Other list operations
L = [9, 6, 0, 3]
# Returns a sorted copy of L
print(sorted(L))
# Changes L
L.sort()
L.reverse()

'''
Range generates the first element and provides a method to produce the next one
range(5) -> [0, 1, 2, 3, 4]
range(2,6) -> [2, 3, 4, 5]
range(5, 2, -1) -> [5, 4, 3]
'''
for var in range(5):
    print(var)
for var in [0, 1, 2, 3, 4]:
    print(var)
