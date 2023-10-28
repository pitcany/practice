#Uses python3

import sys
from collections import deque

def negative_cycle1(adj, cost):
    for src in range(len(adj)):
        distance = [10**19]*(len(adj))
        distance[src] = 0
    
        for _ in range(len(adj)-1):
            for u in range(len(adj)):
                for v, c in zip(adj[u], cost[u]):
                    if distance[u] + c < distance[v] and distance[u] != 10**19:
                        distance[v] = distance[u] + c
        
        for u in range(len(adj)):
            for v, c in zip(adj[u], cost[u]):
                if distance[u] + c < distance[v] and distance[u] != 10**19:
                    return 1
    return 0

def negative_cycle(adj, cost):
    for src in range(len(adj)):
        distance = [10**19] * len(adj)
        distance[src] = 0
        active_vertices = deque([src])
        visited = [False] * len(adj)
        visited[src] = True
        relaxations = 0
        
        while active_vertices:
            u = active_vertices.popleft()
            visited[u] = False
            for v, c in zip(adj[u], cost[u]):
                if distance[u] + c < distance[v] and distance[u] != 10**19:
                    distance[v] = distance[u] + c
                    if not visited[v]:
                        active_vertices.append(v)
                        visited[v] = True
                        relaxations += 1
                        if relaxations >= len(adj) * len(adj):
                            return 1
    
    return 0

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
    print(negative_cycle(adj, cost))
