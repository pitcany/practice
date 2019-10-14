#Uses python3

import sys

inf = float('inf')
#def relax(W, u, v, D, P):
#    d = D.get(u,inf)+W[u][v]
#    if d < D.get(v,inf):
#        D[v], P[v] = d, u
#        return True
 
def relax(adj, cost, u, v, D, P):
    d = D.get(u,inf)+cost[u][adj[u].index(v)]
    if d < D.get(v,inf):
        D[v], P[v] = d, u
        return True
    
#def create_cost_fn(adj,cost):
#    abc = list(zip(adj,cost))
#    cost_fn = []
#    for (a,b) in abc:
#        cost_fn.append(list(zip(a,b)))
#    
#    W=[[inf for _ in range(len(adj))] for _ in range(len(adj))]
#    for i in range(len(cost_fn)):
#        for (j,k) in cost_fn[i]:
#            W[i][j]=k
#    return W
    
#def negative_cycle(adj, cost, s):
#    D,P = {s:0}, {}
#    W=create_cost_fn(adj, cost)
#    for rnd in adj:
#        changed = False
#        for u in range(len(adj)):
#            for v in adj[u]:
#                if relax(W, u, v, D, P):
#                    changed = True
#        if not changed:
#            neg_cycle = 0
#            break
#    else:
#        neg_cycle = 1
#        #raise ValueError('negative cycle')
#    return neg_cycle #D,P

def negative_cycle_disconnected(adj, cost):
    
    def negative_cycle(adj, cost, s, visited):
        #visited[s]=True
        D,P = {s:0}, {}
        #W=create_cost_fn(adj,cost)
        for rnd in adj:
            changed = False
            for u in range(len(adj)):
                for v in adj[u]:
                    if relax(adj, cost, u, v, D, P):
                        changed = True
            if not changed:
                neg_cycle = 0
                break
        else:
            neg_cycle = 1
        #update visited
        for v in D: visited[v]=True
        return neg_cycle
    
    visited=[False]*len(adj)
    while not all(visited):
        s = visited.index(False)
        if negative_cycle(adj, cost, s, visited):
            return 1
    return 0
    #return 1 if any([negative_cycle(adj, cost, s) for s in range(len(adj))]) else 0
#data = [4,4,1,2,-5,4,1,2,2,3,2,3,1,1]
#n, m = data[0:2]
#data = data[2:]
#edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#data = data[3 * m:]
#adj = [[] for _ in range(n)]
#cost = [[] for _ in range(n)]
#for ((a, b), w) in edges:
#    adj[a - 1].append(b - 1)
#    cost[a - 1].append(w)
    
#adj=[[1], [2], [0], [0]]
#cost=[[-5], [2], [1], [2]]
#create_cost_fn(adj,cost)
#[i for i, j in enumerate(['foo', 'bar', 'baz']) if j == 'bar']
#
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle_disconnected(adj, cost))
