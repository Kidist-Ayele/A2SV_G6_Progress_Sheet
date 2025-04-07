class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    f = dfs(n, visited)
                    if f:
                        return True
            return False
        return dfs(source, visited)



        