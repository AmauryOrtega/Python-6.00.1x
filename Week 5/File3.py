# -*- coding: utf-8 -*-
"""
Created on 10/10/2016

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


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        super().__init__(age)  # Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        """Returns object of the same type as this class"""
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent2.rid and self.parent2 == other.parent1.rid
        return parents_same or parents_opposite
        # Or
        # return self.rid == other.rid


peter = Rabbit(2)
peter.set_name('Peter')

hospy = Rabbit(3)
hospy.set_name('Hospy')

cotton = Rabbit(1, peter, hospy)
cotton.set_name('Cottontail')
print(cotton)
print(cotton.get_parent1())
print(cotton + hospy)
print((cotton + hospy).get_parent1())
print((cotton + hospy).get_parent2())
