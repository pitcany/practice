#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 02:43:07 2019

@author: yannik
"""

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    
    for i in range(n - 1):
        previous, current = current, (previous+current) % m
        if previous == 0 and current == 1:
            pisano_period = i+1
            return get_fibonacci_huge(n % pisano_period, m)

    return current

if __name__ == '__main__':
    n,m = map(int, input().split())
    print(get_fibonacci_huge(n, m))