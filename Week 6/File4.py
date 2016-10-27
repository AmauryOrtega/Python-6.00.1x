# -*- coding: utf-8 -*-
"""
Created on 26/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""


# Linear search on unsorted list
def linear_search(l, e):
    # O(len(l)) * O(1)
    # = O(n)
    found = False
    for i in range(len(l)):
        if e == l[i]:
            found = True
    return found


# Linear search on sorted list
def search(l, e):
    # O(len(l)) * O(1)
    # = O(n)
    for i in range(len(l)):
        if l[i] == e:
            return True
        if l[i] > e:
            return False
    return False


# Bisection search
"""
The numbers of elements to be cover in the list is reduced in half each time
n/2     n/4     n/8     n/2^x
so 1=n/2^x
so x=log(n)

O(log n) when n=len(list)
"""


def bisect_search(l, e):
    """O(n log(n))"""
    if l == []:
        # O(1)
        return False
    elif len(l) == 1:
        # O(1)
        return l[0] == e
    else:
        # O(1)
        half = len(l) // 2
        if l[half] > e:
            # not constant because of the copying of the list which adds more complexity each recursive call
            return bisect_search(l[:half], e)
        else:

            return bisect_search(l[half:], e)


def bisect_search2(l, e):
    """O(log(n)) because it uses integers for the high and low limit instead of making a copy"""

    def bisect_search_helper(l, e, low, high):
        if high == low:  # Only one element in the list
            return l[low] == e
        mid = (low + high) // 2
        if l[mid] == e:
            return True
        elif l[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(l, e, low, mid - 1)
        else:
            return bisect_search_helper(l, e, mid + 1, high)

    if len(l) == 0:
        return False
    else:
        return bisect_search_helper(l, e, 0, len(l) - 1)
