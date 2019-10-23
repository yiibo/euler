#!/usr/local/bin/python3

# Euler Project
# Problem 17: https://projecteuler.net/problem=17

# Author: Yibo Weng
# Date: 22/03/2019

# Did it case by case for numbers up to 1000.

singles = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
}

ten = {
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
}

tens = {
    10:"ten",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
}

powers = {
    100:"hundred",
    1000:"thousand"
}

if __name__ == "__main__":
    one_to_nine = sum([len(singles[i]) for i in range(1,10)])
    print("Sum of one to nine:", one_to_nine)

    ten_to_nineteen = sum([len(ten[i]) for i in range(10,20)])
    print("Sum of ten to nineteen:", ten_to_nineteen)

    one_to_hun = one_to_nine + ten_to_nineteen + sum([len(tens[i]) + len(singles[j]) for i in range(20,100,10) for j in range(0,10)])
    print("Sum of one to one hundred:", one_to_hun)

    one_to_thou = one_to_hun * 10 + sum([len(singles[i]) + len(powers[100]) + len("and") for i in range(1,10)]) * 100 + len(singles[1]) + len(powers[1000]) - 9 * 3
    print("Sum of one to one hundred:", one_to_thou)
