#!/usr/local/bin/python3

# Euler Project
# Problem 18: https://projecteuler.net/problem=18

# Author: Yibo Weng
# Date: 23/03/2019

# Comments: Traversing the one dimensional triangle was probably the hard bit

def find_max_sum(nums):
    n = 1
    sum = [0] * len(nums)
    next_row_ends = 0

    for idx, val in enumerate(nums):
        sum[idx] += val
        if idx + n < len(nums):
            if sum[idx] >= sum[idx + n]: sum[idx + n] = sum[idx]
            if sum[idx] >= sum[idx + n + 1]: sum[idx + n + 1] = sum[idx]
            if idx == next_row_ends:
                n += 1
                next_row_ends = idx + n

    print(max(sum[(len(nums) - n) : -1]))



if __name__ == "__main__":
    nums1 = [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]

    nums2 = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10,
             20, 4, 82, 47, 65, 19, 1, 23, 75, 3,
             34, 88, 2, 77, 73, 7, 63, 67, 99, 65,
             4, 28, 6, 16, 70, 92, 41, 41, 26, 56,
             83, 40, 80, 70, 33, 41, 48, 72, 33, 47,
             32, 37, 16, 94, 29, 53, 71, 44, 65, 25,
             43, 91, 52, 97, 51, 14, 70, 11, 33, 28,
             77, 73, 17, 78, 39, 68, 17, 57, 91, 71,
             52, 38, 17, 14, 91, 43, 58, 50, 27, 29,
             48, 63, 66, 4, 68, 89, 53, 67, 30, 73,
             16, 69, 87, 40, 31, 4, 62, 98, 27, 23,
             9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

    f = open('p067_triangle.txt', 'r')
    nums3 = f.read()
    nums3 = nums3.replace('\n', ' ').split(' ')
    nums3 = [int(i) for i in nums3 if i != '']

    print(find_max_sum(nums3))
