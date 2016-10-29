# -*- coding: utf-8 -*-
"""
Created on 29/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

trans = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
         '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '10': 'shi'}


def convert_to_mandarin(text):
    """Assumes text is a string of a number between 0 and 99"""
    if len(text) > 1:
        if int(text[0]) > 1:
            ans = trans[text[0]] + ' ' + trans['10']
            if int(text[1]) != 0:
                ans += ' ' + trans[text[1]]
        else:
            ans = trans['10']
            if int(text[1]) != 0:
                ans += ' ' + trans[text[1]]
    else:
        ans = trans[text[0]]
    return ans


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """

    def linc(L):
        L_copy = L.copy()
        maxLen = 0
        current = [L[0]]
        longest = [L[0]]

        for i in range(len(L_copy) - 1):
            if L_copy[i + 1] >= L_copy[i]:
                current.append(L_copy[i + 1])
                if len(current) > maxLen:
                    maxLen = len(current)
                    longest = current.copy()
            else:
                current.clear()
                current = [L_copy[i + 1]]
                # i += 1
        return longest

    def ldec(L):
        L_copy = L.copy()
        maxLen = 0
        current = [L_copy[0]]
        longest = [L_copy[0]]

        for i in range(len(L_copy) - 1):
            if L_copy[i + 1] <= L_copy[i]:
                current.append(L_copy[i + 1])
                if len(current) > maxLen:
                    maxLen = len(current)
                    longest = current.copy()
            else:
                current.clear()
                current = [L_copy[i + 1]]
                # i += 1
        return longest

    def sum(L):
        sum = 0
        for e in L:
            sum += e
        return sum

    linc = linc(L)
    ldec = ldec(L)

    if len(linc) == len(ldec):
        if L.index(linc[0]) < L.index(ldec[0]):
            return sum(linc)
        else:
            return sum(ldec)
    elif len(linc) > len(ldec):
        return sum(linc)
    else:
        return sum(ldec)


L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
L = [5, 4, 10]

print(longest_run(L))

"""
s = 'azcbobobegghakl'

# initialise tracker variables
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

    i += 1  # Linea de mas

print('Longest substring in alphabetical order is: ' + longest)
"""
