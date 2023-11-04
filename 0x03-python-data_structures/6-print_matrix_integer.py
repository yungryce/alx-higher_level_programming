#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in row:
            if idx != row[-1]:
                print("{}".format(idx), end=' ')
            else:
                print("{}".format(idx), end='')
            #print("{:d}".format(idx), end=" " if idx != row[-1] else "")
        print()
