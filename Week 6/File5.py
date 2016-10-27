# -*- coding: utf-8 -*-
"""
Created on 29/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

# Sort
import random


# __Monkey Sort__
def bogo_sort(l):
    """
    Randomly insert elements into a list
    check if they're sorted
        if yes
            stop
        if not
            go back to the beginning
    """

    # Best case: O(len(l))
    # Worst case: O(?)
    def is_sorted(l):
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    while not is_sorted(l):
        random.shuffle(l)


# __Bubble sort__
def bubble_sort(l):
    # O(n^2)
    swap = False
    while not swap:  # O(len(l))
        swap = True
        for j in range(1, len(l)):  # O(len(l))
            if l[j - 1] > l[j]:
                swap = False
                temp = l[j]
                l[j] = l[j - 1]
                l[j - 1] = temp


# __Selection sort__
def selection_sort(l):
    """
    1) Extract min element -> swap it with element in index 0
    2) In remaining sublist, extract min element -> swap it with element in index 1
    3) Keep the left portion sorted
    """
    # O(n^2)
    suffixSt = 0
    while suffixSt != len(l):  # O(len(l))
        for i in range(suffixSt, len(l)):  # O(len(l))
            if l[i] < l[suffixSt]:
                l[suffixSt], l[i] = l[i], l[suffixSt]
        suffixSt += 1


# __Merge Sort__
def merge_sort(l):
    """
    1) If list is of length 0 or 1, is sorted
    2) If list have more than one element, split into two and sort them
    3) Merge sorted sublists
        Look at first element of each, move smaller to the end of the result
        When one list is empty, just copy the rest of the other list
    """

    # O(n Log(n))
    def merge(left, right):
        """
        O(len(left)) + O(len(right))    copied elements
        O(len(longer list))             comparisons
        """
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < left(right):
            result.append(right[j])
            j += 1
        return result

    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle])
        right = merge_sort(l[middle:])
        return merge(left, right)
