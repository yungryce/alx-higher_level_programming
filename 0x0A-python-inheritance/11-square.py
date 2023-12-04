#!/usr/bin/python3
"""
class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """extends a Rectangle class with a subclass Square"""

    def __init__(self, size):
        """
        size: size of a aquare
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """informal string representation of the rectangle"""
        return f"[Square] {self.__size}/{self.__size}"
