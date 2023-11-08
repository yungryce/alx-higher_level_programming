#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    '''
    new_list = [replace if item == search else item for item in my_list]
    return new_list
