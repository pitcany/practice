#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:57:22 2019

@author: yannik
"""

# Uses python3
import sys

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range((n+1)%60):
        previous, current = current, (previous + current)%10

    return (current-1)%10

def fibonacci_partial_sum(from_, to):
    if from_ > 0:
        return (fibonacci_sum(to)-fibonacci_sum(from_-1))%10
    elif from_ == 0:
        return fibonacci_sum(to)

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))