#!/usr/bin/python
for char_code in range(0, 100):
    if char_code < 99:
        print(f"{char_code:02}", end=', ')
    else:
        print(f"{char_code}")
