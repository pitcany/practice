#Uses python3

import sys
import queue
from heapq import heapify, heappop, heappush

class priority_queue():
    def __init__(self):
        self.queue = list()
        heapify(self.queue)
        self.index = dict()
    def push(self, priority, label):
        if label in self.index:
            self.queue = [(w,l)
                for w,l in self.queue if l!=label]
            heapify(self.queue)
        heappush(self.queue, (priority, label))
        self.index[label] = priority
    def pop(self):
        if self.queue:
            return heappop(self.queue)
    def __contains__(self, label):
        return label in self.index
    def __len__(self):
        return len(self.queue)

def distance(adj, cost, s, t):
    graphsize = len(adj)
    adj_cost = [dict(zip(adj[i],cost[i])) for i in range(graphsize)]
    inf = float('inf')
    known = set()
    priority = priority_queue()
    path = {s:s}
    
    for vertex in range(graphsize):
        if vertex == s:
            priority.push(0,vertex)
        else:
            priority.push(inf,vertex)
    last_node = s
    
    while last_node != t:
        (weight, actual_node) = priority.pop()
        if actual_node not in known:
            for next_node in adj_cost[actual_node]:
                upto_actual = priority.index[actual_node]
                upto_next = priority.index[next_node]
                to_next = upto_actual + \
                adj_cost[actual_node][next_node]
                if to_next < upto_next:
                    priority.push(to_next, next_node)
                    path[next_node] = actual_node
            last_node = actual_node
            known.add(actual_node)
    return priority.index[t] if priority.index[t] != inf else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))