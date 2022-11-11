#!/usr/local/bin/python3

# Euler Project
# Problem 23: https://projecteuler.net/problem=23

# Author: Yibo Weng
# Date: 26/06/2022

# Comments: Summing value of all characters mapped to their place in alphabet
import string
import time

def find_divisors(n, divisors = [1]):
    return divisors + [i for i in range(divisors[-1] + 1, int(n/2) + 1) if n % i == 0]

def find_divisor_sum(n):
    return sum(find_divisors(n,divisors))

def is_abundant(n):
    if sum(find_divisors(n)) > n:
        return True
    return False

def find_abundant_numbers(upper):
    return [i for i in range(1,upper) if is_abundant(i)]

if __name__ == "__main__":

    # DEBUG
    n = 28123

    foo = find_abundant_numbers(n)

    bar = [num + j for idx,num in enumerate(foo) for j in foo[idx:-1]]

    foo1 = [i for i in range(1,n) if i not in bar]

    print(sum(list(set(foo1))))