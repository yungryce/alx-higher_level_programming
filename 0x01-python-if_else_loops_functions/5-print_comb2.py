#!/usr/bin/python3
for char_code in range(0, 100):
    if char_code < 99:
        print("{:02}".format(char_code), end=', ')
    else:
        print("{}".format(char_code))
