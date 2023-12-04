#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass of BaseGeometry"""

    def __init__(self, width, height):
        """
        width: width of a rectangle
        height: height of a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
