#!/usr/bin/python3
def find_peak(list_of_integers):
    """function finds the peak int"""
    list_of_integers.sort()
    return list_of_integers[-1]
