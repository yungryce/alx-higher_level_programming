#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    for list_args in sys.argv[1:]:
        count += int(list_args)
    print(count)
