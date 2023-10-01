#!/usr/bin/python3
"""function add two integers."""


def add_integer(a, b=98):
    """an function that add two integers."""

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    """return the addition of a and b."""
    return (int)(a + b)
