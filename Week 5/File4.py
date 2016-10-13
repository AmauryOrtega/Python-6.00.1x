# -*- coding: utf-8 -*-
"""
Created on 12/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

import datetime


class Person(object):
    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthDate(self, month, day, year):
        """Set self's birthday to birthDate"""
        self.birthday = datetime.date(year=year, month=month, day=day)  # datetime.date(year, month, day)

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """
        Returns True if self's name is lexicographically
        less than other's name, and False otherwise
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name


class MITPerson(Person):
    nextID = 0

    def __init__(self, name):
        super().__init__(name)
        self.ID = MITPerson.nextID
        MITPerson.nextID += 1

    def getID(self):
        return self.ID

    def __lt__(self, other):
        return self.getID() < other.getID()

    def speak(self, utterance):
        # return self.getLastName() + ' says: ' + utterance
        return self.name + ' says: ' + utterance


class Student(MITPerson):
    pass


class UG(Student):  # Undergraduated student

    def __init__(self, name, classYear):
        super().__init__(name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        # return super().speak(" Dude, " + utterance)
        return super().speak(" Yo Bro, " + utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


class Professor(MITPerson):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def speak(self, utterance):
        return super().speak('In course ' + self.department + ' we say ' + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)


# Person's test
p1 = Person('Mark Zuckerberg')
p1.setBirthDate(5, 14, 84)
p2 = Person('Drew Hotson')
p2.setBirthDate(3, 4, 83)
p3 = Person('Bill Gates')
p3.setBirthDate(10, 28, 55)
p4 = Person('Andre Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)
personList.sort()  # Uses the < operator
print()
for e in personList:
    print(e)

# MITPerson's test
m3 = MITPerson('Mark zuckergerb')
m3.setBirthDate(5, 14, 84)
m2 = MITPerson('Drew Huston')
Person.setBirthDate(m2, 3, 4, 83)
m1 = MITPerson('Bill Gates')
Person.setBirthDate(m1, 10, 28, 55)
MITPersonList = [m1, m2, m3]

for e in MITPersonList:
    print(e)
MITPersonList.sort()  # Uses the < operator
print()
for e in MITPersonList:
    print(e)

# Other testes between MITPerson and Person
p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

p1 < p2  # True because of ID
# p1 < p4  # AttributeError because p4 doesn't have an ID -> p1.__lt__(p4) MITPerson's implementation
p4 < p1  # False Because uses the Person __lt__ implementation -> p4.__lt__(p1) Person's implementation

# UG and Grad tests
s1 = UG('Matt Damon', 2017)
s2 = UG('Ben affleck', 2017)
s3 = UG('Lin Manuel Miranda', 2018)
s4 = Grad('Leonardo di Caprio')
s5 = TransferStudent('Robert deNiro')
studentList = [s1, s2, s3, s4, s5]
print(s1)
print(s1.getClass())
print(s1.speak('where is the quiz?'))
print(s2.speak('I have no clue!'))

# Professor test
faculty = Professor('Doctor Arrogant', 'six')
