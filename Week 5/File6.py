# -*- coding: utf-8 -*-
"""
Created on 13/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


def genTest():
    yield 1
    yield 2


foo = genTest()
print(foo.__next__())
print(foo.__next__())
# print(foo.__next__()) StopIteration Exception

print()

for n in genTest():
    print(n)


def genFib():
    fibn_1 = 1  # fib(n-1)
    fibn_2 = 0  # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next


fib = genFib()  # Generator object
print(fib)
print(fib.__next__())

"""
Infinite list
for n in fib:
    print(n)
"""

from File4 import *


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Creates an empty grade book"""
        self.students = []  # list of Students objects
        self.grades = {}  # maps idNum -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """
        Assumes: student is of type Student
        Add student to the grade book
        """
        if student in self.students:
            raise ValueError('Duplicated student')
        self.students.append(student)
        self.grades[student.getID()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """
        Assumes: grade is a float
        Add grade to the list of grades for student
        """
        try:
            self.grades[student.getID()].append(grade)
        except KeyError:
            raise ValueError('Student is not in grade book')

    def getGrades(self, student):
        """
        Returns a copy of the list of grades for student
        """
        try:
            return self.grades[student.getID()][:]
        except KeyError:
            raise ValueError('Student is not in grade book')

    def allStudents(self):
        """
        Returns a copy of the list of students in the grade book
        """
        """
        Inefficient way
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        """
        # Efficient way
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s


def gradeReport(course):
    """Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)
print()

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)
print('-' * 5, 'Grade Report', '-' * 5)
print(gradeReport(six00))
print()

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 70)
print()

print('-' * 5, "Students' list", '-' * 5)
for s in six00.allStudents():
    print(s)


def genPrimes():
    primes = []
    num = 2
    while True:
        band = True
        for n in primes:
            if (num % n) == 0:
                band = False
        if band is True:
            primes.append(num)
            yield num
        num += 1
