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

def pwin(x, y, tolerance):
    # Write your code here
    decimal_places=math.ceil(-math.log10(tolerance))
    num = 0
    n = len(x)
    m = len(y)
    for i in range(n):
        for j in range(m):
            if x[i]>y[j]:
                num += 1
    return round(num/(n*m),decimal_places)

def siftdown(i,arr):
    minIndex = i
    l = 2*i+1
    if l < len(arr) and arr[l] < arr[minIndex]:
        minIndex = l
    r = 2*i+2
    if r < len(arr) and arr[r] < arr[minIndex]:
        minIndex = r
    if i != minIndex:
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
        siftdown(minIndex,arr)
        
def buildheap(arr):
    size = len(arr)
    for i in range(size//2, -1, -1):
        siftdown(i,arr)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next

def increment(head):
     temp = head
     while temp is not None:
        temp.data +=1
        temp = temp.next



node1 = Node(10)
node2 = Node(20)
node1.next = node2
increment(node1)
printLL(node1)

