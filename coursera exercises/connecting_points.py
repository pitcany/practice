#Uses python3
import sys
import math
from heapq import heappop, heappush

def minimum_distance(x, y):
    result = 0.
    #write your code here
    num_pts = len(x)
    nodes = []
    for i in range(num_pts):
    	makeSet(i, nodes, x, y)
    edges = []
    for i in range(num_pts):
    	for j in range(i+1, num_pts):
    		edges.append(Edge(i,j,weight(x[i],y[i],x[j],y[j])))
    edges = sorted(edges, key=lambda edge: edge.weight)
    for edge in edges:
    	if find(edge.u, nodes) != find(edge.v, nodes):
    		result += edge.weight
    		union(edge.u, edge.v, nodes)
    return result

class Node:
	def __init__(self, a, b, c):
		self.x = a
		self.y = b
		self.parent = c
		self.rank = 0

class Edge:
	def __init__(self, a, b, c):
		self.u = a
		self.v = b
		self.weight = c

def makeSet(i, nodes, x, y):
	nodes.append(Node(x[i],y[i],i))

def weight(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def find(i, nodes):
	if (i != nodes[i].parent):
		nodes[i].parent = find(nodes[i].parent, nodes)
	return nodes[i].parent

def union(u, v, nodes):
	p1 = find(u, nodes)
	p2 = find(v, nodes)
	if (p1 != p2):
		if (nodes[p1].rank > nodes[p2].rank):
			nodes[p2].parent = p1
		else:
			nodes[p1].parent = p2
			if (nodes[p1].rank == nodes[p2].rank):
				nodes[p2].rank += 1
	
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
