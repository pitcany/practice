#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:03:44 2019

@author: yannik
"""

#Uses python3

import sys

def concat(x,y):
    return ( int(str(x)+str(y)) )

def largest_number(a):
    #write your code here
    res = ""
    while a:
        maxNum = 0
        for num in a:
            if concat(num,maxNum) >= concat(maxNum,num):
                maxNum = num
        res += str(maxNum)
        a.remove(maxNum)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))