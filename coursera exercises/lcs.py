#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:24:41 2019

@author: yannik
"""

#Uses python3

import sys

def lcs2(a, b):
    m,n = len(a),len(b)
    lcs_table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                lcs_table[i][j]=lcs_table[i-1][j-1]+1
            else:
                lcs_table[i][j]=max(lcs_table[i-1][j],lcs_table[i][j-1])
    
    return lcs_table[m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))