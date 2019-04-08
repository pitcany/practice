#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:24:58 2019

@author: yannik
"""

from __future__ import print_function

class Graph():
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        print(self.vertex)
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge beween two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]

    def DFS(self):
        # visited array for storing already visited nodes
        visited = [False] * len(self.vertex)

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if visited[i] == False:
                self.DFSRec(i, visited)

    def DFSRec(self, startVertex, visited):
        # mark start vertex as visited
        visited[startVertex] = True

        print(startVertex, end = ' ')

        # Recur for all the vertexes that are adjacent to this node
        for i in self.vertex.keys():
            if visited[i] == False:
                self.DFSRec(i, visited)
                
class Solution(object):

    '''
    The number of partitions of a number n into at most k parts equals the number of partitions into exactly k parts
    plus the number of partitions into at most k-1 parts. Subtracting 1 from each part of a partition of n into k parts
    gives a partition of n-k into k parts. These two facts together are used for this algorithm.
    '''        
    def partition(self, m):
        memo = [[0 for _ in range(m)] for _ in range(m+1)]
        for i in range(m+1):
            memo[i][0] = 1
        
        for n in range(m+1):
            for k in range(1, m):
                memo[n][k] += memo[n][k-1]
                if n-k > 0:
                    memo[n][k] += memo[n-k-1][k]
                    
        return memo[m][m-1]        

    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
    
    def maxSubarraySumCircular(self,A):
        N = len(A)
        
        ans = cur = None
        for x in A:
            cur = x + max(cur,0)
            ans = max(ans,cur)
            
        # ans is soln for 1-interval subarrays, now look at 2-interval subarrays
        
        rightsums = [None]*N
        rightsums[-1] = A[-1]
        for i in range(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]
            
        maxright = [None]*N
        maxright[-1]=rightsums[-1]
        for i in range(N-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i]+A[i])
            
        leftsum = 0
        for i in range(N-2):
            leftsum += A[i]
            ans = max(ans, leftsum+maxright[i+2])
        
        return ans
    
    def findCircleNum(self, M):
        processed = set()
        cnt = 0
        for r in range(len(M)):
            if r not in processed:
                cnt += 1
                stack = [i for i,v in enumerate(M[r]) if i != r and v == 1]
                while stack:
                    curr = stack.pop()
                    if curr in processed: continue
                    processed.add(curr)
                    stack.extend([i for i,v in enumerate(M[curr]) if i != r and v == 1])
        return cnt
                
    def find3Nums(A, arr_size, sum):
        for i in range(0, arr_size-1):
            # Find pair in subarray A[i+1,...,n-1] with sum equal to sum-A[i]
            s = set()
            curr_sum = sum - A[i]
            for j in range(i+1, arr_size):
                if (curr_sum-A[j]) in s:
                    print(A[i],A[j],curr_sum-A[j])
                    return True
                s.add(A[j])
            
        return False
    
    def editDist(str1,str2):
        
        def editDist(str1,str2,m,n):
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
                    elif str1[i-1] == str2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    
                    # if last characters are different, consider all possibilities and find min
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        
            return dp[m][n]
        
        return editDist(str1,str2,len(str1),len(str2))
    
    '''coin change problem where S is an array of coins of length m and we want to count the number of ways to make change for n'''
    def dp_count(self,S,m,n):
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(m):
            for j in range(S[i],n+1):
                dp[j] += dp[j-S[i]]
                
        return dp[n]
                
    
if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()
    print('DFS:')
    g.DFS()
    
    print('\n')
    ykp=Solution()
    print(ykp.dp_count([1, 2, 3], 3, 4))  # answer 4
    print(ykp.dp_count([2, 5, 3, 6], 4, 10))  # answer 5

import numpy as np
from hmmlearn import hmm
np.random.seed(42)

startprob = np.array([0.6, 0.3, 0.1, 0.0])
# The transition matrix, note that there are no transitions possible
# between component 1 and 3
transmat = np.array([[0.7, 0.2, 0.0, 0.1],
                     [0.3, 0.5, 0.2, 0.0],
                     [0.0, 0.3, 0.5, 0.2],
                     [0.2, 0.0, 0.2, 0.6]])
# The means of each component
means = np.array([[0.0,  0.0],
                  [0.0, 11.0],
                  [9.0, 10.0],
                  [11.0, -1.0]])
# The covariance of each component
covars = .5 * np.tile(np.identity(2), (4, 1, 1))

# Build an HMM instance and set parameters
model = hmm.GaussianHMM(n_components=4, covariance_type="full")

# Instead of fitting it from the data, we directly set the estimated
# parameters, the means and covariance of the components
model.startprob_ = startprob
model.transmat_ = transmat
model.means_ = means
model.covars_ = covars

def ListPrimes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p < n):
        
        if (prime[p]==True):
            
            for i in range(2*p,n+1,p):
                prime[i]=False
                
        p += 1
    return([i for i in range(2,n+1) if prime[i]==True])
    
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

CoinChange([1,2,25483],5)

def gcd(a,b):
    if a==0:
        return (b)
    else:
        return(gcd(b%a,a))
        
def egcd(a, b):
	if b == 0:
		return((a, 1, 0))
	else:
		gcd, x, y = egcd(b, a%b)
		return((gcd, y, x-(a//b)*y))
    
egcd(3,2)

def products_not_elt_i(lst):
    ascending_product = [1]
    descending_product = [1]
    prod=1
    N=len(lst)
    
    for j in range(N):
        prod = prod*lst[j]
        ascending_product.append(prod)
    
    prod=1
    for k in range(-1,-N,-1):
        prod = prod*lst[k]
        descending_product.append(prod)
    
    for m in range(N):
        lst[m]=ascending_product[m]*descending_product[-(m+1)]
    return(lst)
    
def longest_unique_subarray(lst):

    def allUnique(lst):
        seen = list()
        return(not any(i in seen or seen.append(i) for i in lst))

    ans = 0
    for i in range(len(lst)):
        k=i
        seen=set()
        while ((k<len(lst)) and (lst[k] not in seen)):
            seen.add(lst[k])
            k+=1
        ans = max(ans,k-i+1)
    return(ans)

longest_unique_subarray([1,2,3,4,5,5]) 
#allUnique("ABCDEF")

def find_unsorted_subarray(nums):
    left, right = None, None
    n = len(nums)
    max_seen, min_seen = -float("inf"), float("inf")
    
    for i in range(n):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            right = i
    
    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            left = i
    
    return left,right

from math import floor,log,pow
def reverse(num):
    if num==0:
        return 0
    elif num<=9:
        return num
    else:
        num_digits = floor(log(num,10))+1
        return (num%10*pow(10,num_digits-1)+reverse(num//10))
    
find_unsorted_subarray([2,6,4,8,10,9,15])