#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:54:40 2019

@author: yannik
"""

# python3
import sys

def optimal_summands(n):
    summands = []
    sum = n
    i = 0
    while (sum > 0):
        if 2*(i+1) < sum:
            i+=1
            summands.append(i)
            sum-=i
        else:
            summands.append(sum)
            sum=0
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')