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
                
    
#if __name__ == '__main__':
#    g = Graph()
#    g.addEdge(0, 1)
#    g.addEdge(0, 2)
#    g.addEdge(1, 2)
#    g.addEdge(2, 0)
#    g.addEdge(2, 3)
#    g.addEdge(3, 3)
#
#    g.printGraph()
#    print('DFS:')
#    g.DFS()
#    
#    print('\n')
#    ykp=Solution()
#    print(ykp.dp_count([1, 2, 3], 3, 4))  # answer 4
#    print(ykp.dp_count([2, 5, 3, 6], 4, 10))  # answer 5

#import numpy as np
#from hmmlearn import hmm
#np.random.seed(42)
#
#startprob = np.array([0.6, 0.3, 0.1, 0.0])
## The transition matrix, note that there are no transitions possible
## between component 1 and 3
#transmat = np.array([[0.7, 0.2, 0.0, 0.1],
#                     [0.3, 0.5, 0.2, 0.0],
#                     [0.0, 0.3, 0.5, 0.2],
#                     [0.2, 0.0, 0.2, 0.6]])
## The means of each component
#means = np.array([[0.0,  0.0],
#                  [0.0, 11.0],
#                  [9.0, 10.0],
#                  [11.0, -1.0]])
## The covariance of each component
#covars = .5 * np.tile(np.identity(2), (4, 1, 1))
#
## Build an HMM instance and set parameters
#model = hmm.GaussianHMM(n_components=4, covariance_type="full")
#
## Instead of fitting it from the data, we directly set the estimated
## parameters, the means and covariance of the components
#model.startprob_ = startprob
#model.transmat_ = transmat
#model.means_ = means
#model.covars_ = covars

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

#def getMedian(arr1,arr2,n):
#    
#    #no element in either array
#    if n == 0:
#        return -1
#    
#    # 1 element in each array
#    elif n == 1:
#        return (arr1[0]+arr2[0])/2
#    
#    # 2 elements in each
#    elif n == 2:
#        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
#
#    else:
#        m1 = median(arr1,n)
#        m2 = median(arr2,n)
#        
#        if m1 == m2:
#            return m1
#        
#        elif m1 < m2:
#            if n % 2 == 0:
#                return getMedian(arr1[(int(n/2)-1):],arr2[:(int(n/2)+1)],int(n/2)+1)
#            else:
#                return getMedian(arr1[(int(n/2)):],arr2[:(int(n/2)+1)],int(n/2)+1)
#        
#        else:
#            if n % 2 == 0:
#                return getMedian(arr1[:(int(n/2)+1)],arr2[(int(n/2)-1):],int(n/2)+1)
#            else:
#                return getMedian(arr1[:(int(n/2)+1)],arr2[(int(n/2)):],int(n/2)+1)
        
def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n/2) - 1] + arr[int(n/2)])/2
    else:
        return arr[int(n/2)]
    
#arr1 = [1,2,3,6,9,12,39,44]
#arr2 = [4,6,8,10,11,29,30,31,35]
#n = len(arr1)
#getMedian(arr1,arr2,n)


class Solution1:
    def findMedianSortedArrays(self,A,B):
        m = len(A)
        n = len(B)
    
        if ((m+n)%2 != 0):
            return self.findKth(A,0,m-1,B,0,n-1,(m+n)//2)
        else:
            return (self.findKth(A,0,m-1,B,0,n-1,(m+n)//2) + self.findKth(A,0,m-1,B,0,n-1,(m+n)//2-1))*0.5
                
    def findKth(self, A, p1, r1, B, p2, r2, k):
        # k means 'there are k elements beneath so this can go from 0 to n-1
    	n1 = r1-p1+1
    	n2 = r2-p2+1
    
    	if (n1 == 0):
    		return B[p2+k]
    	elif (n2 == 0):
    		return A[p1+k]
    	elif (k == 0):
    		return min(A[p1],B[p2])
    
    	i = int(n1*k/(n1+n2))
    	j = k-1-i
        # i + j + 1 = k
    
    	mid1 = min(p1+i, r1)
    	mid2 = min(p2+j, r2)
    
    	if (A[mid1] > B[mid2]):
    		k = k - (mid2-p2+1)
    		r1 = mid1
    		p2 = mid2+1
    	else:
    		k = k - (mid1-p1+1)
    		p1 = mid1+1
    		r2 = mid2
        
    	return self.findKth(A, p1, r1, B, p2, r2, k)
    
#ykp=Solution1()
#ykp.findKth([1,3,5,7],0,3,[2,4,6,8,10,11],0,5,0)

class Solution2:
    def TwoSum(self,nums):
        nums.sort()
        start = 0
        end = len(nums)-1
        while (start < end):
            if nums[start]+nums[end] < 0:
                start += 1
            elif nums[start]+nums[end] > 0:
                end -= 1
            else:
                return True
        return False
    
    def ThreeSum(self,nums,target):
        nums.sort()
        solns = []
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            if (i != 0 and nums[i]==nums[i-1]):
                continue
            while j<k:
                if (j != i+1 and nums[j]==nums[j-1]):
                        j+=1
                        continue
                if nums[i]+nums[j]+nums[k] < target:
                    j += 1
                elif nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                else:
                    solns.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        return solns
    
    def Foursum(self,nums,target):
        nums.sort()
        solns = []
        n = len(nums)
        for i in range(n-3):
            if (i != 0 and nums[i]==nums[i-1]):
                continue
            if (self.ThreeSum(nums[i+1:],target-nums[i]) != []):
                solns.extend([[nums[i]]+x for x in self.ThreeSum(nums[i+1:],target-nums[i])])
        return solns

ykp=Solution2()
#ykp.ThreeSum([3,5,9,-5,2,-8])
#ykp.ThreeSum([-2,0,0,2,2])
#ykp.TwoSum([3,5,9,-15,2])
#class NQueens:
#    
#    def __init__(self, size):
#        self.size = size
#        self.solutions = 0
#        self.solve()
#        
#    def solve(self):
#        positions = [-1] * self.size
#        self.put_queen(positions,0)
#        print("Found", self.solutions, "solutions.")
#    
#    def put_queen(self, positions, target_row):
#        if target_row == self.size:
#            self.show_full_board(positions)
#            self.solutions += 1
#        else:
#            for column in range(self.size):
#                if self.check_place(positions,target_row,column):
#                    positions[target_row] = column
#                    self.put_queen(positions, target_row+1)
#    
#    def check_place(self, positions, occupied_rows, column):
#        for i in range(occupied_rows):

        
"""The n queens puzzle."""
class NQueens:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, size):
        # Store the puzzle (problem) size and the number of valid solutions
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        """Solve the n queens puzzle and print the number of solutions"""
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.show_full_board(positions)
            # self.show_short_board(positions)
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, occupied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(occupied_rows):
            if positions[i] == column or \
                positions[i]-column == i-occupied_rows or \
                positions[i]-column == occupied_rows-i:
                return False
#            if positions[i] == column or \
#                positions[i] - i == column - occupied_rows or \
#                positions[i] + i == column + occupied_rows:
#                return False
        return True

    def show_full_board(self, positions):
        """Show the full NxN board"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        """
        Show the queens positions on the board in compressed form,
        each number represent the occupied column position in the corresponding row.
        """
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    """Initialize and solve the n queens puzzle"""
    NQueens(7)

#if __name__ == "__main__":
    # execute only if run as a script
#    main()

def dfs(G,s,S=None):
    if S is None: S=set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        dfs(G,u,S)

from collections import deque
def bfs(G,s):
    P,Q=set(s), deque([s])
#    P,Q={s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            P.add(v)
            Q.append(v)
    return P
        
def permutation(lst):
    if len(lst)==0:
        return []
    
    if len(lst)==1:
        return [lst]
    
    l = []
    
    for i in range(len(lst)):
        m=lst[i]
        remlst = lst[:i] + lst[(i+1):]
        
        for p in permutation(remlst):
            l.append([m]+p)
    return l

class NQueens_YKP:
    # board is a list of n elements...board[i] is the column
    # in the ith row where a queen is placed
    
    def represent(self,board):
        """Show the full NxN board"""
        new_board = []
        n = len(board)
        for row in range(n):
            line = ""
            for column in range(n):
                if board[row] == column:
                    line += "Q"
                else:
                    line += "."
            new_board.append(line)
        return(new_board)
    
    def find_configurations(self,n,board):
        if len(board)==n:
            return 1
            #return [self.represent(board)]
        
        #configs = []
        count = 0
        for i in range(n):
            board.append(i)
            if self.is_valid(board):
                count += self.find_configurations(n,board)
          #      configs.extend(self.find_configurations(n,board))
            board.pop()
        return count
        #return configs
    
    def is_valid(self,board):
        if board[-1] in board[:-1]:
            return False
        coords=[x for x in enumerate(board)]
        past_queens = coords[:-1]
        candidate = coords[-1]
        for past_queen in past_queens:
            if abs(candidate[1]-past_queen[1]) == candidate[0]-past_queen[0]:
                return False
        return True

ykp=NQueens_YKP()
ykp.find_configurations(8,[])