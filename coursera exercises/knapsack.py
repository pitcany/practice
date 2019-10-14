#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:38:09 2019

@author: yannik
"""

# Uses python3
import sys

def optimal_weight(W, w):
    w.sort()
    rec = [[None for _ in range(len(w)+1)] for _ in range(W+1)]
    
    def optimal_weight_sub(W1,w1):
        if W1==0:
            rec[0][len(w1)] = 0
            return 0
        elif not w1:
            rec[W1][0] = 0
            return 0
        else:
            if rec[W1][len(w1)]:
                result = rec[W1][len(w1)]
            else:
                if w1[-1] <= W1:
                    result = max(optimal_weight_sub(W1,w1[:-1]),
                       optimal_weight_sub(W1-w1[-1],w1[:-1])+w1[-1])
                else:
                    result = optimal_weight_sub(W1,w1[:-1])
                rec[W1][len(w1)] = result
            return result
    
    return optimal_weight_sub(W,w)

def optimal_weight_bottomup(W,w):
    n = len(w)
    rec = [[0 for _ in range(n+1)] for _ in range(W+1)]
    #rec[i][j] is the max weight when using items up to w_{j-1} with capacity i
    for i in range(W+1):
        for j in range(n+1):
            if i==0 or j==0:
                rec[i][j] = 0
            elif w[j-1] <= i:
                rec[i][j] = max(w[j-1] + rec[i-w[j-1]][j-1], rec[i][j-1])
            else:
                rec[i][j] = rec[i][j-1]
    return rec[W][n]

#optimal_weight(10,[1,4,8])
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))