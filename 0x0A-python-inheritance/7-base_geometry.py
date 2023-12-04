#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Base class"""

    def area(self):
        """public class that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
