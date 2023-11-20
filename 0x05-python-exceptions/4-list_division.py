#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lst = []
    for idx in range(list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            lst.append(result)
    return lst
