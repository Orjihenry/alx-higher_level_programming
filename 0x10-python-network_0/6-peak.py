#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    	Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    elem = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        elem = elem // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if elem // 2 == 0:
                elem = 2
            mid = mid + elem // 2
        elif elem > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if elem // 2 == 0:
                elem = 2
            mid = mid - elem // 2
        else:
            return list_of_integers[mid]
