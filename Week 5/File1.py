# -*- coding: utf-8 -*-
"""
Created on 08/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# Every class inherits from object
class Coordinate(object):
    # Attributes can be here
    def __init__(self, x, y):
        # Or here with the constructor
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def distance(self, other):
        """
        :param other: an instance of Coordinate
        :return: float distance between self and other
        """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'


'''
methods to override
__add__(self, other)    self + other
__sub__(self, other)    self - other
__eq__(self, other)     self == other
__lt__(self, other)     self < other
__len__(self)           len(self)
__str__(self)           print(self)
'''
c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.distance(origin))

print(Coordinate.distance(c, origin))

print(c)

print(isinstance(c, Coordinate))

print(origin - c)


class fraction(object):
    def __init__(self, number, denom):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + ' / ' + str(self.denom)

    def getNumber(self):
        return self.number

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumber() \
                   + other.getNumber() * self.getDenom()
        denomNew = other.getDenom * self.getDenom()
        return fraction(numerNew, denomNew)

    def __sub__(self, other):
        numberNew = other.getDenom() * self.getNumber() \
                    - other.getNumber() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numberNew, denomNew)

    def convert(self):
        return self.getNumber() / self.getDenom()


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        ans = intSet()
        for e in self.vals:
            if self.member(e) and other.member(e):
                ans.insert(e)
        return ans

    def __len__(self):
        return len(self.vals)
