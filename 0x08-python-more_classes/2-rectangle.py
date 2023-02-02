#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """
        A class rectangle defines a rectangle
             Attributes:
                width (int): width of the rectangle
                height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Inatialize the instance of the classe(the constructor)
            args:
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
            getter function for the private attribute width
            returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for the private attribute width
            returns: width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for private attriburte height
            return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the private attribute height
            returns: height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            public method area to caluclate the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            public method perimeter to clauculate the perimeter of a rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
