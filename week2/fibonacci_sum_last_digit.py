#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 04:30:25 2019

@author: yannik
"""

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    
    n = (n+2)%60

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10

    return (current-1)%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))