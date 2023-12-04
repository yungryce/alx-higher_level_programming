#!/usr/bin/python3
"""
Function that returns True if the object is exactly an
instance of the specified class
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    obj: instance of specified classs
    a_class: class to check
    """
    return type(obj) == a_class
