#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:18:11 2019

@author: yannik
"""

# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partition(S):
    if sum(S)%3 != 0:
        return 0
    else:
        k = sum(S)
        return partition_helper(S,len(S)-1,k/3,k/3,k/3,lookup={})

def partition_helper(S,n,a,b,c,lookup={}):
    if (a==0 and b==0 and c==0):
        return 1
    
    if (n<0):
        return 0
    
    key=(a,b,c)
    
    if key not in lookup:
        A,B,C = 0,0,0
        if (a - S[n] >= 0):
            A = partition_helper(S,n-1,a-S[n],b,c,lookup)
        elif (b - S[n] >= 0):
            B = partition_helper(S,n-1,a,b-S[n],c,lookup)
        elif (c - S[n] >= 0):
            C = partition_helper(S,n-1,a,b,c-S[n],lookup)
        lookup[key]= A or B or C
    
    return lookup[key]
        
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))