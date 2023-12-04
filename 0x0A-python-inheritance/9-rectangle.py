#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""


class Rectangle(BaseGeometry):
    """sub class of BaseGeometry"""

    def __init__(self, width, height):
        """
        width: width of a rectangle
        height: height of a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
