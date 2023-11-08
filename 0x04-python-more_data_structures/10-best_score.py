#!/usr/bin/python3
def best_score(a_dictionary):
    count = 0
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > count:
            count = value
            word = key
    return word
