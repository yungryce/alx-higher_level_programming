#!/usr/bin/python3
""" Low memory cost """


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ['first_name']
