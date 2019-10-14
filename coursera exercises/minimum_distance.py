#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:09:20 2019

@author: yannik
"""

#Uses python3
import sys
import math

def calc_dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def minimum_distance(points):
    n = len(points)
    points_sorted_by_x = sorted(points,key=lambda z:z[0])
    points_sorted_by_y = sorted(points,key=lambda z:z[1])
    if n <= 1:
        raise Exception
    elif n==2:
        (z1,z2) = points
        return calc_dist(z1,z2)
    elif n==3:
        (z1,z2,z3)=points
        localMin = calc_dist(z1,z2) if calc_dist(z1,z2) < calc_dist(z1,z3) else calc_dist(z1,z3)
        localMin = localMin if localMin < calc_dist(z2,z3) else calc_dist(z2,z3)
        return localMin
    else:
        #sort by x-axis and y-axis--points is sorted by x
        #points_sorted_by_y is sorted by y
        leftPoints = points_sorted_by_x[:int(n/2)]
        rightPoints = points_sorted_by_x[int(n/2):]
        
        #Divide and Conquer
        d1 = minimum_distance(leftPoints)
        d2 = minimum_distance(rightPoints)
        
        #min distances for left and right
        d = min(d1,d2)
        
        #cut self of points into half
        mid = (points_sorted_by_x[int(n/2)][0] + points_sorted_by_x[int(n/2) - 1][0])/2 if n%2 == 0 else points_sorted_by_x[int(n/2)][0]
        
        #find points in [mid-d,mid+d] sorted by y axis
        midRange = [z for z in points_sorted_by_y if mid-d <= z[0] <= mid+d]
        
        localMin = float("inf")

        for i in range(len(midRange)):
            a = midRange[i]
            for j in range(i+1, min(len(midRange),i+6)):
                b = midRange[j]
                if (abs(a[1]-b[1]) <= d and calc_dist(a,b) < localMin):
                    localMin = calc_dist(a,b)
        return min(localMin,d)
#minimum_distance([(0,0),(1,1),(0,2),(5,0)])
#minimum_distance([(7,7),(1,100),(4,8),(7,7)])
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = [z for z in zip(x,y)]
    print("{0:.9f}".format(minimum_distance(points)))