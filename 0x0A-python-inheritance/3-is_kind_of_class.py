#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    obj: object to check if an instance of a class
    a_class: class to be checked
    """
    return isinstance(obj, a_class)
