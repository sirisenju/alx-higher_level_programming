#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """
        class rectangle that defines a rectangle
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Initializes the instance of the class(The constructor)
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
        Rectangle.number_of_instances += 1

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
            setter function for private attribute width
            args:
                returns: value(new width)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for the private attribute height
            returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for the private attribute height
            args:
                returns: value(new height)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public method to caluculate area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        public method that calculate the perimeter of a rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns string rep of rectangle
        """
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        rectangle += str(self.print_symbol) * self.__width

        return rectangle

    def __repr__(self):
        """
        returns a string representation of the rectangle to be
        able to recreate a new instance
        """
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """
            properly deletes the instance of a class
        """
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
