#!/usr/bin/python3
'''
    for ones in range(10):
if char_code != char_cude and char_cude > char_code:
(ones start has to be greater than tens
'''
for tens in range(10):
    for ones in range(tens + 1, 10):
        if tens == 8 and ones == 9:
            print("{}{}".format(tens, ones))
        else:
            print("{}{}".format(tens, ones), end=', ')
