#Uses python3

import sys

def propagate_negative_cycle(adj, u, shortest):
    shortest[u] = 0
    for v in adj[u]:
        if shortest[v] == 1:
            propagate_negative_cycle(adj, v, shortest)

def shortest_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1

    for _ in range(len(adj) - 1):
        for u in range(len(adj)):
            for v, c in zip(adj[u], cost[u]):
                if distance[u] + c < distance[v] and distance[u] != 10**19:
                    distance[v] = distance[u] + c
                    reachable[v] = 1

    # Run the algorithm once more to find vertices that are part of or reachable by negative cycles
    for u in range(len(adj)):
        for v, c in zip(adj[u], cost[u]):
            if distance[u] + c < distance[v] and distance[u] != 10**19:
                shortest[v] = 0
                # negative cycle info for all reachable vertices from v
                propagate_negative_cycle(adj, v, shortest)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

