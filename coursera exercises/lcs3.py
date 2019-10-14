#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:31:13 2019

@author: yannik
"""

import sys

def lcs3(a, b, c):
    l,m,n = len(a),len(b),len(c)
    lcs_table = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,m+1):
            for k in range(1,n+1):
                if a[i-1]==b[j-1]==c[k-1]:
                    lcs_table[i][j][k]=lcs_table[i-1][j-1][k-1]+1
                else:
                    lcs_table[i][j][k]=max(lcs_table[i-1][j][k],lcs_table[i][j-1][k],lcs_table[i][j][k-1])
    
    return lcs_table[l][m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
