#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        Initialises a rectangle class
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the width of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 and self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += '#' * self.__width + '\n'
        return result.rstrip('\n')

    def __repr__(self):
        """Returns a string representation of the object for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"
