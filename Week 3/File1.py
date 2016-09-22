# -*- coding: utf-8 -*-
"""
Created on 21/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# Tuples
# can't do t[2] = 3 just like strings
te = ()
t = (2, 'one', 3)
print(t[2])
print(t + (5, 6))
print(t[1:2])
print(t[1:3])

# swap variable values
x = 1
y = 2
print('x:', x, 'y:', y)
(x, y) = (y, x)
print('x:', x, 'y:', y)


# Can make a function that returns multiple values
def quotient_and_reminder(x, y):
    q = x // y
    r = x % y
    return (q, r)
    # return q, r also works


(quot, rem) = quotient_and_reminder(4, 5)
print(quot, rem)


# Iterations on a tuple
def get_Data(aTuple):
    """
    :param aTuple: a tuple of tuples that contains ints and strings, ej: ((1, 'one'), (2, 'two'), (3, 'three'))
    :return: a tuple of minimum number, the maximum number and the amount of unique words
    """
    nums = ()
    words = ()
    for t in aTuple:
        nums += (t[0],)  # the comma tells python is a tuple, not an int
        if t[1] not in words:
            words += (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
