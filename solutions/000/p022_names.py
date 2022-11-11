#!/usr/local/bin/python3

# Euler Project
# Problem 22: https://projecteuler.net/problem=22

# Author: Yibo Weng
# Date: 25/06/2022

# Comments: Summing value of all characters mapped to their place in alphabet
import string

def calc_char_val(s):
    # DEBUG
    # for i in s:
    #     print("%s : %i" % (i, string.ascii_uppercase.index(i) + 1))

    # print(sum([string.ascii_uppercase.index(i) + 1 for i in s]))
    # print("\n")
    return(sum([string.ascii_uppercase.index(i) + 1 for i in s]))

if __name__ == "__main__":

    f = open('./solutions/000/p022_names.txt', 'r')
    names = f.read()
    names = names.replace('"','').split(',')
    names.sort()

    # DEBUG
    # print([names[-1]])
    # names = ["MARY","PATRICIA","LINDA","BARBARA","ELIZABETH"]
    summed_names = [(i+1) * calc_char_val(n) for i,n in enumerate(names)]

    print(sum(summed_names))