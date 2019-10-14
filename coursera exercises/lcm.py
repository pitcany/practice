#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 02:30:19 2019

@author: yannik
"""

def gcd(a,b):
    if a==0:
        return (b)
    else:
        return(gcd(b%a,a))

def lcm(a,b):
    return a*int(b/gcd(a,b))
        
if __name__ == '__main__':
    a,b = map(int, input().split())
    print(lcm(a,b))
    
# 226553150
# 1023473145