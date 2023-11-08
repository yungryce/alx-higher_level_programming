#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for keys, item in a_dictionary.items():
        if item == value:
            to_del.append(keys)
    for key in to_del:
        del a_dictionary[key]
    return a_dictionary
