#!/usr/bin/python3
"""the class Rectangle"""


class Rectangle:
    """init the Rectangle.
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """the initial of rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """instance private width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """give value to width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """instance private height of rectangle."""
        return self.__height

    @width.setter
    def height(self, value):
        """give value to height."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
