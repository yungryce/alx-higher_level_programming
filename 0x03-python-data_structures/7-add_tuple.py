#!/usr/bin/python3
tuple_a = (1, 89)
tuple_b = (88, 11)

def add_tuple(tuple_a=(), tuple_b=()):

    pairs = (tuple_a, tuple_b)
    sum_pairs = ()

    for i, j in pairs:
        sum_pairs += (i + j,)

    return sum_pairs

new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
