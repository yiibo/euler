#!/usr/local/bin/python2
import math

def pythagoras(number):
    """ Returns a set of natural pythagorean numbers
    """
    for a in range(1,number):
        for b in range(a,number):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == number:
                return a,b,c

    return 0,0,0

def pythagoras_product(a,b,c):
    return a * b * c

if __name__ == "__main__":
    print pythagoras_product(*pythagoras(1000))
