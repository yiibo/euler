#!/usr/local/bin/python3

# Euler Project
# Problem 16: https://projecteuler.net/problem=16

# Author: Yibo Weng
# Date: 22/03/2019

# Comment: Just a bunch of type conversions. It seems that the power function
# type conversion and representing values within code is fairly lightweight
import math
import time

class PowerDigitSum:
    def __init__(self, digit, power):
        self.digit = digit
        self.power = power

    def calculatePower(self):
        self.power = math.pow(self.digit, self.power)

    def addDigits(self):
        self.result = sum([int(j) for j in str(int(self.power))])

    def printResult(self):
        try:
            print("Power Value:", self.power, "Sum of digits", self.result)
        except NameError:
            print("Variable is not defined")

    def calculateAndPrintResult(self):
        start = time.time()
        self.calculatePower()
        end = time.time()
        print(end - start)

        self.addDigits()

        self.printResult()


if __name__ == "__main__":
    p = PowerDigitSum(2,16)

    p.calculateAndPrintResult()
