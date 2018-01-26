#!/usr/local/bin/python2
# Problem 10 of Project Euler
import time


def isPrime(n):
    for i in xrange(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def mark(s,p,n):
    for i in xrange(2*p,n,p):
        s[i] = False

def sum_primes_sieve(n):
    """ Sieve of Erasthothenes implementation
        How this works is that it creates an array of length n, with boolean True
        Starting from the smallest prime number 2, all multiples of the prime number in the array are marked as False. It then moves up the array to the next True variable (which is a prime number) and makes all multiples of that True. This happens until we reach the end of the array.
    """
    sieve = [True] * n
    for i in xrange(2,int(n ** 0.5)+1,1):
        if sieve[i]: mark(sieve,i,n)

    return sum(i for i in xrange(2, n) if sieve[i])

def main():
    sum = 2
    for i in xrange(3,int(2e6),2):
        if isPrime(i):
            sum += i

    print sum

if __name__ == "__main__":
    start_time = time.time()
    print sum_primes_sieve(int(2e6))
    print "--- %s seconds ---" % (time.time() - start_time)
