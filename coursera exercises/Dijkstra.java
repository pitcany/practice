import java.util.*;

class PriorityQueueWithDecrease {
    private PriorityQueue<int[]> pq;
    private Map<Integer, Integer> index;

    public PriorityQueueWithDecrease(int n) {
        pq = new PriorityQueue<>(n, Comparator.comparingInt(a -> a[1]));
        index = new HashMap<>();
    }

    public void push(int vertex, int priority) {
        if (index.containsKey(vertex)) {
            pq.remove(new int[]{vertex, index.get(vertex)});
        }
        pq.add(new int[]{vertex, priority});
        index.put(vertex, priority);
    }

    public int[] pop() {
        return pq.poll();
    }

    public boolean contains(int vertex) {
        return index.containsKey(vertex);
    }

    public int size() {
        return pq.size();
    }
}

public class Dijkstra {
    private static long distance(ArrayList<Integer>[] adj, ArrayList<Integer>[] cost, int s, int t) {
        int graphSize = adj.length;
        Map<Integer, Integer>[] adjCost = new Map[graphSize];
        for (int i = 0; i < graphSize; i++) {
            adjCost[i] = new HashMap<>();
            for (int j = 0; j < adj[i].size(); j++) {
                adjCost[i].put(adj[i].get(j), cost[i].get(j));
            }
        }

        long[] distance = new long[graphSize];
        Arrays.fill(distance, Long.MAX_VALUE);
        distance[s] = 0;

        int[] path = new int[graphSize];
        Arrays.fill(path, -1);
        path[s] = s;

        Set<Integer> known = new HashSet<>();
        PriorityQueueWithDecrease pq = new PriorityQueueWithDecrease(graphSize);
        pq.push(s, 0);

        while (pq.size() > 0) {
            int[] top = pq.pop();
            int actualNode = top[0];
            long weight = top[1];

            if (known.contains(actualNode)) {
                continue;
            }

            known.add(actualNode);

            for (Map.Entry<Integer, Integer> entry : adjCost[actualNode].entrySet()) {
                int nextNode = entry.getKey();
                int edgeCost = entry.getValue();
                if (distance[actualNode] + edgeCost < distance[nextNode]) {
                    distance[nextNode] = distance[actualNode] + edgeCost;
                    pq.push(nextNode, (int) distance[nextNode]);
                    path[nextNode] = actualNode;
                }
            }
        }

        return distance[t] != Long.MAX_VALUE ? distance[t] : -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        ArrayList<Integer>[] adj = (ArrayList<Integer>[])new ArrayList[n];
        ArrayList<Integer>[] cost = (ArrayList<Integer>[])new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<Integer>();
            cost[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) {
            int x, y, w;
            x = scanner.nextInt();
            y = scanner.nextInt();
            w = scanner.nextInt();
            adj[x - 1].add(y - 1);
            cost[x - 1].add(w);
        }
        int x = scanner.nextInt() - 1;
        int y = scanner.nextInt() - 1;
        System.out.println(distance(adj, cost, x, y));
    }
}

