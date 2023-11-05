#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = len(sentence),
    for i in sentence:
        if i == sentence[0]:
            new_tuple += (i,)
    return new_tuple
