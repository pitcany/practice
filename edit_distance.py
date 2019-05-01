#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:31:37 2019

@author: yannik
"""

# Uses python3
def edit_distance(s, t):
    #write your code here
    def edit_distance(s,t,m,n):
            # table to record results of subproblems
            dp = [[0 for x in range(n+1)] for x in range(m+1)]
        
            # bottom up fill dp[][]
            for i in range(m+1):
                for j in range(n+1):
                
                    # if first string empty, insert all characters of second string
                    if i==0:
                        dp[i][j]=j
                
                    # second string empty, remove all characters of first string
                    elif j==0:
                        dp[i][j]=i
                    
                    # if last characters are same, ignore last char and recur for remaining string
                    elif s[i-1] == t[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    
                    # if last characters are different, consider all possibilities and find min
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        
            return dp[m][n]
    return edit_distance(s,t,len(s),len(t))

if __name__ == "__main__":
    print(edit_distance(input(), input()))
