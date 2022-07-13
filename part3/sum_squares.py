#!/usr/bin/env python

import numpy as np
from functools import reduce

def my_sum_of_squares(l):
    sumsq=0
    for i in l:
        sumsq += i*i
    return sumsq

def sum_of_squares(l):
    good_values = [int(x) for x in l if x[0] != '#']
    squares = [int(x) * int(x) for x in good_values]
    # how does this know to sum more than one item
    # when only given a+b
    sumsq = reduce(lambda a, b: a + b, squares)
    return sumsq

#print(sum_of_squares([0]))
#print(sum_of_squares([1]))
#print(sum_of_squares([1, 2, 3]))
#print(sum_of_squares([-1]))
#print(sum_of_squares([-1, -2, -3]))
print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))



print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))

