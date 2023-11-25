#!/usr/bin/python3
""" function that prints a square with the character #. """


def print_square(size):
    """This function prints a square with the character #
    Args:
        size (int): This represents the length of the square
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 or (isinstance(size, float) and size < 0):
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print(size * '#')
