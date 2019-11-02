#Uses python3

import sys

sys.setrecursionlimit(200000)

# my_graph = {0:[1],3:[0],1:[2],2:[0]}
# my_graph2 = {4:[1,2],1:[0],2:[1,0],3:[2,0],0:[]}
# my_graph2 = [[],[0],[0,1],[0,2],[1,2]]
# def walk(G, s, S=set()):
#     P, Q = dict(), set()
#     P[s] = None
#     Q.add(s)
#     while Q:
#         u = Q.pop()
#         for v in G[u].difference(P,S):
#             Q.add(v)
#             P[v]=u
#     return P

def rec_walk(G, s, S=None, Z=set()): # now S represents visited nodes and Z is forbidden
    if s in Z:  # make sure we're not in forbidden zone
        return
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S.union(Z): continue
        rec_walk(G, u, S, Z)
    return S

def dfs_topsort(G):
    S, res = set(), []  # history and result
    def recurse(u):     # traversal subroutine
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

def tr(G):                  # transpose G
    GT = {}
    for u in G:
        GT[u] = set()       # get all nodes
    for u in G:
        for v in G[u]:
            GT[v].add(u)    # add all reverse edges
    return GT

def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen: continue
        C = rec_walk(GT, u, Z=seen)
        seen.update(C)
        sccs.append(C)
    return sccs

#scc(my_graph2)
#print(scc(my_graph2))

def number_of_strongly_connected_components(adj):
    return len(scc(adj))

#data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
#n,m = data[0:2]
#data = data[2:]
#edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#adj = {i:[] for i in range(n)}
#for (a, b) in edges:
#    adj[a - 1].append(b - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # adj = [[] for _ in range(n)]
    adj = {i:[] for i in range(n)}
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
