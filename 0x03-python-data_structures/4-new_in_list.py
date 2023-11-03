#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = []
    for lst in my_list:
        if lst is not my_list[idx]:
            new_list.append(lst)
        else:
            new_list.append(element)
    return new_list
"""
    for i in range(len(my_list)):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])
"""
