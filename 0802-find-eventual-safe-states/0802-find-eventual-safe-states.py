class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        reverse_graph = [[] for _ in range(n)]

        # Build reverse graph and compute indegrees
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                indegree[u] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        
        return sorted([i for i in range(n) if safe[i]])

        