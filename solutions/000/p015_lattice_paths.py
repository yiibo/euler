#!/usr/local/bin/python3

# Euler Project
# Problem 15: https://projecteuler.net/problem=15

# Author: Yibo Weng
# Date: 12/03/2019

# Comment: Code is kinda bad and unnecessary as this is more of an exercise in OOP
#           than anything else

# Bugs:
# heaps
import itertools
import time
import math

class LatticePathSolver:

    def __init__(self, length):
        self.length = length
        self.path_count = 0    # Used for the path traversal

    # Loop implementation
    def nCr(self):
        f = math.factorial
        self.path_count = f(self.length * 2) / f(self.length) / f(self.length)

    # Solves by permuting lattice
    def permute(self):
        p = list(itertools.permutations('RD' * self.length, self.length * 2))
        p = list(dict.fromkeys(p))

        self.path_count = len([item for item in p if item.count('R') == self.length])

    # Solves by traversing lattice and solving recursively
    def traverse(self, cur_path = []):
        cur_path_len = len(cur_path)

        if cur_path_len < self.length * 2:
            if cur_path.count("r") < self.length:
                self.traverse(cur_path.__add__(["r"]))

            if cur_path.count("d") < self.length:
                self.traverse(cur_path.__add__(["d"]))
        else:
            self.path_count += 1

    def reset():
        self.path_count = 0

# def traverse(length, path_count = 0, cur_path = []):
#     cur_path_len = len(cur_path)
#
#     if cur_path_len < length * 2:
#         if cur_path.count("r") < length:
#             path_count += traverse(length, 0, cur_path.__add__(["r"]))
#
#         if cur_path.count("d") < length:
#             path_count += traverse(length, 0, cur_path.__add__(["d"]))
#
#     elif cur_path_len == length * 2:
#         return 1
#
#     return path_count


if __name__ == "__main__":
    grid_len = 20

    ### 1: Calculate run through recursion (does not solve quickly enough)
    # lattice = LatticePathSolver(grid_len)
    # lattice.traverse()
    # print("Traversal count:",lattice.path_count)

    ### 2: Calculate run through permutation (does not solve quickly enough)
    # lattice = LatticePathSolver(grid_len)
    #
    # start = time.time()
    # lattice.permute()
    # end = time.time()
    # print("Count:",lattice.path_count)
    # print("Exec Time:",end - start,"s")

    ### 3: nCr calc
    lattice = LatticePathSolver(grid_len)
    start = time.time()
    lattice.nCr()
    end = time.time()
    print("Count:",lattice.path_count)
    print("Exec Time:",end - start,"s")

    # print(traverse(grid_len))
    # lattice.path_count += None
