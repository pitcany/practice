#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:23:02 2019

@author: yannik
"""

# Uses python3
import sys

def CoinChange(S,n):
    S.sort()
    m=len(S)
    dp = [float("inf")]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i>=S[j]:
                dp[i]=min(dp[i],dp[i-S[j]]+1)
    
    if dp[n]==float("inf"):
        dp[n]=-1
        
    return(dp[n])

def get_change(m):
    return CoinChange([1,3,4],m)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))