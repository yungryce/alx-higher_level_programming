#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    obj: object to check if an instance of a class
    a_class: class to be checked
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
