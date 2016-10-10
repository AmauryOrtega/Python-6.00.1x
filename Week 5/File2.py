# -*- coding: utf-8 -*-
"""
Created on 09/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None


myAnimal = Animal(3)
