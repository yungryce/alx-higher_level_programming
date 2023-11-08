#!/usr/bin/python3
def roman_to_int(roman_string):
    str_list = list(roman_string)
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    new_value = 0
    prev_value = 0

    for item in reversed(roman_string):
        if item not in roman:
            return None

        value = roman[item]

        if value < prev_value:
            new_value -= value
        else:
            new_value += value

        prev_value = value
    return new_value
