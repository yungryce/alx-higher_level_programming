#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        try:
            print("Inside result: {: f}".format(result))
        except (TypeError, ValueError):
            print("Inside result: {}".format(result))
    return result
