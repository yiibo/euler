#!/usr/local/bin/python2
import math

def special_pythagoras(number):
    """ Returns a set of natural pythagorean numbers
    """
    a = 1
    while 4 * a < number:
        for b in range(a,number - 2 * a):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == number:
                return a,b,c
        a+=1

    return 0,0,0

def pythagoras_product(a,b,c):
    return a * b * c

if __name__ == "__main__":
    print pythagoras_product(*special_pythagoras(1000))
