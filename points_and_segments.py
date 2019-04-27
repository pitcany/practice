#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:32:08 2019

@author: yannik
"""

# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    n = len(points)
    cnt = [0] * n
    starts=[(p,0) for p in starts]
    ends=[(p,2) for p in ends]
    points=[(p,1) for p in points]
    points_indices=sorted(range(n), key=lambda k: points[k])
    segments_and_points=starts+ends+points
    segments_and_points.sort()
    counter = 0
    i=0
    for p in segments_and_points:
        if p[1] == 0:
            counter += 1
        elif p[1] == 2:
            counter -= 1
        elif p[1] == 1:
            cnt[points_indices[i]]=counter
            i+=1
    return cnt

#fast_count_segments([-10,100],[10,200],[-100,100,0])

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')