class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        # Reverse the direction: build child → parents map
        for v, u in edges:
            graph[u].append(v)


        ans = [set() for _ in range(n)] 
        visited = [False] * n
        
        def dfs(node):
            if visited[node]:
                return ans[node]


            for parent in graph[node]:
                ans[node].add(parent) 
                ans[node].update(dfs(parent))
    
            visited[node] = True
            return ans[node]

        for i in range(n):
            dfs(i)
        
        return [sorted(list(num)) for num in ans]




        