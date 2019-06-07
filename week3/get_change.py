#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:43:56 2019

@author: yannik
"""

# Uses python3

def get_change(m):
    dimes = m // 10
    nickels = (m - 10*dimes) // 5
    pennies = m - 10*dimes - 5*nickels
    return dimes+nickels+pennies

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))