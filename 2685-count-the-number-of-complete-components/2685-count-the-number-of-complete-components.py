class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node, elements):
            elements.append(node)
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    dfs(child, elements)
            return elements
        
        count = 0
        for i in range(n):
            if i not in visited:
                elements = []
                dfs(i, elements)
                # Count ages of this component
                total_edges = 0
                for node in elements:
                    total_edges += len(graph[node])
                total_edges //= 2

                num_node = len(elements)
                # Check if it's complate graph
                if total_edges == num_node * (num_node - 1) // 2:
                    count += 1
        return count

        
        
        