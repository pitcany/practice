#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:49:54 2019

@author: yannik
"""

#def removechar(s,x):
#    words = s.split(" ")
#    for w in words:
#        w=w.replace(x,"")
#    words = " ".join(words)
#    s = s.replace(x,"")
#    print(s)
#
#def main():
#    removechar('Yannik likes statistics','a')
#    
#if __name__ == '__main__':
#    main()
    
def spiralPrint(arr):
    k,l = 0,0
    m,n = len(arr[0]),len(arr)
    #m and n are numbers of rows and columns
    ''' k - initial row
        l - initial column '''
        
    while (k < m and l < n):
        
        # print the first row
        for i in range(l,n):
            print(arr[k][i],end=' ')
        
        k += 1
        
        # print last column
        for i in range(k,m):
            print(arr[i][n-1],end=' ')
            
        n -= 1
        
        # print the last row
        if (k < m):
            for i in range(n-1,l-1,-1):
                print(arr[m-1][i],end=' ')
        
            m -= 1
            
        # print first column
        if (l < n):
            for i in range(m-1,k-1,-1):
                print(arr[i][l],end=' ')
            
            l += 1

def spiralPrint(m,n,a):
    k,l = 0,0
    
    #m and n are numbers of rows and columns
    ''' k - initial row
        l - initial column '''
        
    while (k < m and l < n):
        
        # print the first row
        for i in range(l,n):
            print(a[k][i],end=' ')
        
        k += 1
        
        # print last column
        for i in range(k,m):
            print(a[i][n-1],end=' ')
            
        n -= 1
        
        # print the last row
        if (k < m):
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=' ')
        
            m -= 1
            
        # print first column
        if (l < n):
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=' ')
            
            l += 1
        

def subset_sum(arr,n,target_sum,target_arr=[],ite=0):
    for i in range(ite,n):
        target_arr.append(arr[i])
#        print(target_arr)
        if sum(target_arr)==target_sum:
            print (target_arr, len(target_arr))
            target_arr.pop()
            subset_sum(arr,n,target_sum,target_arr,i+1)
            return
#        print(target_arr)
        subset_sum(arr,n,target_sum,target_arr,i+1)
        target_arr.pop()

def subset_sum_opt(arr,n,target_sum,target_arr=[],ite=0):
    for i in range(ite,n):
        target_arr.append(arr[i])
        if sum(target_arr)==target_sum:
            print (target_arr, len(target_arr))
            target_arr.pop()
            if i+1 < n:
                if sum(target_arr)+arr[i+1] <= target_sum:
                    subset_sum_opt(arr,n,target_sum,target_arr,i+1)
            return
#        print(target_arr)
        if sum(target_arr) <= target_sum:
            subset_sum_opt(arr,n,target_sum,target_arr,i+1)
        target_arr.pop()

subset_sum([1,2,3,4,5,6],6,12)
subset_sum([1,4,5,6,7,12,15,120],8,139)

subset_sum_opt([1,2,3,4,5,6],6,12)
subset_sum_opt([1,4,5,6,7,12,15,120],8,139)