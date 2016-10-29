# -*- coding: utf-8 -*-
"""
Created on 29/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):
    def say(self, stuff):
        # Initially     return self.name + ' says: ' + self.lecture(stuff)
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)


class ArrogantProfessor(Professor):
    def say(self, stuff):
        # First problem     return Lecturer.say(self, 'It is obvious that ' + Person.say(self, stuff))
        return Person.say(self, 'It is obvious that ') + Lecturer.lecture(self, stuff)

    def lecture(self, stuff):
        # First problem     return 'It is obvious that ' + Person.say(self, stuff)
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

print(pe.say('the sky is blue'))
print(ae.say('the sky is blue'))
