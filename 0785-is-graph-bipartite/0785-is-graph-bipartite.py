class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1 for _ in range(len(graph))]

        def dfs(node, color):             

            colors[node] = color

            for child in graph[node]:

                if colors[child] == -1:
                    if not dfs(child, not color):
                        return False
                elif colors[child] == colors[node]:
                    return False
                    
            return True

        for i, row in enumerate(graph):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

            
            


        