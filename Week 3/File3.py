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
