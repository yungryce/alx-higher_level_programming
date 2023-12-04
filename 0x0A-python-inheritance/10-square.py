#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py):"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of Rectangle, a subclass of BaseGeometry"""

    def __init__(self, size):
        """
        size: size of a square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of a square"""
        return self.__size ** 2
