#!/usr/bin/python3
"""the class"""


class Square:
    """the entry of class"""

    def __init__(self, size=0):
        """init the class

        Args:
            size (int): the size of Square
        """
        try:
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
