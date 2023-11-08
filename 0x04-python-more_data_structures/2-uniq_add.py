#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
# unique_set = {x for x in my_list}
    for item in {x for x in my_list}:
        count += item
    return count
