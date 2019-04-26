#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 02:25:13 2019

@author: yannik
"""
import sys

def gcd(a,b):
    if a==0:
        return (b)
    else:
        return(gcd(b%a,a))
        
#if __name__ == '__main__':
#    a,b = map(int, input().split())
#    print(gcd(a,b))

if __name__ == "__main__":
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(gcd(a, b))
