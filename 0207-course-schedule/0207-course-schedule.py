class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for courses in prerequisites:
            a, b = courses
            graph[a].append(b)

        colors = [-1 for _ in range(numCourses)]

        def dfs(node, color):
            colors[node] = color

            for child in graph[node]:
                if colors[child] == -1:
                    if not dfs(child, color):
                        return False
                elif colors[child] == 0:
                    return False

            colors[node] = 1
            return True
            
        for i in range(numCourses):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


            

        