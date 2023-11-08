#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
# result = list(map(lambda x: x**2, col))
# new_matrix.append(result)
# square = [[x**2 for x in row] for row in matrix]
    square = [x**2 for row in matrix for x in row]
    return square
