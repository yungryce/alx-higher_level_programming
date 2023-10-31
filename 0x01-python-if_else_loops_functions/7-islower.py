#!usr/bin/python3
def islower(c):
    for char_lower in range(ord('a'), ord('z') + 1):
        if ord(c) == char_lower:
            return True
    return False
