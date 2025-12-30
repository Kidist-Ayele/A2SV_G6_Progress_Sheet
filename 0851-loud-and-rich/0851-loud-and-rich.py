class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        indegree = [0] * n

        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        # print(indegree)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        # print(queue)
        
        result = [i for i in range(n)]
        # print(graph)
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                if quiet[result[node]] < quiet[result[child]]:
                    result[child] = result[node]

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    
        return result


