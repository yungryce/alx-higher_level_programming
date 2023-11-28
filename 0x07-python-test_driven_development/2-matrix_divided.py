#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide each element in the matrix by the given divisor.

    Args:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - list of lists: The resulting matrix after division.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
        if not all(type(element) in (int, float) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    square = [[round(x / div, 2) for x in row] for row in matrix]
    return square
