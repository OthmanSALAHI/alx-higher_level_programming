#!/usr/bin/python3
"""the class Rectangle"""


class Rectangle:
    """init the Rectangle."""
    def __init__(self, width=0, height=0):
        """the initial of rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """instance private width of rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        """give value to width."""
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val < 0:
            raise ValueError('width must be >= 0')
        self.__width = val

    @property
    def height(self):
        """instance private height of rectangle."""
        return self.__height

    @width.setter
    def height(self, val):
        """give value to height."""
        if type(val) is not int:
            raise TypeError('height must be an integer')
        elif val < 0:
            raise ValueError('height must be >= 0')
        self.__height = val
