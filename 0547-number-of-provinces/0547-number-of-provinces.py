class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Change to adjacency list
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)

        # DFS traversal
        visited = set()

        def dfs(node):
            visited.add(node)

            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb)
        count = 0

        #Count connected provinces 
        for city in range(len(isConnected)):
            if city not in visited:
                    count += 1
                    dfs(city)
        return count

        