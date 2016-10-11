# -*- coding: utf-8 -*-
"""
Created on 09/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

import random


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


class Rabbit(Animal):
    def speak(self):
        print('meep')

    def __str__(self):
        return 'rabbit:' + str(self.name) + ':' + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)  # Animal.__init__(self, age)
        super().set_name(name)  # Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        return 'hello'

    def age_diff(self, other):
        # Alternate way: diff = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.get_age() > other.get_age():
            print(self.get_name(), 'is', diff, 'years older than', other.get_name())
        else:
            print(self.get_name(), 'is', -diff, 'years younger than', other.get_name())

    def __str__(self):
        return 'Person:' + str(self.get_name()) + ':' + str(self.get_age())


class Student(Person):
    def __init__(self, name, age, major=None):
        super().__init__(name, age)  # Persion.__init__(self, name, age)
        self.major = major

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print('I am watching tv')

    def __str__(self):
        return 'student:' + str(self.get_name()) + ':' + str(self.get_age()) + ':' + str(self.major)


jelly = Cat(1)
jelly.set_name('JellyBelly')
print(jelly)
print(Animal.__str__(jelly))

blob = Animal(1)
peter = Rabbit(5)

print(jelly.speak())
print(peter.speak())
# print(blob.speak()) Gives and AttributeError

eric = Person('eric', 45)
john = Person('john', 55)


# Multiple inheritance
class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        print("A.x")

    def y(self):
        print("A.y")

    def z(self):
        print("A.z")


class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3

    def y(self):
        print("B.y")

    def z(self):
        print("B.z")


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def y(self):
        print("C.y")

    def z(self):
        print("C.z")


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6

    def z(self):
        print("D.z")


obj = D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
obj.x()
obj.y()
obj.z()
