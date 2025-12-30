class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        print(graph)
        queue = deque()
        ancestors = [set() for _ in range(n)]

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        print(queue)
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                ancestors[child].add(node)
                ancestors[child].update(ancestors[node])

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
           

        return [sorted(list(a)) for a in ancestors]
        