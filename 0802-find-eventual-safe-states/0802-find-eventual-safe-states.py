class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        new_g = defaultdict(list)
        outdegree = [0] * n

        for i, arr in enumerate(graph):
            outdegree[i] = len(arr)
            for num in arr:
                new_g[num].append(i)
        queue = deque()
        ans = []
    
        for i in range(n):
            if len(graph[i]) == 0:
                queue.append(i)
  
  
        print(new_g)
        while queue:
            node = queue.popleft()
            ans.append(node)
            for parent in new_g[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    queue.append(parent)
        ans.sort()
        return ans



        