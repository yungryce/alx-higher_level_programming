#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
def print_reversed_list_integer(my_list=[]):
    for lst in range(len(my_list), 0, -1):
        print("{}".format(lst))
print_reversed_list_integer(my_list)
