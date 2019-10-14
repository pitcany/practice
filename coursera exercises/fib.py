#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 02:00:56 2019

@author: yannik
"""

def calc_fib(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))