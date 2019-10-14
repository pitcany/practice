# python3

import sys
import threading
from collections import defaultdict, deque

class Node():
    def __init__(self,val=None,children=None):
        self.value = val
        if children is None:
            self.children = []
        else:
            self.children = children
        
    def addChild(self,new_children=[]):
        self.children.append(new_children)
            
#recursively compute height
#def compute_height(node):
#    if not node.children:
#        return 1
#    return 1+max([compute_height(node_child) for node_child in node.children])
        
#use bfs to compute height
def compute_height_bfs(n,parents,visited=deque()):
    nodeset=[Node(i) for i in range(n)]
    for node,parent in enumerate(parents):
        if parent == -1:
            root = nodeset[node]
        else:
            nodeset[parent].addChild(nodeset[node])
    heights=defaultdict(int)
    heights[root]=1
    visited.append(root)
    while visited:
        check_node = visited.popleft()
        visited.extend(check_node.children)
        for node in check_node.children:
            heights[node] = heights[check_node]+1
    return max(heights[node] for node in heights)

#first build the tree

#compute_height_bfs(5,[4,-1,4,1,1])
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_bfs(n, parents))
#
#
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
