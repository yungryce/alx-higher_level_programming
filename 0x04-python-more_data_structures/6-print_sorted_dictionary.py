#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = list(a_dictionary.keys())
    lst.sort()
    for key in lst:
        print("{} : {}".format(key, a_dictionary[key]))
