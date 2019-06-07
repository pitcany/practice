#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:29:32 2019

@author: yannik
"""

# python3
from sys import stdin

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n%60):
        previous, current = current, (previous + current) % 10

    return ((previous*current)%10)

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))