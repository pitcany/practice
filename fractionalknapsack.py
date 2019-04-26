#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:07:28 2019

@author: yannik
"""

# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    n = len(weights) # or len(values)
    unit_values = enumerate([values[i]/weights[i] for i in range(n)])
    unit_values = [j for j in unit_values]
    unit_values.sort(key=lambda x:x[1])
    while (capacity > 0 and unit_values):
        # check if all of item can be taken...otherwise take fractional amount
        index,unit_value=unit_values.pop()
        wt = weights[index]
        val = values[index]
        if wt < capacity:
            capacity -= wt
            value += val
        else:
            value += capacity*unit_value
            capacity = 0
    return value

#get_optimal_value(50,[20,50,30],[60,100,120])

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))