#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = 0
    if len(sys.argv[1:]) == 0:
        print("{:d} arguments.".format(0))
    elif len(sys.argv[2:]) == 0:
        print("{:d} argument:".format(1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    for list_args in sys.argv[1:]:
        count += 1
        print("{:d}: {}" .format(count, list_args))
