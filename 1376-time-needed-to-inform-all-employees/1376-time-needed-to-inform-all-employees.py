class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i, mng in enumerate(manager):
            if mng != -1:
                graph[mng].append(i)
        
        def dfs(node):
            if not graph[node]:
                return 0

            max_time = 0
            
            for child in graph[node]:
                max_time = max(max_time, dfs(child))

            return informTime[node] + max_time

        return dfs(headID)



        