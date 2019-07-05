#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


INT_MIN, INT_MAX = -4294967296,4294967296
class Tree:
  def read(self,nodes,lines):
    self.n = nodes
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = lines[i]
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
     
  def isBSTUtil(self, ind, mini, maxi):
    # An empty tree is BST 
    if ind == -1:
        return True
      
    # False if this node violates min/max constraint 
    if self.key[ind] < mini or self.key[ind] > maxi: 
        return False
      
    # Otherwise check the subtrees recursively 
    # tightening the min or max constraint 
    return (self.isBSTUtil(self.left[ind], mini, self.key[ind]-1) and
        self.isBSTUtil(self.right[ind], self.key[ind], maxi)) 

  def isBST(self):
    if self.n == 0:
        return True
    else:
        return (self.isBSTUtil(0, INT_MIN, INT_MAX)) 
    
def main():
  tree = []
  nodes = int(sys.stdin.readline().strip())
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  new_tree = Tree()
  new_tree.read(nodes,tree)
  if new_tree.isBST():
    print("CORRECT")
  else:
    print("INCORRECT")


threading.Thread(target=main).start()
