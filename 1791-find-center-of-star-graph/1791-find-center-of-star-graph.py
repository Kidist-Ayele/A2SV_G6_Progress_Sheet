class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        indegree = [0] * (len(edges) + 2)

        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
        
        for i, num in enumerate(indegree):
            if num == len(edges):
                return i

        