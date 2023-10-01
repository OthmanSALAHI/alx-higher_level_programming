#!/usr/bin/python3
"""
    0-add_integer function
"""


def add_integer(a, b=98):
    """  adds two numbers.
    Args:
        a: first number.
        b: second number.
    Returns: the result  """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
