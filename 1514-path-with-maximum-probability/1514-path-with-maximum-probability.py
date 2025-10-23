class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]
            graph[u].append([v, w])
            graph[v].append([u, w])
        dist = [0] * n
        dist[start_node] = 1

        heap = [(-1, start_node)]
        while heap:
            curr, node = heappop(heap)
            curr = -curr
            if node == end_node:
                return curr

            for child, prob in graph[node]:
                if curr * prob > dist[child]:
                    dist[child] = curr * prob
                    heappush(heap, [-dist[child], child])
        return 0
        