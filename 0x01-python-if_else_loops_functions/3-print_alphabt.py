#!/usr/bin/python
for char_code in range(ord('a'), ord('z') + 1):
    if char_code == ord('q') or char_code == ord('e'):
        continue
    print(chr(char_code), end='')
