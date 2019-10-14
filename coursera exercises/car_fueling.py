#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:24:55 2019

@author: yannik
"""

# python3
import sys

def compute_min_refills(distance, tank, stops):
    numRefills, currentRefill = 0,0
    x = [0]+stops+[distance]
    n = len(stops)
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and x[currentRefill + 1]-x[lastRefill] <= tank):
            currentRefill += 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefills += 1
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))