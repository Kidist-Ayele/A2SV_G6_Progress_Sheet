class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        colors = [-1 for _ in range(n + 1)]

        def dfs(node, color):
            colors[node] = color

            for child in graph[node]:
                if colors[child] == -1:
                    if not dfs(child, not color):
                        return False
                elif colors[child] == color:
                    return False

            
            return True
            
        for i in range(1, n + 1):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True



        