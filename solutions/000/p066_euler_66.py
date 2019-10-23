#!/usr/local/bin/python3
#
# Euler Project
# Problem 66 - Diophantine Equation
# https://projecteuler.net/problem=66
#
# Author: Yibo Weng
# Date: 24/03/2019

import math
import itertools
import time
import sys

import ggplot
import pandas as pd

""" Problem Description

Consider a Diophantine quadratic Equation
    x^2 - Dy^2 = 1

Where, for example, if D = 13, then the minimum solution is:
    649^2 - 13 * 180^2 = 1

It can be assumed that there are no positive integer solutions if D is a square
numbers.

For minimal solutions in D < 8: {2, 3, 5, 6, 7}, we have:
    3^2 - 2 * 2^2 = 1
    2^2 - 3 * 1^2 = 1
    9^2 - 5 * 4^2 = 1
    5^2 - 6 * 2^2 = 1
    8^2 - 7 * 3^2 = 1

Hence, by considering solutions where D < 8, the maximum value of x is found
when D = 5, x = 9.
"""

# Finds solution for D
def diophantine(D, limit = 1e6):
    x = round(math.sqrt(D))
    if math.sqrt(D) % 1 != 0 and D >= 2:
        while x < limit:
            for y in range(x):
                print([x,y, x*x - D * y * y])
                if x * x - D * y * y == 1:
                    return [x, y]
            x += 1

    return [-1, -1]

def largest_x(D_rng):
    x_max = 0
    for d in range(D_rng):
        [x, y] = diophantine(d)
        if x > x_max:
            x_max = x
            y_max = y
            D_max = d

    return [x_max, y_max, D_max]

def load_data(d):
    s = pd.Series(d)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(diophantine(int(sys.argv[1])))
        # print(largest_x(int(sys.argv[1])))
