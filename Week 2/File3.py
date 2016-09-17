# -*- coding: utf-8 -*-
"""
Created on 17/06/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)


def printName(firstName, lastName, reverse=False):  # Default value for reverse
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)


printName('Amaury', 'Ortega', False)
printName('Amaury', 'Ortega', reverse=False)
printName('Amaury', lastName='Ortega', reverse=False)
printName(lastName='Ortega', firstName='Amaury', reverse=False)  # The order doesn't matter
