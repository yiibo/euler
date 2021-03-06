from itertools import product
from mathfun import prime.py

import numpy as np

nums       = '0123456789'

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
last_prime = prime_list[-1]

def prime_list_add(n):
''' Generates prime list up to n
    '''
    primes = []

    for i in xrange(3,int(n**0.5) + 1,2):
        if is_prime(i): primes.append(i)

    return primes

def is_prime(n):
    for i in xrange(3,int(n**0.5) + 1,2):       # Sieve of erasthothenes: convergence up to sqrt(n)
        if n % i == 0:                          # Returns false if any number has a divisor
            return False
    return True

def _isprime(n):
    ''' Raw check to see if n is prime. Assumes that prime_list is already populated '''
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n: break             # ... up to sqrt(n)
        if not n % prime:
            isprime = 0
            break
    if isprime: prime_dict[n] = 1               # Maintain a dictionary for fast lookup
    return isprime

def _update(x):
    global last_prime
    while last_prime < x - 1:
        last_prime += 2                         # Check the next number
        if _isprime(last_prime):
            prime_list.append(last_prime)       # Maintain a list for sequential access

def isrecur(num,idx,count):
    if idx == len(str(num):
        return False
    


def prime_family(8):
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
    print prime_family(2,7,8)
    print "--- %s seconds ---" % (time.time() - start_time)
