#!/usr/bin/python3
"""function add two integers."""


def add_integer(a, b=98):
        """  adds two numbers.
    Args:
        a: first number.
        b: second number.
    Returns: the result  """


    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    """return the addition of a and b."""
    a = int(a)
    b = int(b)
    return (a + b)
