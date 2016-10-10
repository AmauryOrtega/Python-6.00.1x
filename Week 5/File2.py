# -*- coding: utf-8 -*-
"""
Created on 09/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


class Animal(object):
    """A class that defines an animal"""

    def __init__(self, age):
        """Takes an age and builds and age and a name"""
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return 'animal:' + str(self.name) + ':' + str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ':' + str(self.age)


jelly = Cat(1)
jelly.set_name('JellyBelly')
print(jelly)
print(Animal.__str__(jelly))


class Rabbit(Animal):
    def speak(self):
        print('meep')

    def __str__(self):
        return 'rabbit:' + str(self.name) + ':' + str(self.age)
