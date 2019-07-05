#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:15:37 2019

@author: yannik
"""

# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    # first place everything less than x to the left
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    # next place everything greater than x to the right traversing in reverse
    k = r+1
    for i in reversed(range(l+1, r+1)):
        if a[i] > x:
            k -= 1
            a[i], a[k] = a[k], a[i]
        elif a[i] < x:
            break
    return (j,k)

# trythis = [5,5,5,3,6,7,8,2,1,13,9,7]
# partition3(trythis,0,len(trythis)-1)

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # using partition 3
    start,end = partition3(a, l, r)
    randomized_quick_sort(a, l, start - 1);
    randomized_quick_sort(a, end, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')