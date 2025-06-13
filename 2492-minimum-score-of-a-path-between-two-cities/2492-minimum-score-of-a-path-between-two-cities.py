class Solution:
    def minScore(self, num_nodes: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        
        min_score = float('inf')
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for child, score in graph[node].items():
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
                min_score = min(min_score, score)
                
        return min_score