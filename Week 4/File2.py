# -*- coding: utf-8 -*-
"""
Created on 30/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# raise <ExceptionName>(<arguments>)
# raise ValueError("something is wrong")

def get_ratios(l1, l2):
    """
    Assumes: L1 and L2 are list of equal length of numbers
    Returns: a list containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(l1)):
        try:
            ratios.append(l1[index] / float(l2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))  # Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios


test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], [['bruce', 'wayne'], [10.0, 8.0, 74.0]]]
test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]], [['deadpool'], []]]


def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats


# def avg(grades):
#     return sum(grades) / len(grades)

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('No grades data')
        return 0.0


def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)


def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
