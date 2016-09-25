# -*- coding: utf-8 -*-
"""
Created on 24/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# List are pointers and can be accessed with different variables
warm = ['red', 'yellow', 'orange']
hot = warm

print('warm:', warm)
print('hot:', hot)

hot.append('pink')

print('warm:', warm)
print('hot:', hot)

# Clone a list
cool = ['blue', 'green', 'grey']
chill = cool[:]

# Sort lists
print('\n' + '-' * 5 + 'Sort Lists' + '-' * 5)
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print('warm:', warm)
print('sortedwarm:', sortedwarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool)
print('cool:', cool)
print('sortedcool:', sortedcool)

# Nested lists
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
print('brightcolors:', brightcolors)
brightcolors.append(hot)
print('brightcolors:', brightcolors)
hot.append('pink')
print('brightcolors:', brightcolors)

print(hot + warm)


# Iterations over mutated lists is wrong
def remove_dups(L1, L2):
    '''
    :param L1: list
    :param L2: list
    '''
    for e in L1:
        if e in L2:
            L1.remove(e)


'''
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
'''


# Iterations over copied lists
def remove_dups(L1, L2):
    '''
    :param L1: list
    :param L2: list
    '''
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
