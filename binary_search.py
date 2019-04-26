#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 07:41:00 2019

@author: yannik
"""

# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    while left<=right:
        median = (left+right)//2
        if median>=len(a):
            break
        if a[median] == x:
            return median
        elif a[median] > x:
            right = median-1
        elif a[median] < x:
            left = median+1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')