#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """
        a class rectangle that defines a rectangle
            Attributes:
                width (int): width of the rectangle
                height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Initializes the inistance(the constructor)
                Args:
                    width (int): width of the rectangle
                    height (int): height of the rectangle
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
            getter function for private attribute width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for the private attribute width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the private attribute height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
