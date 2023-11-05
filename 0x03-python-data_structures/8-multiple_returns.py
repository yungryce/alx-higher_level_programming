#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = len(sentence),
    if not sentence:
        new_tuple += (None,)
    else:
        new_tuple += (sentence[0],)
    return new_tuple
