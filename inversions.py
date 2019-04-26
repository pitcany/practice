#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:28:22 2019

@author: yannik
"""

# Uses python3
import sys
from bisect import bisect_left

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        b[left]=a[left]
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # merge the halves together to get a sorted list
    # also count number of inversions where x in first half > y in second half
    i,j,k = left,ave,0
    for x in b[left:ave]:
        number_of_inversions += bisect_left(b[ave:right],x)
    temp = b[left:right]
    while ((b[i:ave] or b[j:right]) and k <= right-left-1):
        if not b[i:ave]:
            temp[k]=b[j]
        elif not b[j:right]:
            temp[k]=b[i]
        elif b[i]<=b[j]:
            temp[k]=b[i]
            i+=1
        elif b[i]>b[j]:
            temp[k]=b[j]
            j+=1
        k += 1
    b[left:right] = temp
    return number_of_inversions

#get_number_of_inversions([2,3,9,2,9],[0,0,0,0,0],0,5)
#get_number_of_inversions([4,3,2,1],[0,0,0,0],0,4)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))