#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:46:49 2019

@author: yannik
"""

# Uses python3
import sys

def get_majority_element(a, left, right):
    size = right-left
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    median = (left + right) // 2
    lhs_majority=get_majority_element(a, left, median)
    rhs_majority=get_majority_element(a, median, right)
    if (lhs_majority == -1 and rhs_majority == -1):
        return -1
    elif (lhs_majority != -1 and rhs_majority == -1):
        if count_occurrence(a[left:right],lhs_majority) > size//2:
            return lhs_majority
        else:
            return -1
    elif (lhs_majority == -1 and rhs_majority != -1):
        if count_occurrence(a[left:right],rhs_majority) > size//2:
            return rhs_majority
        else:
            return -1
    else:
        #check whether lhs_majority or rhs_majority is a majority in whole array
        if count_occurrence(a[left:right],lhs_majority) > size//2:
            return lhs_majority
        elif count_occurrence(a[left:right],rhs_majority) > size//2:
            return rhs_majority
        else:
            return -1

def count_occurrence(a,elt):
    return (sum([x == elt for x in a]))

#get_majority_element([1,2,3,1,5],0,5)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)