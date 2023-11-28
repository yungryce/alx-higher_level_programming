#!/usr/bin/python3
""" function that prints a text with 2 new lines after
each of these characters: ., ? and : """


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each ".", "?", or ":"
    Args:
        text (str): The string to be printed
    Raises:
        TypeError: If text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    in_sentence = False
    for char in text:
        if char.isalpha():
            in_sentence = True

        if in_sentence:
            print(char, end='')

        if char in ['.', '?', ':']:
            in_sentence = False
            print()
            print()
