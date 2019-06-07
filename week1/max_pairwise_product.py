#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:17:21 2019

@author: yannik
"""

# python3

def max_pairwise_product(numbers):
    from collections import defaultdict
    d = defaultdict(int)
    for i in numbers:
        d[i] += 1
    num1 = max(d)
    if d[num1] > 1:
        d[num1] -= 1
    else:
        del d[num1]
    num2 = max(d)
    max_product = num1*num2
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))