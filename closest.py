#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:10:48 2019

@author: yannik
"""

#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    return 10 ** 18

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))