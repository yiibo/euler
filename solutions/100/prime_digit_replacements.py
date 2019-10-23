from numpy import inf
from itertools import ifilter, count, product

import time
import numpy as np

nums = range(0,10)

def is_prime(n):
    for i in xrange(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def count_prime(arr):
    return sum(x for x in map(is_prime,arr))

def int_to_list(num):
    return [int(x) for x in str(num)]

def list_to_int(lst):
    return int(''.join([str(x) for x in lst]))

def lists_to_int(lsts):
    return [int(''.join([str(y) for y in x])) for x in lsts]

def replace_positions(marked_array):
    return [[i if j not in nums else j for j in marked_array] for i in nums]


def generate_first_family(start_digits,end_digits,n,marker='*'):
    for i in range(start_digits,end_digits):
        print "Generating products: %d" % i
        product = list(itertools.product(nums + [marker], repeat=i))

        print "Validating and sorting"
        is_valid = list(filter(lambda x: marker in x and x[-1] != marker and x[-1] % 2 == 1 and x[0] != 0, product))
        is_valid.sort()

        for j in is_valid:
            if count_prime(lists_to_int(replace_positions(j))) == n:
                return i, j

    return 0, []

if __name__ == "__main__":
    start_time = time.time()
    print generate_first_family(2,7,8)
    print "--- %s seconds ---" % (time.time() - start_time)
