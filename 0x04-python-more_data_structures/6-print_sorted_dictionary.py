#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = list(a_dictionary)
    lst.sort()
    for key in lst:
        print(f"{key} : {a_dictionary[key]}")

