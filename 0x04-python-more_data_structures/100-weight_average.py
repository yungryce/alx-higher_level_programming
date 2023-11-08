#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numer = 0
    denom = 0
    for item in my_list:
        numer += item[0] * item[1]
        denom += item[1]
    return numer / denom
